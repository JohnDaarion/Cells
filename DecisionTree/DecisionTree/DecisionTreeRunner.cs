using Accord.MachineLearning.DecisionTrees;
using Accord.MachineLearning.DecisionTrees.Learning;
using Accord.Math;
using Accord.Statistics.Filters;
using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DecisionTree
{
    public class DecisionTreeRunner
    {
        public Accord.MachineLearning.DecisionTrees.DecisionTree Learn(string[][] records , string[] columnNamesWithoutResult , ref Codification codebook)
        {
            DataTable data = new DataTable();
            
            foreach(var columnName in records[0])
            {
                data.Columns.Add(columnName);
            }

            int rowsAdderCounter = 0;
            foreach (var record in records)
            {
                if (rowsAdderCounter == 0)
                {
                    rowsAdderCounter++;
                    continue;
                }

                data.Rows.Add(record);
            }

            double[][] inputs = data.ToJagged(columnNamesWithoutResult);
            string[] labels = data.ToArray<string>(Constants.RESULT_COLUMN_NAME);           

            int[] outputs = codebook.Translate(Constants.RESULT_COLUMN_NAME, labels);

            var teacher = new C45Learning();

            foreach (var columnName in columnNamesWithoutResult)
            {
                DecisionVariable decVar = new DecisionVariable(columnName, DecisionVariableKind.Continuous);
                teacher.Add(decVar);
            }

            Accord.MachineLearning.DecisionTrees.DecisionTree tree = teacher.Learn(inputs, outputs);

            return tree;
        }

        public string Decide(Accord.MachineLearning.DecisionTrees.DecisionTree tree , Codification codebook , params double[] query)
        {
            int predicted = tree.Decide(query);

            return codebook.Revert(Constants.RESULT_COLUMN_NAME, predicted);
        }
    }
}

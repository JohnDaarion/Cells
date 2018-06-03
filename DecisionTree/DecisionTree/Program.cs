using Accord.Statistics.Filters;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DecisionTree
{
    class Program
    {
        static void Main(string[] args)
        {
            var codebook = new Codification(Constants.RESULT_COLUMN_NAME, Constants.LABELS);
            string[] columnNames = null;
            CsvParser parser = new CsvParser();
            string[][] records = parser.Parse(Constants.DATA_FILE_PATH , "B" , out columnNames);
            DecisionTreeRunner runner = new DecisionTreeRunner();
            Accord.MachineLearning.DecisionTrees.DecisionTree tree  =  runner.Learn(records ,  columnNames , ref codebook);
            var result = runner.Decide(tree, codebook, 1500, 2.5, 90, 36.260616, 34.336563, 1.227892, 1.600787, 0.932787, 0.877746, 33, 0.583594, 108.999000, 146.660377, 84, 217);
            Console.Out.Write($"Dla wartości 1500, 2.5, 90, 36.260616, 34.336563, 1.227892, 1.600787, 0.932787, 0.877746, 33, 0.583594, 108.999000, 146.660377, 84, 217 wynikiem jest: { result }");
        }
    }
}

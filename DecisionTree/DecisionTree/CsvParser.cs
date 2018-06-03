using Accord.Math;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DecisionTree
{
    public class CsvParser
    {
        public string[][] Parse (string path , string expectedCelluleType , out string[] columnNames)
        {
            var records = File.ReadLines(path)
                              .Select(a => a.Split(';'))
                              .ToArray();

            for (int i = 0; i < records.Length; i++)
            {
                records[i] = Array.ConvertAll(records[i], s => s.Replace('.', ','));
            }

            string[] columnNamesWithoutResult = null;

            int recordsSize = records.Length;

            for (int i = 0; i < recordsSize; i++)
            {
                records[i] = records[i].RemoveAt(0);
                records[i] = records[i].RemoveAt(0);

                if (i == 0)
                {
                    columnNamesWithoutResult = records[0];
                    records[i] = records[i].Concatenate(Constants.RESULT_COLUMN_NAME);
                    continue;
                }

                records[i] = records[i].Concatenate(expectedCelluleType);
            }

            columnNames = columnNamesWithoutResult;

            return records;
        }
    }
}

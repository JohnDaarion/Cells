using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using NaiveBayesClassifier.Implementation;

namespace NaiveBayesClassifier.DataProvider
{
    public class MockDataProvider : IDataProvider
    {
        public InformationModel FromCsv(string csvLine, string cat)
        {
            List<string> tempList = new List<string>();
            string[] values = csvLine.Split(';');

            for (int i = 0; i < values.Length; i++)
            {
                if (i == 0 || i == 1)
                {
                    continue;
                }

                tempList.Add(values[i]);
            }

            return new InformationModel() { Lable = cat, Features = tempList };
        }

        public object GetTrainingData(string pPath, string pExclude, ExcludeType pExcludeType)
        {
            DirectoryInfo di =
                new DirectoryInfo(pPath + "\\letterM");
            List<InformationModel> values = new List<InformationModel>();

            foreach (var csv in di.GetFiles("*.csv"))
            {
                if (pExcludeType == ExcludeType.m && csv.Name == pExclude)
                {
                    continue;
                }

                values.AddRange(File.ReadAllLines(csv.FullName)
                    .Skip(1)
                    .Select(v => FromCsv(v, "m"))
                    .ToList());
            }
            
            di = new DirectoryInfo(pPath + "\\letterB");

            foreach (var csv in di.GetFiles("*.csv"))
            {
                if (pExcludeType == ExcludeType.b && csv.Name == pExclude)
                {
                    continue;
                }

                values.AddRange(File.ReadAllLines(csv.FullName)
                    .Skip(1)
                    .Select(v => FromCsv(v, "b"))
                    .ToList());
            }


            di = new DirectoryInfo(pPath + "\\letterF");

            foreach (var csv in di.GetFiles("*.csv"))
            {
                if (pExcludeType == ExcludeType.f && csv.Name == pExclude)
                {
                    continue;
                }

                values.AddRange(File.ReadAllLines(csv.FullName)
                    .Skip(1)
                    .Select(v => FromCsv(v, "f"))
                    .ToList());
            }
            
            return values;
        }

        public void SaveTrainingData(object modelInfos)
        {
            if (modelInfos == null)
                throw new ArgumentNullException();

            throw new NotImplementedException();
        }
    }

    public enum ExcludeType
    {
        m, f, b
    }
}

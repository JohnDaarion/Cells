using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NaiveBayesClassifier.DataProvider;
using NaiveBayesClassifier.Implementation;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        { 
            string pathToData = "DATA";
            string pathToResults = "wynik.txt";
            bool runOneTime = true;
            DirectoryInfo di = new DirectoryInfo(pathToData + "\\letterB");

            using (var tw = new StreamWriter(pathToResults, true))
            {
                foreach (var csv in di.GetFiles("*.csv"))
                {
                    IDataProvider dataProvider = new MockDataProvider();
                    Classifier<string> classifier = new Classifier<string>();

                    var sampleData = dataProvider.GetTrainingData(pathToData, csv.Name, ExcludeType.b) as List<InformationModel>;

                    classifier.Teach(sampleData);

                    List<List<string>> values = new List<List<string>>();

                    values.AddRange(File.ReadAllLines(csv.FullName)
                        .Skip(1)
                        .Select(FromCsv)
                        .ToList());

                    Dictionary<string, int> counter = new Dictionary<string, int>() { { "m", 0 }, { "f", 0 }, { "b", 0 } };

                    foreach (var list in values)
                    {
                        IDictionary<string, double> tempDict = classifier.Classify(list);
                        double min = 0;
                        string cat = "";

                        foreach (var item in tempDict)
                        {
                            if (min == 0 || min > item.Value)
                            {
                                min = item.Value;
                                cat = item.Key;
                            }
                        }

                        counter[cat]++;
                    }

                    foreach (var item in counter)
                    {
                        tw.Write("{1}; ", item.Key, item.Value);
                    }

                    tw.WriteLine();

                    if (runOneTime)
                    {
                        break;
                    }
                }
            }
        }

        public static List<string> FromCsv(string csvLine)
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

            return tempList;
        }
    }
}

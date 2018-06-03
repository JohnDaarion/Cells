using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace NaiveBayesClassifier.DataProvider
{
    public interface IDataProvider
    {
        object GetTrainingData(string pPath, string pExclude, ExcludeType pExcludeType);
        void SaveTrainingData(object modelInfos);
    }
}

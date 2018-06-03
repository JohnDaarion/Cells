/*
 *  @Author: Adam Wyrembelski
 *  @Data: 12.10.2012.
 *  @Project: NaiveBayesClassifier 
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace NaiveBayesClassifier.Implementation
{
    public class InformationModel
    {
        /// <summary>
        /// Object category
        /// </summary>
        public string Lable { get; set; }
        
        /// <summary>
        /// List of object features 
        /// </summary>
        public List<string> Features { get; set; }
    }
}

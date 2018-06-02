import os
import re
# Path to source
path = "/home/mg/PycharmProjects/csvMerger/src/resources"
listOfNames = []
dic = {'test': 1}
for filename in os.listdir(path):
    listOfNames.append(filename)

for name in listOfNames:
    m = re.search('.*[0-9]+(.*)\.csv', name)
    case = m.group(1)
    if dic.__contains__(case):
        dic[case] = dic[case] + 1
    else:
        dic[case] = 1

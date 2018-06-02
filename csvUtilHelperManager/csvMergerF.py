import os
import re

#Path to source
path = "/home/mg/PycharmProjects/csvMerger/src/resourcesF"
listOfNames = []
dic = {'dummy': []}
for _outputFilename in os.listdir(path):
    listOfNames.append(_outputFilename)

for name in listOfNames:
    m = re.search('.*[0-9]+(.*)\.csv', name)
    case = m.group(1)
    if dic.__contains__(case):
        dic[case].append(name)
    else:
        dic[case] = [name]


i = 0
j = 0

counter = 1
regex = re.compile(r'^[0-9]+;')

for canal in dic:
    #Path to output
    _outputFilename = "/home/mg/PycharmProjects/csvMerger/src/letterF/F" + canal + ".csv"
    f = open(_outputFilename, "a")
    for file in dic[canal]:
        for line in open(path + "/" + file):
            if j == 0:
                f.write(line)
                j = j + 1
                continue
            if i == 0:
                i = i + 1
                continue

            f.write(re.sub(regex, str(counter) + ";", line))
            counter = counter + 1
            i = i + 1
        i = 0
    j = 0
    counter = 1
    f.close()



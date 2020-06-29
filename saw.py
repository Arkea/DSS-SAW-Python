import csv
import numpy

attribArray = []
weightArray = []
minMaxedArray = []
listedData = []
arrayOfData = []

with open('criteria.csv') as csv_file:  # criteria
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            attribArray.append(row[1])
            weightArray.append(row[2])
            line_count += 1

with open('inputData.csv') as csv_file: # input data
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            for x in range(len(row)):
                try:
                    if attribArray[x] == 'cost' and float(minMaxedArray[x]) > float(row[x]):
                        minMaxedArray[x] = row[x]
                    elif attribArray[x] == 'benefit' and float(minMaxedArray[x]) < float(row[x]):
                        minMaxedArray[x] = row[x]
                except:
                    minMaxedArray.append(row[x])
            arrayOfData.append(row)
            line_count += 1

# normalisasi
normalizedData = []
for x in arrayOfData:
    normalizedLine = []
    for y in range(len(x)):
        if attribArray[y] == 'cost':
            normalizedLine.append(float(minMaxedArray[y])/float(x[y]))
        else:
            normalizedLine.append(float(x[y])/float(minMaxedArray[y]))
    normalizedData.append(normalizedLine)

# grade
grade = []
for x in normalizedData:
    sumgrade = 0
    for y in range(len(x)):
        sumgrade += x[y]*float(weightArray[y])
    grade.append(sumgrade)

print(grade)

# ranking
array = numpy.array(grade)
temp = array.argsort()
rank = numpy.empty_like(temp)
rank[temp] = numpy.arange(len(array))

with open('rank.csv', 'w') as csv_file: # write result
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    arrayLen = len(rank)
    csv_writer.writerow(['index', 'grade', 'rank'])
    for x in range(len(grade)):
        csv_writer.writerow([x, grade[x], (arrayLen-rank[x])])
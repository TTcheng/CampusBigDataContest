# 第一种方法 字符形式
import csv
with open('csvtest1.csv',newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    info = []
    for row in csvreader:
        # row : list
        info.append(row)
        # print(','.join(row))
    print(info)


# 第二种方法 数字形式
import pandas
data = pandas.read_csv('csvtest.csv')
matrix = data.as_matrix()
# print(data.__array__())
# print(data)
print(matrix)
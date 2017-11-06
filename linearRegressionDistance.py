# 将四个坐标特征复合成一个表示距离的特征，这种方式不可取

import pandas as pd
from math import sqrt
from sklearn.linear_model import LinearRegression


def getDistance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)


# Function to get data
def getData(file_name):
    # 将.csv数据读入Pandas数据帧。
    data = pd.read_csv(file_name)
    distance = []
    for each_x1, each_y1, each_x2, each_y2 in zip(data['x1'], data['y1'],data['x2'],data['y2']):
        each_distance = getDistance(each_x1, each_y1, each_x2, each_y2)
        distance.append(each_distance)
    xDataFrame = pd.DataFrame({'distance':distance,'population_size1':data.population_size1,'population_size2':data.population_size2,'temperature':data.temperature,'queue_len':data.queue_len})
    # select a Series from the DataFrame
    ySeries = data['rate']
    # ySeries = data.rate
    return xDataFrame,ySeries


# y=β0+β1∗distance+β2∗population1+...+β8∗maxQueueLen
def regressionModel(X_parameter, Y_parameter, xPrediction): # , predict_X):
    # 1. 构造回归对象
    regr = LinearRegression()
    # linear_model.
    regr.fit(X_parameter, Y_parameter)
    predictions = regr.predict(xPrediction)

    return predictions

    # regr.fit(trainSet)
    # regr.predict(testSet)   # 预测
    # regr.coef_              # 回归系数
    # regr.intercept_         # 截距


def writeFile(text):
    # write rate to csv file
    f = open('res.csv', 'a')
    for row in text:
        f.writelines(str(row) + '\n')
    f.close()


if __name__ == '__main__':
    xTrain, yTrain = getData('train.csv')
    xTest, yTest = getData('test.csv')

    predictions = regressionModel(xTrain, yTrain,xTest) #getRegressionCoefficient
    writeFile(predictions)

    # print('回归系数：')
    # print(ceof)

    # print(type(x))
    # print(x)
    # print(type(y))
    # print(y)


# x1,y1,x2,y2,population_size1,population_size2,temperature,queue_len,rate

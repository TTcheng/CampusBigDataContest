# Required Packages
import pandas as pd
from sklearn.linear_model import LinearRegression


# 表头 x1,y1,x2,y2,population_size1,population_size2,temperature,queue_len,rate
# Function to get data
def getData(file_name):
    # 将.csv数据读入Pandas数据帧。
    data = pd.read_csv(file_name)

    ySeries = data['rate']
    data.__delitem__('rate')
    return data,ySeries


# y=β0+β1∗distance+β2∗population1+...+β8∗maxQueueLen
def regressionModel(X_parameter, Y_parameter, xPrediction): # , predict_X):
    # 1. 构造回归对象
    regr = LinearRegression()
    # linear_model.
    regr.fit(X_parameter, Y_parameter)          # 拟合
    predictions = regr.predict(xPrediction)     # 得到预测结果并返回
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
    xTrain, yTrain = getData('train.csv')   # 读入训练集数据，并转换成LinearRegression支持的数据类型
    xTest, yTest = getData('test.csv')      #

    predictions = regressionModel(xTrain, yTrain,xTest)
    writeFile(predictions)


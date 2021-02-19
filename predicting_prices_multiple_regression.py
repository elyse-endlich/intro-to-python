from random import random
from altair import Data, Chart


# dot product
def dot(a, b):
    dot = 0
    for x in a:
        index = a.index(x)
        y = b[index]
        dot += x * y
    return dot


array = [[6, 2, 1], [8, 1, 1], [10, 0, 1], [14, 2, 1], [18, 0, 1]]
prices_actual = [7, 9, 13, 17.5, 18]
coefficients = []

for _ in range(3):
    coefficients.append(random())


def dot(a, b):
    dot = 0
    for aa in a:
        index = a.index(aa)
        bb = b[index]
        dot += aa * bb
    return dot


def compute_all_y(array_of_x, list_of_coefs):
    list_of_y = []
    for x in array_of_x:
        y = dot(x, list_of_coefs)
        list_of_y.append(y)
    return list_of_y


def compute_mse(list_of_known, list_of_predictions):
    list_of_error = []
    total = 0
    count = 0
    mse = 0
    for index in range(len(list_of_known)):
        error = list_of_known[index] - list_of_predictions[index]
        list_of_error.append(error)
    for error in list_of_error:
        error = error * error
        total += error
        count += 1
    mse = total / count
    return mse


trials = 1000
MSE_list = []
attempt = []
count = 0

for i in range(trials):
    prices_predict = compute_all_y(array, coefficients)
    MSE1 = compute_mse(prices_actual, prices_predict)
    coefficients[0] = coefficients[0] + 0.01
    prices_predict = compute_all_y(array, coefficients)
    MSE2 = compute_mse(prices_actual, prices_predict)
    if MSE2 > MSE1:
        coefficients[0] = coefficients[0] - 0.02
        prices_predict = compute_all_y(array, coefficients)
        MSE3 = compute_mse(prices_actual, prices_predict)
        if MSE3 < MSE1:
            MSE1 = MSE3
    else:
        MSE1 = MSE2
    coefficients[1] = coefficients[1] + 0.01
    prices_predict = compute_all_y(array, coefficients)
    MSE2 = compute_mse(prices_actual, prices_predict)
    if MSE2 > MSE1:
        coefficients[1] = coefficients[1] - 0.02
        prices_predict = compute_all_y(array, coefficients)
        MSE3 = compute_mse(prices_actual, prices_predict)
        if MSE3 < MSE1:
            MSE1 = MSE3
    else:
        MSE1 = MSE2
    coefficients[2] = coefficients[2] + 0.01
    prices_predict = compute_all_y(array, coefficients)
    MSE2 = compute_mse(prices_actual, prices_predict)
    if MSE2 > MSE1:
        coefficients[2] = coefficients[2] - 0.02
        prices_predict = compute_all_y(array, coefficients)
        MSE3 = compute_mse(prices_actual, prices_predict)
        if MSE3 < MSE1:
            MSE1 = MSE3
    else:
        MSE1 = MSE2
    MSE_list.append(MSE1)
    count += 1
    attempt.append(count)

data = Data(attempt=attempt, MSE_list=MSE_list)
chart = Chart(data)
mark = chart.mark_point()
enc = mark.encode(x='attempt:Q', y='MSE_list:Q', )
enc.display()

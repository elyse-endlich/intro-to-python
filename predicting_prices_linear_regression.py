from altair import Data, Chart

# scatter plot

data = Data(diameter=[6, 8, 10, 14, 18], price=[7, 9, 13, 17.5, 18])
chart = Chart(data)
mark = chart.mark_point()
enc = mark.encode(x='diameter:Q', y='price:Q', )
enc.display()

# calculate price
prices = []
diameters = [6, 8, 10, 14, 18]

for diameter in diameters:
    price = (diameter * 0.7) + 5
    prices.append(price)
print(prices)

# plot prices

prices = [7, 9, 13, 17.5, 18]
diameters = [6, 8, 10, 14, 18]

for diameter in diameters:
    price = (diameter * 0.7) + 5
    prices.append(price)
diameters = diameters * 2

data = Data(diameters=diameters, prices=prices)
print(data)
chart = Chart(data)
mark = chart.mark_point()
enc = mark.encode(x='diameters:Q', y='prices:Q', )
enc.display()


# calculate mean squared error
def compute_y(x, m, b):
    y = (m * x) + b
    return y


def compute_all_y(list_of_x, m, b):
    list_of_y = []
    for x in list_of_x:
        y = compute_y(x, m, b)
        list_of_y.append(y)
    return list_of_y


def compute_mse(list_of_known, list_of_predictions):
    list_of_error = []
    total = 0
    count = 0
    for index in range(len(list_of_known)):
        error = list_of_known[index] - list_of_predictions[index]
        list_of_error.append(error)
    for error in list_of_error:
        error = error * error
        total += error
        count += 1
    mse = total / count
    return mse


# machine learning using MSE

trials = 1000
m = 0.5
b = 7
diameters = [6, 8, 10, 14, 18]
prices_actual = [7, 9, 13, 17.5, 18]
MSE_list = []
attempt = []

for i in range(trials):
    prices_predict = compute_all_y(diameters, m, b)
    MSE1 = compute_mse(prices_actual, prices_predict)
    m2 = m + 0.01
    prices_predict = compute_all_y(diameters, m2, b)
    MSE2 = compute_mse(prices_actual, prices_predict)
    if MSE2 > MSE1:
        m3 = m - 0.01
        prices_predict = compute_all_y(diameters, m3, b)
        MSE3 = compute_mse(prices_actual, prices_predict)
        if MSE3 < MSE1:
            m = m3
            MSE1 = MSE3
    else:
        m = m2
        MSE1 = MSE2
    b2 = b + 0.01
    prices_predict = compute_all_y(diameters, m, b2)
    MSE4 = compute_mse(prices_actual, prices_predict)
    if MSE4 > MSE1:
        b3 = b - 0.01
        prices_predict = compute_all_y(diameters, m, b3)
        MSE5 = compute_mse(prices_actual, prices_predict)
        if MSE5 < MSE1:
            b = b3
            MSE1 = MSE5
    else:
        b = b2
        MSE1 = MSE4
    MSE_list.append(MSE1)
    attempt.append(i)
print(m, b)

data = Data(attempt=attempt, MSE_list=MSE_list)
chart = Chart(data)
mark = chart.mark_point()
enc = mark.encode(x='attempt:Q', y='MSE_list:Q', )
enc.display()

# ------
# 
# A simple moving average (SMA) calculates the average of a selected range
# of values by the number of values in that range
#
#       A1 + A2 + ... + An
# SMA = ------------------
#               n
#
# where:
# An = the value at period n
# n = the number of total values
#
# NOTE: Reason for not using numpy
# numpy is great for large collections, however it is slower than a list
# when using it for smaller collections
#
#               Python List         Numpy Array
# 10            7.796e-08 ms        2.939e-07 ms
# 100           1.630e-07 ms        3.280e-07 ms
# 1000          2.226e-07 ms        1.040e-06 ms
# 10000         2.161e-06 ms        3.566e-07 ms
# 100000        2.505e-05 ms        5.409e-07 ms
#
# ------

def calculate(values: list) -> float:
    if type(values) is not list:
        raise ValueError("'values' argument has to be of type '{0}'", list)

    if len(values) < 1:
        raise ValueError("The length of the 'values' argument needs to be more than 0.")

    dividor = len(values)
    sum = 0

    for i in values:
        sum += i

    result = sum / dividor

    return float(result)

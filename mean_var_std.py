import numpy as np


def calculate(list):
    try:
        if len(list) != 9:
            calculations = "List must contain nine numbers."
            raise ValueError(calculations)
        arr = np.array([[list[0], list[1], list[2]], [list[3], list[4], list[5]], [list[6], list[7], list[8]]])

        mean = getMean(arr)
        vari = getVariance(arr)
        stdv = getStandard(arr)
        maxi = getMax(arr)
        min = getMin(arr)
        sum = getSum(arr)

        calculations = {"mean": mean, "variance": vari, "standard deviation": stdv, "max": maxi, "min": min, "sum": sum}
    except ValueError:
        raise

    return calculations


def getSum(arr):
    sum0 = np.sum(arr, axis=0)
    sum1 = np.sum(arr, axis=1)
    sumf = np.sum(arr)
    sum0 = sum0.tolist()
    sum1 = sum1.tolist()
    sumf = sumf.tolist()
    sum_list = [sum0, sum1, sumf]
    return sum_list


def getMin(arr):
    min0 = np.amin(arr, axis=0)
    min1 = np.amin(arr, axis=1)
    minf = np.amin(arr)
    min0 = min0.tolist()
    min1 = min1.tolist()
    minf = minf.tolist()
    min_list = [min0, min1, minf]
    return min_list


def getMax(arr):
    max0 = np.amax(arr, axis=0)
    max1 = np.amax(arr, axis=1)
    maxf = np.amax(arr)
    max0 = max0.tolist()
    max1 = max1.tolist()
    maxf = maxf.tolist()
    max_list = [max0, max1, maxf]
    return max_list


def getStandard(arr):
    std0 = np.std(arr, axis=0)
    std1 = np.std(arr, axis=1)
    stdf = np.std(arr)
    std0 = std0.tolist()
    std1 = std1.tolist()
    stdf = stdf.tolist()
    std_list = [std0, std1, stdf]
    return std_list


def getMean(arr):
    me0 = np.mean(arr, axis=0)
    me1 = np.mean(arr, axis=1)
    mef = np.mean(arr)
    me0 = me0.tolist()
    me1 = me1.tolist()
    mef = mef.tolist()
    mean_list = [me0, me1, mef]
    return mean_list


def getVariance(arr):
    var0 = np.var(arr, axis=0)
    var1 = np.var(arr, axis=1)
    varf = np.var(arr)
    var0 = var0.tolist()
    var1 = var1.tolist()
    varf = varf.tolist()
    var_list = [var0, var1, varf]
    return var_list

import numpy as np

def calculate(lista):

    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")

    elArray = np.array([lista])

    elArray3 = elArray.reshape(3,3)

    diccResultados = {"mean": [], "variance": [], "standard deviation": [], "max": [], "min": [], "sum": []}

    meanFlat = np.mean(elArray)
    varFlat = np.var(elArray)
    stdFlat = np.std(elArray)
    maxFlat = np.max(elArray)
    minFlat = np.min(elArray)
    sumFlat = np.sum(elArray)

    meanRow1 = []
    varRow1 = []
    stdRow1 = []
    maxRow1= []
    minRow1 = []
    sumRow1 = []

    meanRow2 = []
    varRow2 = []
    stdRow2 = []
    maxRow2= []
    minRow2 = []
    sumRow2 = []

    for i in range(3):  # Row1

        meanRow1.append(np.mean(elArray3[:,i]))
        varRow1.append(np.var(elArray3[:,i]))
        stdRow1.append(np.std(elArray3[:,i]))
        maxRow1.append(np.max(elArray3[:,i]))
        minRow1.append(np.min(elArray3[:,i]))
        sumRow1.append(np.sum(elArray3[:,i]))

    for i in range(3):  # Row2

        meanRow2.append(np.mean(elArray3[i:i+1]))
        varRow2.append(np.var(elArray3[i:i+1]))
        stdRow2.append(np.std(elArray3[i:i+1]))
        maxRow2.append(np.max(elArray3[i:i+1]))
        minRow2.append(np.min(elArray3[i:i+1]))
        sumRow2.append(np.sum(elArray3[i:i+1]))

    mean = []
    variance = []
    std = []
    max = []
    min = []
    sum = []

    mean.append(meanRow1)
    mean.append(meanRow2)
    mean.append(meanFlat)

    variance.append(varRow1)
    variance.append(varRow2)
    variance.append(varFlat)

    std.append(stdRow1)
    std.append(stdRow2)
    std.append(stdFlat)

    max.append(maxRow1)
    max.append(maxRow2)
    max.append(maxFlat)

    min.append(minRow1)
    min.append(minRow2)
    min.append(minFlat)

    sum.append(sumRow1)
    sum.append(sumRow2)
    sum.append(sumFlat)

    diccResultados["mean"] = mean
    diccResultados["variance"] = variance
    diccResultados["standard deviation"] = std
    diccResultados["max"] = max
    diccResultados["min"] = min
    diccResultados["sum"] = sum

    return diccResultados
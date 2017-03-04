from Algorithm import hClustering


class Main:
    l1 = [4, 7]
    l2 = [0, 19]
    l3 = [24, 37]
    l4 = [33, 7]
    l5 = [4, 4]
    l6 = [26, 18]
    l7 = [23, 3]
    l8 = [3, 3]
    l9 = [7, 17]
    l10 = [3, 40]
    l11 = [31, 19]

    listOfPoints = []
    listOfPoints.append(l1)
    listOfPoints.append(l2)
    listOfPoints.append(l3)
    listOfPoints.append(l4)
    listOfPoints.append(l5)
    listOfPoints.append(l6)
    listOfPoints.append(l7)
    listOfPoints.append(l8)
    listOfPoints.append(l9)
    listOfPoints.append(l10)
    listOfPoints.append(l11)

    print hClustering(listOfPoints)

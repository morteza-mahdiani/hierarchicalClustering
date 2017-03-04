import math
import sys


def hClustering(listOfPoints):
    # list of clustre for computations
    listOfClusters = []
    # assign each point to one cluster
    for e in listOfPoints:
        cls  = cluster([e], None, None)
        # computing center of cluster
        # print cls.listOfNodes
        cls.center = cls.computeCenter(cls.listOfNodes)
        listOfClusters.append(cls)

    while len(listOfClusters) > 1:
        tempDistance = sys.maxint
        tempe1 = cluster([[0,0]], None, None)
        tempe2 = cluster([[0,0,]], None, None)
        for e1 in listOfClusters:
            for e2 in listOfClusters:
                if not (e2 == e1):
                    if tempDistance > clusterDistance(e1, e2):
                        tempDistance = clusterDistance(e1, e2)
                        tempe1 = e1
                        tempe2 = e2
        for e in listOfClusters:
            if e == tempe1 or e == tempe2:
                listOfClusters.remove(e)
        listOfClusters.append(mergTwoCluster(tempe1, tempe2))

        if len(listOfPoints) == len(listOfClusters[0].listOfNodes):
            listOfClusters.pop(1)

        print listOfClusters[0].listOfNodes

    return listOfClusters[0]


def mergTwoCluster(cluster1, cluster2):
    list1 = list(cluster1.listOfNodes)
    list2 = list(cluster2.listOfNodes)
    newList = list(list1)
    for e in list2:
        if e not in newList:
            newList.append(e)

    cls = cluster(newList, cluster1, cluster2)
    cls.center = cls.computeCenter(cls.listOfNodes)
    # print cls.listOfNodes

    return cls

def clusterDistance(cluster1, cluster2):
    tempi = cluster1.center[0] - cluster2.center[0]
    tempj = cluster1.center[1] - cluster1.center[1]

    return math.sqrt(math.fabs(math.pow(tempi, 2) + math.pow(tempj, 2)))

class cluster:
    center = [0,0]
    def __init__(self, listOfNodes, child1Cluster, child2Cluster):
        self.listOfNodes = listOfNodes
        self.child1Cluster = child1Cluster
        self.child2Cluster = child2Cluster

    def computeCenter(self, listOfNodes):
        tempi = 0
        tempj = 0
        for e in listOfNodes:
            tempi += e[0]
            tempj += e[1]
        tempi = tempi / len(listOfNodes)
        tempj = tempj / len(listOfNodes)

        return [tempi, tempj]

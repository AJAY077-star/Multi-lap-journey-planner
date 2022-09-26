from graph import Graph
import networkx
import itertools


class PathFinder:
    graph = networkx.DiGraph()
    scheduleDetailLookup = {}
    # g = None

    def __init__(self, totalVertices, scheduleData):
        self.totalVertices = totalVertices
        self._intialize(scheduleData)

    def _intialize(self, trainSchedules):

        self.graph.add_node(self.totalVertices)

        # self.g = Graph(self.totalVertices, directed=True)
        self.scheduleDetailLookup = {}
        edgeList = []

        for schedule in trainSchedules:
            src = schedule[0]
            dest = schedule[1]
            duration = schedule[2]
            distance = schedule[3]
            trainNumber = schedule[4]
            srcDistance = schedule[5]
            destDistance = schedule[6]
            srcArrivalTime = schedule[7]
            srcDepartureTime = schedule[8]
            destArrivalTime = schedule[9]
            destDepartureTime = schedule[10]
            edge = (src, dest)
            edgeList.append(edge)
            # self.g.add_edge(src, dest)
            self.scheduleDetailLookup[edge] = {
                "duration": duration, "distance": distance, "trainNumber": trainNumber, "srcDistance": srcDistance, "destDistance": destDistance, "srcArrivalTime": srcArrivalTime, "srcDepartureTime": srcDepartureTime, "destArrivalTime": destArrivalTime, "destDepartureTime": destDepartureTime}
        # print(self.scheduleDetailLookup)
        self.graph.add_edges_from(edgeList)

    def simple_paths(self, source, target):
        edge_list = []
        value = networkx.all_simple_paths(
            self.graph, source, target)
        # self.graph.add_nodes_from(edge_list)
        # path = self.g.bfs(source, target)
        # print(value)
        return value

    def find_path(self, source, target):
        routePathList = []
        simplePathList = self.simple_paths(source, target)
        first3 = itertools.islice(simplePathList, 3)
        # print(list(top5))
       # print([next(top5) for _ in range(10)])
        # l = []
        # for i in first5:
        #     print("i", i)
        #     l.append(i)

        # print(l)
        count = 0
        for path in first3:
            print(path)
            cumulativeDuration = 0
            cumulativeDistance = 0
            count = count + 1
            print("path ", count)

            i = 0
            for index, d in enumerate(path):
                i = i + 1

                if((index + 1) < len(path)):
                    edge = (path[index], path[index + 1])
                    print("dest src distance = ",
                          self.scheduleDetailLookup[edge]["destDistance"], self.scheduleDetailLookup[edge]["srcDistance"])
                    trainNumber = self.scheduleDetailLookup[edge]["trainNumber"]
                    print(self.scheduleDetailLookup[edge])
                    cumulativeDuration += abs(self.scheduleDetailLookup[edge]["destArrivalTime"] -
                                              self.scheduleDetailLookup[edge]["srcDepartureTime"])
                    cumulativeDistance += abs(self.scheduleDetailLookup[edge]["destDistance"] -
                                              self.scheduleDetailLookup[edge]["srcDistance"])
            routePathList.append(
                (path, cumulativeDuration, cumulativeDistance, trainNumber))
            print(routePathList)
        return routePathList


# totalNodes = 4
# trainSchedules = [
#     (0, 1, 20, 3),
#     (0, 2, 30, 3),
#     (0, 3, 5, 2),
#     (2, 0, 6, 2),
#     (2, 1, 8, 2),
#     (1, 3, 3, 4)
# ]

# finder = PathFinder(totalNodes, trainSchedules)
# routePathList = finder.find_path(0, 3)
# print(str(routePathList))

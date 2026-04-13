class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(listOfGraphs, a):
            for graph in listOfGraphs:
                if a in graph:
                    return graph
            return []
        
        def addToGraph(listOfGraphs, target, val):
            for graph in listOfGraphs:
                if target in graph:
                    graph.append(val)
                    return
            return
        
        def joinGraph(listOfGraphs, a, b):
            newGraph = a + b
            listOfGraphs.remove(a)
            listOfGraphs.remove(b)
            listOfGraphs.append(newGraph)

        connectedDots = []
        duplicate = []
        for edge in edges:
            a, b = edge[0], edge[1]
            graphA = find(connectedDots, a)
            graphB = find(connectedDots, b)
            if len(graphA) != 0 and graphA is graphB:
                duplicate.append(edge)
                continue
            if len(graphA) == 0 and len(graphB) == 0:
                connectedDots.append([a, b])
                continue
            if len(graphA) == 0:
                addToGraph(connectedDots, b, a)
                continue
            if len(graphB) == 0:
                addToGraph(connectedDots, a, b)
                continue
            joinGraph(connectedDots, graphA, graphB)

        return duplicate[-1]

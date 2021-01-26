#{"A":{"B":5,"C":3}, "B":{"A":5,"D":2}, "C":{"A":3}, "D":{"B":2}}
class WeightedGraph:
    def __init__(self):
        self.verticies = {}
        self.maxWeight = 0

    def new_vertex(self, vertexID):
        #Each vertex is an item in a dictionary, with the key being the vertexID
        #And the value being a disctionary conatining the neighbors and weights.
        self.verticies[vertexID] = {}
 
    def connect_verticies(self, vertexA, vertexB, weight):
        #this method will make the weight the same in both directions.
        #make it do otherwise by removing the second line.
        if weight > self.maxWeight:
            self.maxWeight = weight
        self.verticies[vertexA][vertexB] = weight
        self.verticies[vertexB][vertexA] = weight

    def display_graph(self):
        #This is where I could put a fancier method to display the graph but I can't be bothered
        print(self.verticies)

    def path_cost(self,path):
        #assumes it is a valid path
        totalCost = 0
        for i in range(len(path)-1):
            totalCost += self.verticies[path[i]][path[i+1]]
        return(totalCost)

    def dijkstra(self, start, end):
        nodePaths = {start: {"path":[start],"cost":0}}
        currentVertex = start
        for vertex in self.verticies:
            #set weights to effectively infinity
            if vertex != start:
                nodePaths[vertex] = {"path":[start], "cost":len(self.verticies)*self.maxWeight+1}
        while currentVertex != end:
            for neighbour in self.verticies[currentVertex]:
                if neighbour in nodePaths:
                    #if the cost to the current vertex + the cost from the current vertex to the neighbour
                    #is greater than the current known cost to that neighbour
                    if nodePaths[currentVertex]["cost"] + self.verticies[currentVertex][neighbour] < nodePaths[neighbour]["cost"]:
                        #set new paths
                        nodePaths[neighbour]["path"] = nodePaths[currentVertex]["path"] + [neighbour]
                        #recalculate path cost
                        nodePaths[neighbour]["cost"] = self.path_cost(nodePaths[neighbour]["path"])
            del nodePaths[currentVertex]
            #get the node with the lowest cost
            currentVertex = min(nodePaths, key = lambda x : nodePaths[x]["cost"]) 
        return(nodePaths[end]["path"])

if __name__ == "__main__":
    graph = WeightedGraph()
    graph.new_vertex("A")
    graph.new_vertex("B")
    graph.new_vertex("C")
    graph.new_vertex("D")
    graph.new_vertex("E")
    graph.new_vertex("F")
    graph.new_vertex("G")
    graph.new_vertex("H")
    graph.connect_verticies("A","B",5)
    graph.connect_verticies("E","F",1)
    graph.connect_verticies("D","F",6)
    graph.connect_verticies("G","F",2)
    graph.connect_verticies("C","G",9)
    graph.connect_verticies("D","E",4)
    graph.connect_verticies("C","A",3)
    graph.connect_verticies("D","B",2)
    graph.connect_verticies("B","H",1)
    graph.connect_verticies("H","E",1)
    #graph.display_graph()
    print(graph.dijkstra("A","F"))

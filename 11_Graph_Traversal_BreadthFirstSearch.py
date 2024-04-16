class Node():
    def __init__(self ,  value):
        self.value = value
        self.adjacentList = []
        self.visited = False
class Graph():
    def BFS(self , start):
        queue = []
        queue.append(start)
        start.visited = True
        
        traversal = []
        
        while queue:
            actualNode = queue.pop(0)
            traversal.append(actualNode.value)
            
            for element in actualNode.adjacentList:
                if element.visited is False:
                    queue.append(element)
                    element.visited = True
        return traversal
    
node1 = Node('A') 
node2 = Node('B') 
node3 = Node('C') 
node4 = Node('D') 
node5 = Node('E') 
node6 = Node('F') 
node7 = Node('G') 

node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node1.adjacentList.append(node4)
node2.adjacentList.append(node5)
node2.adjacentList.append(node6)
node4.adjacentList.append(node7)

graph = Graph()
print("Breadth First Search For Graph: ",graph.BFS(node1))
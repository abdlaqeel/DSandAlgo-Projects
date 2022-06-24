from graph import Graph
from linked_tree import LinkedTree
class myGraph(Graph):

  def findPath(self,v,z):
    """ Q1: Complete this method, which finds a path from vertices v to z in a graph (either undirected or directed).
        Return True if there is a path between v and z, else return False
        Note: you can refer to the algorithm in lecture note 10.3 DFS, slide 14, using labels ("UNEXPLORED", "DISCOVERY", and "BACK" etc.) to facilitate your coding; however, there is no need to return the list of vertices or edges along the path as indicated in the lecture note, instead just return True or False. You're also allowed to implement the method without any facilitator labels.
        
        Your code goes here:
    """ #adapted from slides
    v.setLabel("VISITED")
    if v == z:
      return True #Sets true if visited
    else:
      for e in self.incident_edges(v):
        if e.getLabel() == "UNEXPLORED":
          w= e.opposite(v)
          if w.getLabel()== "UNEXPLORED":
            e.setLabel("DISCOVERY")
            return self.findPath(w, z)
      return False
    
    
  def spanning_Forest_DFS(self):
    """Q3: Complete this method to perform DFS for the entire graph and return its spanning forest and discovered edges in a dictionary. The format of the returned dictionary is samilar to that of question 2, except the cells originally filled with None (root vetices) in Q2 now store spanning tree objects. Such that the content of the example in Part III looks like [<linked_tree.LinkedTree object at 0x10306abe0> (A,B,5) (B,C,6) (C,E,5) (D,E,3) <linked_tree.LinkedTree object at 0x10315e460> (F,G,25) (G,H,30)]. The nodes in the spanning trees only store the elements of vertices. We use the linkedTree class from linked_tree.py for the spanning trees.
    
        Note: Finishing Q2 before this question may be helpful.
            You can modify methods DFS and _DFS from graph.py for this quesiton.
    """
    forest = {} #forms a dictionary names forest
    for x in g.vertices():
      if x not in forest: #checks if x is in forest or not
        forest[x] = None  #forms the root
        self._DFS(x, forest)#runs DFS
    for r in forest:
      if forest[r] == None:
        forest[r] = LinkedTree()
        tree=forest[r]
        previus = tree._add_root(r) #adds a root to the tree
      else:
        previus = tree._add_to_right(previus,r)
      return forest #returns the forest formed
    


  #facilitator methods to be used in testing code
  def reset(self):
    """reset all vertices and edges to UNEXPLORED
    """
    for v in self.vertices():
      v.setLabel("UNEXPLORED")
    for e in self.edges():
      e.setLabel("UNEXPLORED")

  def getVertexByValue(self, e):
    """
        Return the vertex that has element of value e.
    """
    # go through and check each of the vertices and check value
    findVertex = None
    for v in self.vertices():
      if v.element() == e:
        findVertex = v
    return findVertex

#-- Main method, for testing
if __name__ == '__main__':
  def testFun_Traversal(g, Directed = False):
    # Print all edges
    print("Edges:", g.edge_count())
    for e in g.edges():
      print(e, end = " ")
    print()

    # Print all vertices
    print("Vertices:", g.vertex_count())
    for v in g.vertices():
      print(v, end = ", ")
    print()

    g.reset() # reset the vertices and edges
    # Call DFS on g, to get the discovery edges
    discovery = g.DFS()
    print("DFS discovery edges:")
    for e in discovery:
      print(discovery[e], end = " ")
    print()

    g.reset() # reset the vertices and edges
    # Call BFS on g, to get the discovery edges
    discovery = g.BFS()
    print("BFS discovery edges:")
    for e in discovery:
      print(discovery[e], end = " ")
    print()
        
    
  """Test Part I, testing with an undirected graph
  """
  v_elements = ["A","B","C","D","E"]
  g = myGraph()
  for v in v_elements:
    g.insert_vertex(v)
  
  g.insert_edge(g.getVertexByValue("A"),g.getVertexByValue("B"),5)
  g.insert_edge(g.getVertexByValue("A"),g.getVertexByValue("C"),4)
  g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("C"),6)
  g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("D"),1)
  g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("E"),10)
  g.insert_edge(g.getVertexByValue("C"),g.getVertexByValue("E"),5)
  g.insert_edge(g.getVertexByValue("D"),g.getVertexByValue("E"),3)
  
  print("Test Part I")
  print("This is an undirected graph:")
  testFun_Traversal(g)
  
  g.reset() # reset the vertices and edges before another traversal
  """Testing for Q1, the output should be:
     Is it a path?  True
  """
  print("Is it a path? ",g.findPath(g.getVertexByValue("A"),g.getVertexByValue("E")))

  """Test Part II, testing with a directed graph
  """
  v_elements = ["A","B","C","D","E"]
  g = myGraph(True)
  for v in v_elements:
    g.insert_vertex(v)
  #adding edges between vertices, note the edge direction is from the first vertex to the second one
  g.insert_edge(g.getVertexByValue("A"),g.getVertexByValue("B"),5)
  g.insert_edge(g.getVertexByValue("A"),g.getVertexByValue("C"),4)
  g.insert_edge(g.getVertexByValue("C"),g.getVertexByValue("B"),6)
  g.insert_edge(g.getVertexByValue("D"),g.getVertexByValue("B"),1)
  g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("E"),10)
  g.insert_edge(g.getVertexByValue("E"),g.getVertexByValue("C"),5)
  g.insert_edge(g.getVertexByValue("E"),g.getVertexByValue("D"),3)
  
  print("Test Part II")
  print("This is a directed graph:")
  testFun_Traversal(g)

  """Testing for Q1, the output should be:
     Is it a path? True
  """
  g.reset() # reset the vertices and edges
  print("Is it a path?",g.findPath(g.getVertexByValue("A"),g.getVertexByValue("E")))
  
  
  """Test Part III, testing with a graph with multiple connected components
  """
  v_elements = ["A","B","C","D","E","F","G","H"]
  g = myGraph()
  for v in v_elements:
    g.insert_vertex(v)
  #adding edges between vertices
  g.insert_edge(g.getVertexByValue("A"),g.getVertexByValue("B"), 5)
  g.insert_edge(g.getVertexByValue("A"),g.getVertexByValue("C"), 4)
  g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("C"), 6)
  g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("D"), 1)
  g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("E"), 10)
  g.insert_edge(g.getVertexByValue("C"),g.getVertexByValue("E"), 5)
  g.insert_edge(g.getVertexByValue("D"),g.getVertexByValue("E"), 3)
  # a second connected component  
  g.insert_edge(g.getVertexByValue("F"),g.getVertexByValue("G"), 25)
  g.insert_edge(g.getVertexByValue("F"),g.getVertexByValue("H"), 26)
  g.insert_edge(g.getVertexByValue("G"),g.getVertexByValue("H"), 30)
  print("Test Part III")
  print("This is a multiple components graph:")
  testFun_Traversal(g)
  """Q2: Please draw a spanning forest from the result of discovery = g.DFS() in the method testFun_Traversal(g). In this case, the returned discovery =
[None (A,B,5) (B,C,6) (C,E,5) (D,E,3) None (F,G,25) (G,H,30)], which is a dictionary that contains the edges of
DFS trees. None is where the root is, please see corresponding code in graph.py. You can draw the forest in a separate word document.
  
  """

  """Testing for Q1, resulting output should be:
  is it a path? False
  """
  g.reset() # reset the vertices and edges
  print("Is it a path?",g.findPath(g.getVertexByValue("A"),g.getVertexByValue("F")))
  
  """Testing for Q3
    Spanning Forest DFS discovery edges:
    <linked_tree_sln.LinkedTree object at 0x102efcbe0> (A,B,5) (B,C,6) (C,E,5) (D,E,3) <linked_tree_sln.LinkedTree object at 0x102ff1430> (F,G,25) (G,H,30)
    Spanning trees:
    A{B{C{E{D}}}}
    F{G{H}}
  """
  """ uncomment the following testing code when you finish Q3
  g.reset() # reset the vertices and edges
  discovery = g.spanning_Forest_DFS()
  print("Spanning Forest DFS discovery edges:")
  for e in discovery:
    print(discovery[e], end = " ")
  print()
  #Here we print each of spanning trees
  print("Spanning trees:")
  for e in discovery:
    if isinstance(discovery[e],LinkedTree):
      discovery[e].print()
  """

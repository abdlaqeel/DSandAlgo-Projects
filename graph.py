# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class Graph:
  """Representation of a simple graph using an adjacency map."""

  #------------------------- nested Vertex class -------------------------
  class Vertex:
    """Lightweight vertex structure for a graph.
       Vertices can have the following labels (optional):
        UNEXPLORED
        VISITED
    """
    __slots__ = '_element', '_label'
  
    def __init__(self, x, label="UNEXPLORED"):
      """Do not call constructor directly. Use Graph's insert_vertex(x)."""
      self._element = x
      self._label = label
  
    def element(self):
      """Return element associated with this vertex."""
      return self._element
      
    def getLabel(self):
      """ Get label assigned to this vertex. """
      return self._label

    def setLabel(self, label):
      """ Set label after the vertex has been created. """
      self._label = label
  
    def __hash__(self):         # will allow vertex to be a map/set key
      return hash(id(self))

    def __str__(self):
      return self._element
    
  #------------------------- nested Edge class -------------------------
  class Edge:
    """Lightweight edge structure for a graph.
       Edges can have the following labels (optional):
        UNEXPLORED
        DISCOVERY
        BACK
    """
    __slots__ = '_origin', '_destination', '_element', '_label'
  
    def __init__(self, u, v, x = None,label = "UNEXPLORED"):
      """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
      self._origin = u
      self._destination = v
      self._element = x
      self._label = label

    def getLabel(self):
      """ Get label assigned to this vertex. """
      return self._label

    def setLabel(self, label):
      """ Set label after the vertex has been created. """
      self._label = label

    def endpoints(self):
      """Return (u,v) tuple for vertices u and v."""
      return (self._origin, self._destination)
  
    def opposite(self, v):
      """Return the vertex that is opposite v on this edge."""
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      return self._destination if v is self._origin else self._origin
      raise ValueError('v not incident to edge')
  
    def element(self):
      """Return element associated with this edge."""
      return self._element
  
    def __hash__(self):         # will allow edge to be a map/set key
      return hash( (self._origin, self._destination) )

    def __str__(self):
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)
    
  #------------------------- Graph methods -------------------------
  def __init__(self, directed=False):
    """Create an empty graph (undirected, by default).

    Graph is directed if optional paramter is set to True.
    """
    self._outgoing = {}
    # only create second map for directed graph; use alias for undirected
    self._incoming = {} if directed else self._outgoing

  def _validate_vertex(self, v):
    """Verify that v is a Vertex of this graph."""
    if not isinstance(v, self.Vertex):
      raise TypeError('Vertex expected')
    if v not in self._outgoing:
      raise ValueError('Vertex does not belong to this graph.')
    
  def is_directed(self):
    """Return True if this is a directed graph; False if undirected.

    Property is based on the original declaration of the graph, not its contents.
    """
    return self._incoming is not self._outgoing # directed if maps are distinct

  def vertex_count(self):
    """Return the number of vertices in the graph."""
    return len(self._outgoing)

  def vertices(self):
    """Return an iteration of all vertices of the graph."""
    return self._outgoing.keys()

  def edge_count(self):
    """Return the number of edges in the graph."""
    total = sum(len(self._outgoing[v]) for v in self._outgoing)
    # for undirected graphs, make sure not to double-count edges
    return total if self.is_directed() else total // 2

  def edges(self):
    """Return a set of all edges of the graph."""
    result = set()       # avoid double-reporting edges of undirected graph
    for secondary_map in self._outgoing.values():
      result.update(secondary_map.values())    # add edges to resulting set
    return result

  def get_edge(self, u, v):
    """Return the edge from u to v, or None if not adjacent."""
    self._validate_vertex(u)
    self._validate_vertex(v)
    return self._outgoing[u].get(v)        # returns None if v not adjacent

  def degree(self, v, outgoing=True):   
    """Return number of (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to count incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    return len(adj[v])

  def incident_edges(self, v, outgoing=True):   
    """Return all (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to request incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    for edge in adj[v].values():
      yield edge

  def insert_vertex(self, x=None):
    """Insert and return a new Vertex with element x."""
    v = self.Vertex(x)
    self._outgoing[v] = {}
    if self.is_directed():
      self._incoming[v] = {}        # need distinct map for incoming edges
    return v
      
  def insert_edge(self, u, v, x=None):
    """Insert and return a new Edge from u to v with auxiliary element x.

    Raise a ValueError if u and v are not vertices of the graph.
    Raise a ValueError if u and v are already adjacent.
    """
    if self.get_edge(u, v) is not None:      # includes error checking
      raise ValueError('u and v are already adjacent')
    e = self.Edge(u, v, x)
    self._outgoing[u][v] = e
    self._incoming[v][u] = e

  def _DFS(self,u, discovered):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in self.incident_edges(u):    # for every outgoing edge from u
      v = e.opposite(u)
      if v not in discovered:        # v is an unvisited vertex
        discovered[v] = e            # e is the tree edge that discovered v
        self._DFS(v, discovered)        # recursively explore from v
  def DFS(self):
    """Perform DFS for entire graph and return forest as a dictionary.

    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest = {}
    for u in self.vertices():
      if u not in forest:
        forest[u] = None             # u will be the root of a tree
        self._DFS(u, forest)
    return forest
    
  def _BFS(self, s, discovered):
    """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s]                        # first level includes only s
    while len(level) > 0:
      next_level = []                  # prepare to gather newly found vertices
      for u in level:
        for e in self.incident_edges(u):  # for every outgoing edge from u
          v = e.opposite(u)
          if v not in discovered:      # v is an unvisited vertex
            discovered[v] = e          # e is the tree edge that discovered v
            next_level.append(v)       # v will be further considered in next pass
      level = next_level               # relabel 'next' level to become current

  def BFS(self):
    """Perform BFS for entire graph and return forest as a dictionary.

    Result maps each vertex v to the edge that was used to discover it.
    (vertices that are roots of a BFS tree are mapped to None).
    """
    forest = {}
    for u in self.vertices():
      if u not in forest:
        forest[u] = None            # u will be a root of a tree
        self._BFS(u, forest)
    return forest
    
    
if __name__ == '__main__': #test
  g = Graph()
  A = g.insert_vertex("A")
  B = g.insert_vertex("B")
  C = g.insert_vertex("C")
  D = g.insert_vertex("D")
  g.insert_edge(A,B,"Eab")
  g.insert_edge(A,C,"Eac")
  g.insert_edge(A,D,"Ead")
  g.insert_edge(B,C,"Ebc")
  g.insert_edge(B,D,"Ebd")
  g.insert_edge(C,D,"Ecd")
  print(g.degree(A))
  


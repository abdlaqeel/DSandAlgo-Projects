from general_tree import Tree

class LinkedTree(Tree):
  """Linked representation of a tree structure."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a node."""
    __slots__ = '_element', '_parent', '_children' # streamline memory usage

    def __init__(self, element, parent=None):
      self._element = element
      self._parent = parent
      self._children = []   #Children list, store pointers pointing to children subtrees, respectively
      
    def element(self):
      return self._element
  

  #-------------------------- linked tree constructor --------------------------
  def __init__(self):
    """Create an initially empty tree."""
    self._root = None
    self._size = 0

  #-------------------------- implemented methods --------------------------
  def __len__(self):
    """Return the total number of elements in the tree."""
    return self._size
  
  def root(self):
    """Return the root node of the tree (or None if tree is empty)."""
    return self._root

  def parent(self, p):
    """Return the node of p's parent (or None if p is root)."""
    return p._parent

  def children(self, p):
    """Return the node iterator of p's children."""
    for nd in p._children:
      yield nd
  
  def num_children(self, p):
    """Return the number of children of node p."""
    return len(p._children)  #simply retrun the size of children list.
      

  def is_leaf(self, p):
    """Return True if Position p does not have any children."""
    return self.num_children(p) == 0
    
  def _add_root(self, e):
    """Place element e at the root of an empty tree and return new node.

    Raise ValueError if tree nonempty.
    """
    if self._root is not None:
      raise ValueError('Root exists')
    self._size = 1
    self._root = self._Node(e)
    return self._root

  def _add_to_left(self, p, e):
    """Create a new child with element e, and add to the left side children of node p.

    Return the new node.
    """
    self._size += 1
    p._children.insert(0,self._Node(e, p))        # add node at the front of the children list
    return p._children[0]

  def _add_to_right(self, p, e):
    """Create a new child with element e, and add to the right side children of node p.

    Return the new node.
    """
    self._size += 1
    p._children.append(self._Node(e, p))        # add node at the front of the children list
    return p._children[-1]
    
  def _add_by_index(self, p, e, idx):
    """Create a new child with element e, and add to the children of node p, indexed at idx.

    Return the new node.
    """
    self._size += 1
    p._children.insert(idx, self._Node(e, p))        # add node at the idx node in the children list
    return p._children[idx]
    
  def _attach_children(self,p,s):
    """attach childre from s to p till '}'"""
    p1 = self._add_to_right(p, s.pop(0))
    while s[0] != '}':
      if s[0] == '{':
        s.pop(0)  #pop out '{'
        self._attach_children(p1,s)
      else:
        p1 = self._add_to_right(p, s.pop(0))
    s.pop(0) #pop '}'
                    
  def create(self,s):
    """Create a tree from a sequence, e.g. s =['B','{','A','D','{','C','E','}','F','}']"""
    self._add_root(s.pop(0))
    s.pop(0) #pop out '{'
    self._attach_children(self._root,s) #pass in ['A','D','{','C','E','}','F','}']
      
  def print(self):
    """print the tree in preoder with {} to separate children"""
    self._print_subtree_preorder(self.root())
    print()
    

  #--------------------------  Methods for you to implement (Questions) --------------------------
    
  def _count_nodes(self,p):
    """Q1: Count the number of node in the subtree rooted by p.
    Note: suggest to use recursion.

    Your code goes below    
    """
    cnt = 1
    for child in self.children(p):
      cnt += self._count_nodes(child)
    return cnt
        
  def _delete_subtree(self, p):
    """Q2: delete a whole subtree whose root is the node p; return the element of p
    Note: don’t forget to reduce the size of the tree by the number of nodes of the subtree.

    Your code goes below    
    """
    if self.is_root(p):
      self._root = None
      self._size = 0
      return p.element()
    parent_p = self.parent(p)
    parent_p._children.remove(p)
    self._size -= self._count_nodes(p)  #should derease the number of the trees
    p._parent = p           # convention for deprecated node p
    
  
  def _print_subtree_preorder(self, p):
    """Q3: The recursive method that actually print the subtree rooted by p in preoder using {} to separate children.
        The suggested things to do in this method could be below, but you feel free to implement using your own way.        
        1 print the node p element
        2 if p has children/child, print a '{' first then print children (recursion), and then print '}'
        
    Your code goes below
    """
    print(p.element(), end='')                  # visit p before its subtrees
    if self.num_children(p)>0:
      print('{', end='')
      for c in self.children(p):                        # for each child c
        self._print_subtree_preorder(c)
      print('}', end='')

  def _height(self, p):                  
    """Q4:Return the height of the subtree rooted at node p.
        Your code goes below
    """
    if self.is_leaf(p):
      return 0
    else:
      return 1 + max(self._height(c) for c in self.children(p))
     
      
    
if __name__ == '__main__':
  lgt = LinkedTree()
  s = ['B','{','A','D','{','C','E','}','F','}']
  #s = ['A','{','B','{','E','F','G','}','C','D','{','H','I','}','}']
  lgt.create(s)
  itrs = lgt.breadthfirst()
  for it in itrs:
    print(it.element(),end='')
  print()
  pre_order_iter = lgt.preorder()
  for it in pre_order_iter:
    print(it.element(), end='')
  print()
  lgt.print()

  lgt = LinkedTree()
  Root = lgt._add_root('B')
  lgt._add_to_left(Root,'A')
  p = lgt._add_to_right(Root,'D')
  lgt._add_to_left(p,'C')
  lgt._add_to_right(p,'E')
  lgt._add_to_right(Root,'F')
  itrs = lgt.breadthfirst()
  for it in itrs:
    print(it.element(),end='')
  print()

  pre_order_iter = lgt.preorder()
  for it in pre_order_iter:
    print(it.element(), end='')
  print()
  
  print(lgt._height(p))
  print(lgt._count_nodes(p))


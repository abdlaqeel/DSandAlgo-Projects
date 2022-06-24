#!/usr/bin/python3

class AVL:
  """AVL based on 'BTNode's."""
  __slots__ = 'root'

  #-------------------------- nested BTNode class --------------------------
  class _BTNode:
    """ Lightweight, nonpublic class for storing a BTNode. 
    
    	Notice that the member variable balanceFactor is defined here 
    	for recording balance factor of each node
    """
    __slots__ = 'element', 'left', 'right','parent','balanceFactor'

    def __init__(self, element, left = None, right = None, parent = None):
      self.element = element
      self.left    = left
      self.right   = right
      self.parent  = parent
      """Notice that original self.height was changed to self.balanceFactor"""
      self.balanceFactor  = 0

    def hasLeft(self):
      """ Returns whether this node has a left child. """
      return self.left != None

    def hasRight(self):
      """ Returns whether this node has a right child. """
      return self.right != None
      
    def left_height(self):
      """ Q1: Returns the height of left subtree. If the left tree is None, return -1.
      	Note: there is no more field of height of the node
      	Your code goes bellow
      """
      if self.left is None: #if it does not have a left child
        return -1
      else:
        return self.left_height #computing left height


    def right_height(self):
      """ Q2: Returns the height of right subtree. If the right tree is None, return -1.
      	Note: there is no more field of height of the node
      	Your code goes bellow
      """
      if self.right is None: #if it does not have a right child
        return -1

      else:
        return self.right_height #computing right height
      
    def _height(self):                  
      """Return the height of the subtree rooted at the current node.       
      """
      if self.is_leaf():
        return 0
      else:
        return 1 + max(c._height() for c in self.children())

    def is_leaf(self):
      """Return True if current node does not have any children."""
      return self.left is None and self.right is None
      
    def children(self):
      """Generate an iteration of current node's children."""
      if self.left is not None:
        yield self.left
      if self.right is not None:
        yield self.right
      
    def __lt__(self, other):
      """ Return True if other is a BTNode and this node is less than other. """
      return type(other) is type(self) and self.element < other.element

    def __gt__(self, other):
      """ Return True if other is a BTNode and this node is greater than other. """
      return type(other) is type(self) and self.element > other.element

    def __eq__(self, other):
      """ Return True if other is a BTNode and this node is equal to the other. """
      return type(other) is type(self) and self.element == other.element

  #-- c'tor
  def __init__(self):
    self.root = None

  def insert(self, element):
    """ Insert element into the AVL, keeping the AVL property. """
    def _insertNode(root, node):
      if root == None or root == node:    # Overwrite if already present
        root = node
      else:
        if node < root:  # Go left
          if root.hasLeft():
            _insertNode(root.left, node)
          else:
            root.left = node
            node.parent = root
        else:            # Go right
          if root.hasRight():
            _insertNode(root.right, node)
          else:
            root.right = node
            node.parent = root

    # Create node to insert
    node = self._BTNode(element)

    if self.root == None:   # Special case for when tree is empty
      self.root = node
    else:
      _insertNode(self.root, node)
      self.recompute_balanceFactor(node) #recompute the balance factors from the node along its path to the root
      self._rebalance(node)
      
  def _subtree_last_position(self, p):
    """Return Position of last item in subtree rooted at p."""
    walk = p
    while walk.right is not None:                # keepwalking right
      walk = walk.right
    return walk

  def _replace(self, node, e):
    """Replace the element at node with e, and return old element."""
    old = node.element
    node.element = e
    return old
    
  def _delete(self, node):
    """Delete node. It is called by the method delete"""
    child = node.left if node.left else node.right  # might be None
    if child is not None:
      child.parent = node.parent   # child's grandparent becomes parent
    if node is self.root:
      self.root = child             # child becomes root
    else:
      parent = node.parent
      if node is parent.left:
        parent.left = child
      else:
        parent.right = child
    node.parent = node              # convention for deprecated node
    return node.element

  def delete(self, p):
    """Remove the item at given Node and keep in AVL"""
    if p is None:
      return None
    replacement = p
    if p.left and p.right:           # p has two children
      replacement = self._subtree_last_position(p.left)
      self._replace(p, replacement.element)
      p =  replacement
      # now p has at most one child
    parent = p.parent
    self._delete(p)
    #recompute the balance factors from the parent node along its path to the root
    self.recompute_balanceFactor(parent) 
    self._rebalance(parent)               
        
      
  def _subtree_search(self, p, k):
    """Return Note of p's subtree having key k, or last node searched."""
    
    if k == p.element:                                   # found match
      return p
    elif k < p.element:                                  # search left subtree
      if p.left is not None:
        return self._subtree_search(p.left, k)
      else:
        return None
    else:                                              # search right subtree
      if p.right is not None:
        return self._subtree_search(p.right, k)
      else:
        return None
      
  def search(self,element):
    """Return node with key k, or else neighbor (or None if empty)."""
    if self.root==None:
      return None
    else:
      p = self._subtree_search(self.root, element)
      return p

  def print(self):
    """ Print tree (node and balance factor) using inorder traversal. """
    def _print_inOrder(root):
      if root != None:
        _print_inOrder(root.left)
        print([root.element,root.balanceFactor], end=' ')
        _print_inOrder(root.right)
        
    def _print_preOrder(root):
      if root != None:
        print([root.element,root.balanceFactor], end=' ')
        _print_preOrder(root.left)
        _print_preOrder(root.right)

    print("In-order: ");
    _print_inOrder(self.root)
    print();
    print("Pre-order: ");
    _print_preOrder(self.root)
    print();
#-------utilities for rebalance
  def recompute_balanceFactor(self, p):
    """Q3: recompute balance factor	for not along the path from p to root"""
    return p.left_height() - p.right_height()


  def _recompute_balanceFactor_singleNode(self, p):
    """Q4: recompute balance factor	of a single node"""
    if node is None:
      return 
    return p._node.left_height() - p._node.right_height()



  def _isbalanced(self, p):
    """Q5: check the current node if it is balanced."""
    return abs(p._node.left_height() - p._node.right_height()) <= -1



  def _tall_child(self, p, favorleft=False): # parameter controls tiebreaker
    if p.left_height() + (1 if favorleft else 0) > p.right_height():
      return p.left
    else:
      return p.right

  def _tall_grandchild(self, p):
    child = self._tall_child(p)
    # if child is on left, favor left grandchild; else favor right grandchild
    alignment = (child == p.left)
    return self._tall_child(child, alignment)

  def _rebalance(self, p):
    while p is not None:
      if not self._isbalanced(p):                           # imbalance detected!
        # perform trinode restructuring, setting p to resulting root,
        # and recompute new local heights after the restructuring
        p = self._restructure(self._tall_grandchild(p))
        self._recompute_balanceFactor_singleNode(p.left)
        self._recompute_balanceFactor_singleNode(p.right)
      self._recompute_balanceFactor_singleNode(p)              # adjust for recent changes            
      p = p.parent                                # repeat with parent
	  
  def _relink(self, parent, child, make_left_child):
    """Relink parent node with child node (we allow child to be None)."""
    if make_left_child:                           # make it a left child
      parent.left = child
    else:                                         # make it a right child
      parent.right = child
    if child is not None:                         # make child point to parent
      child.parent = parent

  def _rotate(self, p):
    """Rotate Position p above its parent.

    Switches between these configurations, depending on whether p==a or p==b.

          b                  a
         / \                /  \
        a  t2             t0   b
       / \                     / \
      t0  t1                  t1  t2

    Caller should ensure that p is not the root.
    """
    """Rotate Position p above its parent."""
    x = p
    y = x.parent                                 # we assume this exists
    z = y.parent                                 # grandparent (possibly None)
    if z is None:
      self.root = x                              # x becomes root
      x.parent = None
    else:
      self._relink(z, x, y == z.left)            # x becomes a direct child of z
    # now rotate x and y, including transfer of middle subtree
    if x == y.left:
      self._relink(y, x.right, True)             # x.right becomes left child of y
      self._relink(x, y, False)                   # y becomes right child of x
    else:
      self._relink(y, x.left, False)             # x.left becomes right child of y
      self._relink(x, y, True)                    # y becomes left child of x

  def _restructure(self, x):
    """Perform a trinode restructure among Position x, its parent, and its grandparent.

    Return the Position that becomes root of the restructured subtree.

    Assumes the nodes are in one of the following configurations:

        z=a                 z=c           z=a               z=c
       /  \                /  \          /  \              /  \
      t0  y=b             y=b  t3       t0   y=c          y=a  t3
         /  \            /  \               /  \         /  \
        t1  x=c         x=a  t2            x=b  t3      t0   x=b
           /  \        /  \               /  \              /  \
          t2  t3      t0  t1             t1  t2            t1  t2

    The subtree will be restructured so that the node with key b becomes its root.

              b
            /   \
          a       c
         / \     / \
        t0  t1  t2  t3

    Caller should ensure that x has a grandparent.
    """
    """Perform trinode restructure of Position x with parent/grandparent."""
    y = x.parent
    z = y.parent
    if (x == y.right) == (y == z.right):  # matching alignments
      self._rotate(y)                                 # single rotation (of y)
      return y                                        # y is new subtree root
    else:                                             # opposite alignments
      self._rotate(x)                                 # double rotation (of x)
      self._rotate(x)
      return x                                        # x is new subtree root

#-- Main method
tree = AVL()
test = 1
print('Test Case ', test)
if test==1:  
  """testing slide 24
  The output will look like:
Test Case  1
In-order: 
[12, 0] [23, 0] [26, 0] [30, 0] [37, -1] [45, 0] 
Pre-order: 
[30, 0] [23, 0] [12, 0] [26, 0] [37, -1] [45, 0] 
  """
  tree.insert(23)
  tree.insert(12)
  tree.insert(37)
  tree.insert(30)
  tree.insert(45)
  tree.insert(26)
  tree.print()
  print()
elif test==2:  
  """
  The output will look like:
  Test Case  2
  In-order: 
  [50, 0] [60, 0] [70, 0] 
  Pre-order: 
  [60, 0] [50, 0] [70, 0] 
  In-order: 
  [50, -1] [55, 0] [60, 1] [70, 0] 
  Pre-order: 
  [60, 1] [50, -1] [55, 0] [70, 0] 
  In-order: 
  [50, 0] [52, -1] [55, 0] [60, 0] [70, 0] 
  Pre-order: 
  [52, -1] [50, 0] [60, 0] [55, 0] [70, 0] 
  In-order: 
  [50, 0] [52, 1] [55, 0] [56, 0] [60, 0] [70, 0] 
  Pre-order: 
  [55, 0] [52, 1] [50, 0] [60, 0] [56, 0] [70, 0] 
  In-order: 
  [50, 0] [52, -1] [56, 0] [60, 0] [70, 0] 
  Pre-order: 
  [52, -1] [50, 0] [60, 0] [56, 0] [70, 0] 
  """
  tree.insert(50)
  tree.insert(60)
  tree.insert(70)
  tree.print()
  tree.insert(55)
  tree.print()
  tree.insert(52)
  tree.print()
  tree.insert(56)
  tree.print()

  nd = tree.search(55)
  tree.delete(nd)
  #tree.delete(tree.search(70))
  tree.print()
else:
  """You can test your more examples if it is needed"""
  pass




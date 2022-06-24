#AVL Tree Implementation in Python
class AVLTreeMap(TreeMap):
#----------------------------nested _Node class--------------------------------------
class Node(Treemap._Node):
    #This class maintains height value for balancing for AVL
    __slots__='_height_' #additional data member to store height

    def __init__(self,element,parent=None,left=None,right=None):
        super().__init__(element,parent,left,right)
        self._height = 0 #will be recomputed during balancing

    def left_height(self):
        return self._left._height if self._left is not None else 0

    def right_height(self):
        return self._right._height if self._right is not None else 0
#----------------------- positional-based utility methods----------------------------
    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalanced(self, p):
        return abs(p._node.left_height()-p._node.right_height()

    def _tall_child(self, p, favourleft=False): # parameter controls tiebreaker
        if p._node.left_height() + (1 if facourleft else 0)> p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self,p):
        child = self._tall_child(p)
        #if child is on left, favour left grandchild; else favour grandchild
        alignment = (child==self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self,p):
        while p is not None:
            old_height = p._node._height #trivially 0  if new node
            if not self._isbalanced(p): #imbalance detected
            #perform trinode reconstructinf, setting p to resukting root
            #and recompute new local heights after restructing
                p= self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)

#--------------------------override balancing hooks----------------------------------
def _rebalance_insert(self, p):
    self._rebalance(p)
def _rebalance_delete(self, p):
    self._rebalance(p)
            
            

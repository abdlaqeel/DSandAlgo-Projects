#Binary Removal Algorithm
def _subtree_search(self, p, k):
    #Return position of p's subtree having key last node searched.
    if k == p.key():   #found math
        return p
    elif k < p.key():  #search left subtree
        if self.left(p) is not None:
            return self._subtree_search(self.left(p), k)
        else if self.right(p) is not None:
            return self._subtree_search(self.right(p), k)
        return p

def _delete(self,p):
    #in linked_binary_tree
    child._parent=p._parent

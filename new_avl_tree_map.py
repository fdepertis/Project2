from TdP_collections.map.avl_tree import TreeMap

class NewAVLTreeMap(TreeMap):

    class _Node(TreeMap._Node):
        # -------------------------- nested _Node class --------------------------
        __slots__ = '_balance_factor'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0

    def _isbalanced(self, p):
        node = self._validate(p)
        return -1 <= node._balance_factor <= 1

    def _rebalance(self, p):
        #print("p:",p.element()._value,"left(p):",self.left(p),"right",self.right(p))
        if p._node._balance_factor < 0:
            if self.right(p)._node._balance_factor > 0:
                self._rotate(self.left(self.right(p)))         #right
                """Rotazione effettuata e ora è allineata"""
                self.right(self.right(p))._node._balance_factor += 1 + max(self.right(p)._node._balance_factor, 0)
                self.right(p)._node._balance_factor += 1 - min(self.right(self.right(p))._node._balance_factor, 0)

                self._rotate(self.right(p))         #left
                p._node._balance_factor += 1 - min(self.parent(p)._node._balance_factor, 0)
                self.parent(p)._node._balance_factor += 1 + max(p._node._balance_factor, 0)
            else:
                self._rotate(self.right(p))         #left
                p._node._balance_factor += 1 - min(self.parent(p)._node._balance_factor, 0)
                self.parent(p)._node._balance_factor += 1 + max(p._node._balance_factor, 0)

        elif p._node._balance_factor > 0: #else
            if self.left(p)._node._balance_factor < 0:
                self._rotate(self.right(self.left(p)))          #left #right(left(p))
                """Rotazione effettuata e ora è allineata"""
                self.left(self.left(p))._node._balance_factor += 1 - min(self.left(p)._node._balance_factor, 0)
                self.left(p)._node._balance_factor += 1 + max(self.left(self.left(p))._node._balance_factor, 0)


                self._rotate(self.left(p))          #right
                p._node._balance_factor += 1 + max(self.parent(p)._node._balance_factor, 0)
                self.parent(p)._node._balance_factor += 1 - min(p._node._balance_factor, 0)

            else:
                self._rotate(self.left(p))          #right
                p._node._balance_factor += 1 + max(self.parent(p)._node._balance_factor, 0)
                self.parent(p)._node._balance_factor += 1 - min(p._node._balance_factor, 0)

    # ---------------------------- override balancing hooks -----------------------
    def _rebalance_insert(self, p):
       if not self._isbalanced(p):
           self._rebalance(p)
           return
       parent = self.parent(p)
       if parent:
           if p == self.left(parent):
               parent._node._balance_factor += 1
           else:
               parent._node._balance_factor -= 1
           if parent._node._balance_factor != 0:
               self._rebalance_insert(parent)

    def _rebalance_delete(self, p, v):
        #print(p.key())
        if not p:
            return
        elif not self.left(p) and not self.right(p):
            p._node._balance_factor = 0
        elif not self.left(p):
            p._node._balance_factor -= 1
        elif not self.right(p):
            p._node._balance_factor += 1
        else:
            if p.key() > v:
                p._node._balance_factor -= 1
            else:
                p._node._balance_factor += 1

        if not self._isbalanced(p):
            self._rebalance(p)
            return

        if p._node._balance_factor == 0:
           self._rebalance_delete_auxiliary(p, self.parent(p))

    def _rebalance_delete_auxiliary(self, p, parent):
        if parent:
            if p == self.left(parent):
                parent._node._balance_factor -= 1
            else: #p == self.right(parent)
                parent._node._balance_factor += 1

            if not self._isbalanced(parent):
                self._rebalance(parent)
                return
            if parent._node._balance_factor == 0:
                self._rebalance_delete_auxiliary(parent, self.parent(parent))

if __name__ == '__main__':
    a = NewAVLTreeMap()
    for i in range(1, 1001):
        a[i] = i
    for i in a.inorder():
        print(i.value(),"|",i._node._balance_factor)
    print("--------")
    for i in range (200, 801):
        del a[i]
    for i in a.inorder():
        print(i.value(),"|",i._node._balance_factor)
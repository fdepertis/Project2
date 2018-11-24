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
        #print("p:",p.element()._value,"|",p._node._balance_factor,"left(p):",self.left(p),"right",self.right(p))
        if p._node._balance_factor < 0:

            if self.right(p)._node._balance_factor > 0:

                self._rotate(self.left(self.right(p)))         #right
                """Rotazione effettuata e ora è allineata"""
                self.right(self.right(p))._node._balance_factor += -1 - max(self.right(p)._node._balance_factor, 0)
                self.right(p)._node._balance_factor += -1 + min(self.right(self.right(p))._node._balance_factor, 0)

                self._rotate(self.right(p))         #left
                p._node._balance_factor += 1 - min(self.parent(p)._node._balance_factor, 0)
                self.parent(p)._node._balance_factor += 1 + max(p._node._balance_factor, 0)

            else:

                self._rotate(self.right(p))         #left
                p._node._balance_factor += 1 - min(self.parent(p)._node._balance_factor, 0)
                self.parent(p)._node._balance_factor += 1 + max(p._node._balance_factor, 0)
                #self._rebalance_delete_auxiliary(p,self.parent(p))

        elif p._node._balance_factor > 0: #else

            if self.left(p)._node._balance_factor < 0:

                self._rotate(self.right(self.left(p)))          #left #right(left(p))
                """Rotazione effettuata e ora è allineata"""
                self.left(self.left(p))._node._balance_factor += 1 - min(self.left(p)._node._balance_factor, 0)
                self.left(p)._node._balance_factor += 1 + max(self.left(self.left(p))._node._balance_factor, 0)

                self._rotate(self.left(p))          #right
                p._node._balance_factor += -1 - max(self.parent(p)._node._balance_factor, 0)
                self.parent(p)._node._balance_factor += -1 + min(p._node._balance_factor, 0)

            else:

                #print(self.left(p).element()._value,"|",self.left(p)._node._balance_factor,p.element()._value,"|",p._node._balance_factor)
                self._rotate(self.left(p))          #right

                print(p.element()._value,"|",p._node._balance_factor,self.parent(p).element()._value,"|",self.parent(p)._node._balance_factor)
                p._node._balance_factor += -1 - max(self.parent(p)._node._balance_factor, 0)
                self.parent(p)._node._balance_factor += -1 + min(p._node._balance_factor, 0)
                #self._rebalance_delete_auxiliary(p,self.parent(p))


    # ---------------------------- override balancing hooks -----------------------
    def _rebalance_insert(self, p):

        if not self._isbalanced(p):

            self._rebalance(p)
            return

        parent = self.parent(p)

        if parent is not None:


            if p == self.left(parent):

                parent._node._balance_factor += 1

            else:

                parent._node._balance_factor -= 1

            if parent._node._balance_factor != 0:

                self._rebalance_insert(parent)

    def _rebalance_delete(self, p):

        if not p:

            return

        elif not self.left(p) and not self.right(p):

            p._node._balance_factor = 0

        elif not self.left(p):

            p._node._balance_factor -= 1

        elif not self.right(p):

            p._node._balance_factor += 1

        else:
            if self.num_children(self.left(p)) < self.num_children(self.right(p)):

                p._node._balance_factor -= 1

            elif self.num_children(self.left(p)) > self.num_children(self.right(p)):

                p._node._balance_factor += 1

            elif self.num_children(self.left(p)) == self.num_children(self.right(p)) == 0:

                p._node._balance_factor = 0

        if not self._isbalanced(p):
            self._rebalance(p)
            #print(p.element()._value,"|",p._node._balance_factor,self.parent(p).element()._value,"|",self.parent(p)._node._balance_factor)
            return

        if p._node._balance_factor == 0:
            self._rebalance_delete_auxiliary(p, self.parent(p))

    def _rebalance_delete_auxiliary(self, p, parent):

        if parent is not None:

            if p == self.left(parent):

                parent._node._balance_factor -= 1

            else:

                parent._node._balance_factor += 1

            if not self._isbalanced(parent):

                self._rebalance(parent)
                return

            if parent._node._balance_factor == 0:

                self._rebalance_delete_auxiliary(parent, self.parent(parent))

if __name__ == '__main__':
    a = NewAVLTreeMap()
    for i in range(1, 16):
        a[i] = i
    print("------------------------Insert----------------------------")
    for k in a.inorder():
        print(k.value(),"|",k._node._balance_factor)
    print("------------------------Insert----------------------------")
    for i in range (1, 16):
        print("------------------------Delete----------------------------")
        print("Elimino--->",a[i])
        del a[i]
        print("----------------------------------------------------------")
        for k in a.inorder():
            print(k.value(),"|",k._node._balance_factor)
        print("----------------------------------------------------------")
    for i in range(1, 18):
        a[i] = i
    print("------------------------Insert----------------------------")
    for k in a.inorder():
        print(k.value(),"|",k._node._balance_factor)
    print("------------------------Insert----------------------------")
    for i in reversed(range (1, 18)):
        print("------------------------Delete----------------------------")
        print("Elimino--->",a[i])
        del a[i]
        print("----------------------------------------------------------")
        for k in a.inorder():
            print(k.value(),"|",k._node._balance_factor)
        print("----------------------------------------------------------")


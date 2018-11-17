from TdP_collections.map.avl_tree import TreeMap

class NewAVLTreeMap(TreeMap):

    class _Node(TreeMap._Node):
        # -------------------------- nested _Node class --------------------------
        __slots__ = '_balance_factor'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0

    def _isbalanced(self, p):
        return -1 <= p._node._balance_factor <= 1

    def _recompute_balance_factor(self, x):
        y = self.parent(x)
        z = self.parent(y)

        #Primo caso
        if x == self.right(y) and y == self.right(z):
            # x rimane invariato
            y._node._balance_factor = 0
            if self.left(y) is None:
                if self.left(z) is None:
                    z._node._balance_factor = 0
                else:
                    z._node._balance_factor = 1
            else:
                if self.left(z) is None:
                    z._node._balance_factor = -1
                else:
                    z._node._balance_factor = 0

        #Secondo caso
        elif x == self.left(y) and y == self.left(z):
            #x rimane invariato
            y._node._balance_factor = 0
            if self.right(y) is None:
                if self.right(z) is None:
                    z._node._balance_factor = 0
                else:
                    z._node._balance_factor = -1
            else:
                if self.right(z) is None:
                    z._node._balance_factor = 1
                else:
                    z._node._balance_factor = 0

        #Terzo caso
        elif x == self.left(y) and y == self.right(z):
            x._node._balance_factor = 0
            if self.right(x) is None and self.left(x) is None:
                y._node._balance_factor = 0
                z._node._balance_factor = 0
            elif self.right(x) is None:
                if self.right(y) is None:
                    y._node._balance_factor = 0
                else:
                    y._node._balance_factor = -1
                if self.left(z) is None:
                    z._node._balance_factor = -1
                else:
                    z._node._balance_factor = 0
            else: #self.left(x) is None:
                if self.right(y) is None:
                    y._node._balance_factor = 1
                else:
                    y._node._balance_factor = 0
                if self.left(z) is None:
                    z._node._balance_factor = 0
                else:
                    z._node._balance_factor = 1

        #Quarto caso, cioè se x == self.right(y) and y == self.left(z)
        else:
            x._node._balance_factor = 0
            if self.right(x) is None and self.left(x) is None:
                y._node._balance_factor = 0
                z._node._balance_factor = 0
            elif self.right(x) is None:
                if self.left(y) is None:
                    y._node._balance_factor = 1
                else:
                    y._node._balance_factor = 0
                if self.right(z) is None:
                    z._node._balance_factor = 0
                else:
                    z._node._balance_factor = -1
            else:  # self.left(x) is None:
                if self.left(y) is None:
                    y._node._balance_factor = 0
                else:
                    y._node._balance_factor = 1
                if self.right(z) is None:
                    z._node._balance_factor = -1
                else:
                    z._node._balance_factor = 0


    # ---------------------------- override balancing hooks -----------------------
    def _rebalance_insert(self, p):
        save = None
        cursor = p
        while self.parent(cursor) is not None:
            up_cursor = self.parent(cursor)
            if cursor == self.left(up_cursor):
                up_cursor._node._balance_factor += 1
            else:
                up_cursor._node._balance_factor -= 1

            if not self._isbalanced(up_cursor):
                self._recompute_balance_factor(save)
                self._restructure(save)
            if up_cursor._node._balance_factor == 0:
                cursor = self.root()
            else:
                save = cursor
                cursor = self.parent(cursor)

    def _rebalance_delete(self, p):
        save = None
        cursor = p
        while self.parent(cursor) is not None:
            up_cursor = self.parent(cursor)
            if cursor == self.left(up_cursor):
                up_cursor._node._balance_factor -= 1
            else:
                up_cursor._node._balance_factor += 1

            if not self._isbalanced(up_cursor):
                self._recompute_balance_factor(save)
                self._restructure(save)
            if up_cursor._node._balance_factor == 0:
                cursor = self.root()
            else:
                save = cursor
                cursor = self.parent(cursor)

if __name__ == '__main__':
    a = NewAVLTreeMap()
    for i in range(0, 101):
        a[i] = i
    
    for i in a.inorder():
        print(i.element()._value, "\t", i._node._balance_factor)

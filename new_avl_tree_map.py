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

    def _node_height(self, p):
        node = self._validate(p)
        if node._left is None and node._right is None:
            return 1
        elif node._left is None:
            return 1 + self._node_height(node._right)
        elif node._right is None:
            return 1 + self._node_height(node._left)
        else:
            return 1 + max(self._node_height(node._left), self._node_height(node._right ))
    # ---------------------------- override balancing hooks -----------------------
    def _rebalance_insert(self, p):
        print("\nè stato inserito", p.element()._value)
        save = None
        cursor = p
        while self.parent(cursor) is not None:
            up_cursor = self.parent(cursor)
            if cursor == self.left(up_cursor):
                up_cursor._node._balance_factor += 1
                print("up_cursor._node._balance_factor", up_cursor.element()._value, up_cursor._node._balance_factor)
            else:
                up_cursor._node._balance_factor -= 1
                print("up_cursor._node._balance_factor", up_cursor.element()._value, up_cursor._node._balance_factor)
            if not self._isbalanced(up_cursor):
                print("Trovato nodo non bilanciato")
                save._node._balance_factor = 0
                cursor._node._balance_factor = 0
                up_cursor._node._balance_factor = 0
                print("Up Cursor:", up_cursor.element()._value)
                print("Cursor:", cursor.element()._value)
                print("Save:", save.element()._value)
                self._restructure(save)
                print("Rotazione effettuata")
            if up_cursor._node._balance_factor == 0:
                cursor = self.root()
            else:
                save = cursor
                cursor = self.parent(cursor)

    """def _rebalance_delete(self, p):
        cursor = p
        while self.parent(cursor) is not None:
            up_cursor = self.parent(cursor)
            if cursor == self.left(up_cursor):
                up_cursor._node._balance_factor -= 1
            else:
                up_cursor._node._balance_factor += 1
            if not self._isbalanced(up_cursor):
                print("Trovato nodo non bilanciato")
                cursor._node._balance_factor = 0
                up_cursor._node._balance_factor = 0
                self._restructure(p)
                print("Rotazione effettuata")
            if up_cursor._node._balance_factor == 0:
                cursor = None
            else:
                cursor = self.parent(cursor)"""

if __name__ == '__main__':
    a = NewAVLTreeMap()
    a[0] = 0
    a[1] = 1
    a[2] = 2
    a[3] = 3
    a[4] = 4
    a[5] = 5
    a[6] = 6

    print("\tSTAMPA!")
    print("\t  ",a.root().element()._value)
    print("\t", a.left(a.root()).element()._value, "\t", a.right(a.root()).element()._value)

    if a.left(a.left(a.root())) is not None:
        print(a.left(a.left(a.root())).element()._value,end='\t')
    else:
        print("N",end='\t')
    if a.right(a.left(a.root())) is not None:
        print(a.right(a.left(a.root())).element()._value,end='\t')
    else:
        print("N",end='\t')
    if a.left(a.right(a.root())) is not None:
        print(a.left(a.right(a.root())).element()._value,end='\t')
    else:
        print("N",end='\t')
    if a.right(a.right(a.root())) is not None:
        print(a.right(a.right(a.root())).element()._value,end='\n')
    else:
        print("N",end='\t')
#    print(a.right(a.right(a.right(a.root()))).element()._value)
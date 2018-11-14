from TdP_collections.map.avl_tree import TreeMap

class NewAVLTreeMap(TreeMap):

    class _Node(TreeMap._Node):

        # -------------------------- nested _Node class --------------------------
        __slots__ = '_balance_factor'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0

        def height(self):
            if self is None:
                return 0
            else:
                return 1 + max(self._left.height(), self._right.height())

    def _isbalanced(self, p):
        return -1 <= p._node._balance_factor <= 1

    def _recompute_balance_factor(self, p):
        pass

    def _tall_child(self, p, favorleft=False):  # parameter controls tiebreaker
        pass

    def _tall_grandchild(self, p):
        pass

    def _rebalance(self, p):
        pass

    # ---------------------------- override balancing hooks ----------------------------
    def _rebalance_insert(self, p):
        cursor = p
        while cursor is not None:
            up_cursor = self.parent(cursor)
            if cursor == self.left(up_cursor):
                cursor._node._balance_factor -= 1
            else:
                cursor._node._balance_factor += 1
            cursor = self.parent(cursor)
        self._rebalance(p)

    def _rebalance_delete(self, p):
        cursor = p
        while cursor is not None:
            up_cursor = self.parent(cursor)
            if cursor == self.left(up_cursor):
                cursor._node._balance_factor += 1
            else:
                cursor._node._balance_factor -= 1
            cursor = self.parent(cursor)
        self._rebalance(p)

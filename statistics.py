#from new_avl_tree_map import NewAVLTreeMap
from TdP_collections.map.avl_tree import AVLTreeMap
import json

class Statistics():

    class _Value:
        def __init__(self, f, t):
            self._frequency = f
            self._total = t

    def __init__(self, file_name = None):
        self._tree = AVLTreeMap()
        self._occurrences = 0
        self._average = 0
        if file_name:
            file = open("dataset.json")
            dataset = json.load(file)
            for k in dataset:
                print(k, dataset[k])
                self.add(k, dataset[k])

    def add(self, k, v):
        if k in self._tree:
            self._tree[k]._frequency += 1
            self._tree[k]._total += v
        else:
            self._tree[k] = self._Value(1, v)

        self._occurrences += 1
        if self._occurrences == 1:
            self._average = v
        else:
            self._average = (self._average * (self._occurrences - 1) + v)/ self._occurrences

    def len(self):
        """Complessità: O(1)"""
        return len(self._tree)

    def occurrences(self):
        """Complessità: O(1)"""
        return self._occurrences

    def average(self):
        """Complessità: O(1)"""
        return self._average

    def median(self):
        return self.percentile(50)

    def percentile(self, j = 20):
        if not 1 <= j <= 99:
            raise ValueError("Parameter must be between 1 and 99.")
        else:
            n = round(self.occurrences() * (j / 100))
            print("n =", n)
            cursor = self._tree.first()
            c = 1
            for i in range(n):
                if cursor.value()._frequency == c:
                    cursor = self._tree.after(cursor)
                    c = 1
                else:
                    c += 1
            return cursor.key()

    def mostFrequent(self, j):
        array = list(self._tree.positions())
        for i in range(len(array)-1):
            modified = False
            for k in range(len(array)-i-1):
                if array[k].value()._frequency < array[k+1].value()._frequency:
                    array[k], array[k+1] = array[k+1], array[k]
                    modified = True
            if not modified:
                break
        for i in range(j):
            array[i] = array[i].key()
        return array[:j]


    def __str__(self):
        s = "Key\t\t\tFrequency\tTotal\n"
        for e in self._tree.positions():
            s += str(e.key()) + "\t" + str(e.value()._frequency) + "\t\t\t" + str(e.value()._total) + "\n"
        s += "Total Occurrences: " + str(self.occurrences()) + "\nAverage: " + str(self.average())
        return s

if __name__ == '__main__':
    s = Statistics()
    s.add("Giuseppe", 20)
    s.add("Giuseppe", 20)
    s.add("Giuseppe", 20)
    s.add("Giuseppe", 20)
    s.add("Giuseppe", 20)
    s.add("Andrea  ", 20)
    s.add("Andrea  ", 20)
    s.add("Andrea  ", 20)
    s.add("Andrea  ", 20)
    s.add("Simone  ", 20)
    s.add("Simone  ", 20)
    s.add("Simone  ", 20)
    s.add("Giovanni", 20)
    s.add("Giovanni", 20)
    s.add("Francesco", 20)
    print(s)
    print(s.median())
    print(s.percentile(25))
    print(s.percentile(75))
    print(s.mostFrequent(3))
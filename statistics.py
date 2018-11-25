from new_avl_tree_map import NewAVLTreeMap
import json

class Statistics():

    class _Value:
        def __init__(self, f, t):
            self._frequency = f
            self._total = t

    def __init__(self, file_name = None):
        """Complessità: O(n*log2(n))"""
        self._tree = NewAVLTreeMap()
        self._occurrences = 0
        self._average = None
        if file_name:
            file = open(file_name)
            dataset = json.load(file)
            for (k, v) in dataset:
                self.add(k, v)

    def add(self, k, v):
        """Complessità: O(log2(n))"""
        if k in self._tree:
            self._tree[k]._frequency += 1
            self._tree[k]._total += v
        else:
            self._tree[k] = self._Value(1, v)

        self._occurrences += 1
        if self._occurrences == 1:
            self._average = v
        else:
            self._average = (self._average * (self._occurrences - 1) + v) / self._occurrences

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
        """Complessità: O(n*log2(n))"""
        return self.percentile(50)

    def percentile(self, j = 20):
        """Complessità: O(n*log2(n))"""
        if not 1 <= j <= 99:
            raise ValueError("Parameter must be between 1 and 99.")
        else:
            n = round(self.occurrences() * (j / 100))
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
        """Complessità: O(n*log2(n))"""
        array = list(self._tree.positions())
        _mergeSort(array)
        for i in range(j):
            array[i] = array[i].key()
        return array[:j]

    def __str__(self):
        s = "Key\t\t\tFrequency\tTotal\n"
        for e in self._tree.positions():
            s += str(e.key()) + "\t" + str(e.value()._frequency) + "\t\t\t" + str(e.value()._total) + "\n"
        s += "Total Occurrences: " + str(self.occurrences()) + "\nAverage: " + str(self.average())
        return s

def _mergeSort(alist):
    """Complessità: O(n*log2(n))"""
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        _mergeSort(lefthalf)
        _mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].value()._frequency > righthalf[j].value()._frequency:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

if __name__ == '__main__':
    s = Statistics("dataset.json")
    print(s)
    print("\nFirst quartile:\t", s.percentile(25))
    print("Median:\t\t\t", s.median())
    print("Third quartile:\t", s.percentile(75),"\n")
    print("3 most frequent keys:")
    for i in s.mostFrequent(3):
        print(i)
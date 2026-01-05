from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array):
        pass

class BubbleSortStrategy(SortingStrategy):
    def sort(self, array):
        print("Sorting using Bubble Sort")

class QuickSortStrategy(SortingStrategy):
    def sort(self, array):
        print("Sorting using Quick Sort")

class Sorter:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_array(self, array):
        self.strategy.sort(array)

if __name__ == "__main__":
    sorter = Sorter()
    array = [5, 3, 8, 4, 2]
    sorter.set_strategy(BubbleSortStrategy())
    sorter.sort_array(array)
    sorter.set_strategy(QuickSortStrategy())
    sorter.sort_array(array)

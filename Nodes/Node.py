import abc

class Node(abc.ABC):

    @abc.abstractmethod
    def parse(self):
        pass

    @abc.abstractmethod
    def printN(self, shift=0):
        pass

    @abc.abstractmethod
    def execute(self):
        pass

import abc

class Node(abc.ABC):

    @abc.abstractmethod
    def parse(self):
        pass

    @abc.abstractmethod
    def print(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass

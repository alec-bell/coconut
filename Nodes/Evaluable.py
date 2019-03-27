import abc

class Evaluable(abc.ABC):

    @abc.abstractmethod
    def evaluate(self):
        """Evaluate the value represented by a Node."""
        pass

import abc

class Executable(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        """Execute the processes represented by a node."""
        pass

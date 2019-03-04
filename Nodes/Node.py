import abc

class Node(abc.ABC):

    @abc.abstractmethod
    def parse(self):
        """Parse the user-defined CORE code or output any errors."""
        pass

    @abc.abstractmethod
    def pretty_print(self, shift=0):
        """Print the CORE code represented by a node in an attractive format, indenting :shift times."""
        pass

    @abc.abstractmethod
    def execute(self):
        """Execute the processes represented by a node."""
        pass

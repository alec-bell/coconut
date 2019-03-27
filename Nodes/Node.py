import abc

class Node(abc.ABC):

    @abc.abstractmethod
    def parse(self):
        """Parse the code to set the object data model for a Node derivation or output any errors."""
        pass

    @abc.abstractmethod
    def pretty_print(self, shift=0):
        """Print the code represented by a node in an attractive format, indenting :shift times."""
        pass

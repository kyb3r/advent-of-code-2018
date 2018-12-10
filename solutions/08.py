from aocd import data
from dataclasses import dataclass, field
from utils import timed

@dataclass
class Node:
    children: list = field(default_factory=list)
    metadata: list = None

    @classmethod
    def from_data(cls, data):
        node = cls()

        num_children = data.pop(0)
        num_metadata = data.pop(0)

        for x in range(num_children):
            child = cls.from_data(data)
            node.children.append(child)

        node.metadata = [data.pop(0) for x in range(num_metadata)]
        return node
    
    @property
    def value(self):
        if not self.children:
            return sum(self.metadata)
        return sum(
            self.children[index-1].value 
            for index in self.metadata 
            if index-1 < len(self.children)
            )

    @property
    def metasum(self):
        return sum(self.metadata) + sum(c.metasum for c in self.children)


input = [int(i) for i in data.split()]
root = Node.from_data(input)

print(root.metasum)
print(root.value)

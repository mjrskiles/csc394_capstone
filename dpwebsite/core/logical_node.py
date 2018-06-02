"""
A structure for representing boolean logic trees
"""

# This class is not meant to be instantiated directly. It is only a super class.
class Node:
    def __init__(self):
        super().__init__()
        self.children = []

    def __str__(self):
        return "Node"

    def truthValue(self, truthList):
        return False

    def printTree(self):
        self.r_printTree(self, 0)

    def r_printTree(self, root, level):
        # Indent properly
        if level > 0:
            for i in range(level - 1):
                print('  ', end='')
            print('`-', end='')
        print(self)
        for child in self.children:
            child.r_printTree(child, level + 1)

class OperationNode(Node):
    def __init__(self):
        super().__init__()
        self.children = []

    def __str__(self):
        return "OperationNode"

    def addChild(self, child):
        self.children.append(child)

class And(OperationNode):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "and"
    
    def truthValue(self, truthList):
        # All children must be true for an AND to be true
        for c in self.children:
            if c.truthValue(truthList) == False:
                return False
        return True

class Or(OperationNode):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "or"
        
    def truthValue(self, truthList):
        # Only one child has to be true in an OR node
        for c in self.children:
            if c.truthValue(truthList) == True:
                return True
        return False

class CourseLeaf(Node):
    def __init__(self, course):
        super().__init__()
        self.course = course
        self.children = []

    def __str__(self):
        return self.course

    def truthValue(self, truthList):
        if self.course in truthList:
            return True
        else:
            return False

class MinimumLeaf(Node):
    def __init__(self, min):
        super().__init__()
        self.min = min # min is an Int
        self.children = []

    def __str__(self):
        return "Minimum {} classes".format(self.min)

    def truthValue(self, truthList):
        if min > len(truthList):
            return False
        else:
            return True


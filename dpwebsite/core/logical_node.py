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

    def truthValue(self, truth_list):
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
    
    def truthValue(self, truth_list):
        # All children must be true for an AND to be true
        for c in self.children:
            if not c.truthValue(truth_list):
                return False
        return True

class Or(OperationNode):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "or"
        
    def truthValue(self, truth_list):
        # Only one child has to be true in an OR node
        for c in self.children:
            if c.truthValue(truth_list):
                return True
        return False

class CourseLeaf(Node):
    def __init__(self, course):
        super().__init__()
        self.course = course
        self.children = []

    def __str__(self):
        return self.course

    def truthValue(self, truth_list):
        if self.course in truth_list:
            return True
        else:
            return False

class MinimumLeaf(Node):
    def __init__(self, minimum):
        super().__init__()
        self.minimum = minimum # minimum is an Int
        self.children = []

    def __str__(self):
        return "Minimum {} classes".format(self.minimum)

    def truthValue(self, truth_list):
        # print(minimum)
        if self.minimum > len(truth_list):
            return False
        else:
            return True

class MinimumSetLeaf(Node):
    def __init__(self, minimum, course_list):
        super().__init__()
        self.minimum = minimum # minimum is an Int
        self.course_list = course_list
        self.children = []

    def __str__(self):
        return "Minimum {} of {}".format(self.minimum, self.course_list)

    def truthValue(self, truth_list):
        num_fullfilled = 0
        for c in self.course_list:
            if c in truth_list:
                num_fullfilled += 1
            if num_fullfilled >= self.minimum:
                return True

        return False

class NoRequirement(Node):
    def __init__(self):
        super().__init__()
        self.children = []

    def __str__(self):
        return 'No Requirement'

    def truthValue(self, truth_list):
        return True
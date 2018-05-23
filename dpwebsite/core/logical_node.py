"""
A structure for representing boolean logic trees
"""

# This class is not meant to be instantiated directly. It is only a super class.
class LogicalNode:
    def __init__(self):
        super().__init__()

    def truthValue(self, truthList):
        return False

class LogicalOperationNode(LogicalNode):
    def __init__(self):
        super().__init__()
        self.children = []

    def addChild(self, child):
        self.children.append(child)

class LogicalAnd(LogicalOperationNode):
    def __init__(self):
        super().__init__()
    
    def truthValue(self, truthList):
        # All children must be true for an AND to be true
        for c in self.children:
            if c.truthValue(truthList) == False:
                return False
        return True

class LogicalOr(LogicalOperationNode):
    def __init__(self):
        super().__init__()
        
    def truthValue(self, truthList):
        # Only one child has to be true in an OR node
        for c in self.children:
            if c.truthValue(truthList) == True:
                return True
        return False

class LogicalCourseLeaf(LogicalNode):
    def __init__(self, course):
        super().__init__()
        self.course = course

    def truthValue(self, truthList):
        if self.course in truthList:
            return True
        else:
            return False

class LogicalMinimumLeaf(LogicalNode):
    def __init__(self, min):
        super().__init__()
        self.min = min # min is an Int

    def truthValue(self, truthList):
        if min > len(truthList):
            return False
        else:
            return True

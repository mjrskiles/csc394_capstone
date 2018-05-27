"""
This class provides methods to build a graph of courses by prerequisite
and searching the graph to find a shortest degree path.abs
"""

"""
regexes:
' or (?=\\()' matches an 'or' only if followed by (
'(?<=\\)) or ' matches an 'or' only if preceded by )
' and (?=\\()'
'(?<=\\)) and '

These can be used to split strings by logical operations while keeping parentheses grouped.

e.g. re.split(' or (?=\\()', 'SE 450 or (CSC 301 and SE 430)')
returns ['SE 450', '(CSC 301 or SE 430)']
"""

from django.db import models
from dpwebsite.core.models import Courses
import dpwebsite.core.logical_node as node
import re

whitespace = ' \t\n\r'

"""
A Requirement represents a prerequisite rule for a single course
"""
class Requirement:
    def __init__(self, prerequisites):
        self.prerequisites = self.parse_rules(prerequisites)

    def parse_rules(self, prerequisites):
        return []

class Node:
    def __init__(self):
        self.children = []

    def addChild(self, child):
        self.children.append(child)

class CourseNode(Node):
    def __init__(self, course, rules):
        super().__init__()
        self.parents = [] # CourseNode[]
        self.course = course
        self.prerequisiteRules = rules

        # grab an array of just the course relationships
        regex = '[A-Za-z]+ [0-9]+'
        matcher = re.compile(regex)
        self.relationships = matcher.findall(rules)
        print('{} relationships: {}'.format(self.course, self.relationships))

    def __str__(self):
        return str(self.course)

    def addParent(self, parent):
        self.parents.append(parent)

class PathFinder:
    def __init__(self):
        self.addedToGraph = {}
        self.courseList = []
        self.root = Node()

    def build_course_list(self):
        table = Courses.objects.all()

        for c in table:
            courseName = '{} {}'.format(c.CRSE_SUBJECT, c.CRSE_NBR).strip(whitespace)
            prereqStr = c.CRSE_PREREQUISITE
            course = CourseNode(courseName, prereqStr)
            self.courseList.append(course)

    def build_graph(self):
        self.build_course_list()

        while len(self.courseList) > 0:
            c = self.courseList.pop()
            self.insert(c, self.root)


    def insert(self, node, root):
        if len(node.relationships) == 0:
            root.addChild(node)
            print('Added {} as child of root (1)'.format(node))
            self.addedToGraph[node.course] = node
            return
        
        else:
            for relation in node.relationships:
                if relation in self.addedToGraph:
                    prereq = self.addedToGraph[relation]
                    prereq.addChild(node)
                    self.addedToGraph[node.course] = node
                    print('Added {} as child of {} (2)'.format(node, prereq))

                else:
                    prereq = self.popNodeWithName(relation)
                            
                    if prereq:
                        prereq.addChild(node)
                        self.addedToGraph[node.course] = node
                        print('Added {} as child of {} (3)'.format(node, prereq))
                        self.insert(prereq, root)
                    else:
                        print("Couldn't pop the node for {}".format(relation))
                        
    def popNodeWithName(self, name):
        for i in range(len(self.courseList)):
            if self.courseList[i].course.strip(whitespace) in name.strip(whitespace):
                return self.courseList.pop(i)
        return None


    def find_shortest_path(self):
        pass

    def print_course_list(self):
        table = Courses.objects.all()
        i = 1
        for course in table:
            print('{:3}. Course: {:3} {:3} Prereq: {}'.format(i, course.CRSE_SUBJECT, course.CRSE_NBR, course.CRSE_PREREQUISITE))
            i += 1


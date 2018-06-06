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
from dpwebsite.core.models import CoreCourses as Courses
import dpwebsite.core.logical_node as node
import dpwebsite.core.rule_parser as rp
import dpwebsite.core.graduation_rule as grad
import re

whitespace = ' \t\n\r'

class Node:
    def __init__(self):
        self.children = []
        self.depth = -1

    def add_child(self, child):
        self.children.append(child)

class CourseNode(Node):
    def __init__(self, course, rules,id):
        super().__init__()
        self.id = id
        self.parents = [] # CourseNode[]
        self.course = course
        self.prerequisite_rule = rp.RuleParser.parse(rules)
        if self.prerequisite_rule is None:
            self.prerequisite_rule = node.NoRequirement()

        # grab an array of just the course relationships
        regex = '[A-Za-z]+ [0-9]+'
        matcher = re.compile(regex)
        self.relationships = matcher.findall(rules)
        # print('{} relationships: {}'.format(self.course, self.relationships))

    def __str__(self):
        return str(self.course)

    def add_parent(self, parent):
        self.parents.append(parent)

class PathFinder:
    def __init__(self):
        self.added_to_graph = {}
        self.course_titles = {}
        self.course_list = []
        self.root = Node()

    def build_course_list(self):
        table = Courses.objects.all()

        for c in table:
            courseName = '{} {}'.format(c.CRSE_SUBJECT, c.CRSE_NBR).strip(whitespace)
            prereqStr = c.CRSE_PREREQUISITE
            courseTitle = c.CRSE_TITLE
            self.course_titles[courseName] = courseTitle
            course = CourseNode(courseName, prereqStr,c.id)
            self.course_list.append(course)

    def build_graph(self):
        self.build_course_list()

        while len(self.course_list) > 0:
            c = self.course_list.pop()
            self.insert(c, self.root)

    def get_course_titles(self):
        return self.course_titles

    def insert(self, node, root):
        if len(node.relationships) == 0:
            root.add_child(node)
            # print('Added {} as child of root (1)'.format(node))
            self.added_to_graph[node.course] = node
            return

        else:
            for relation in node.relationships:
                if relation in self.added_to_graph:
                    prereq = self.added_to_graph[relation]
                    prereq.add_child(node)
                    self.added_to_graph[node.course] = node
                    # print('Added {} as child of {} (2)'.format(node, prereq))

                else:
                    prereq = self.pop_node_with_name(relation)

                    if prereq:
                        prereq.add_child(node)
                        self.added_to_graph[node.course] = node
                        # print('Added {} as child of {} (3)'.format(node, prereq))
                        self.insert(prereq, root)
                    else:
                        print("Couldn't pop the node for {}".format(relation))

    def pop_node_with_name(self, name):
        for i in range(len(self.course_list)):
            if self.course_list[i].course.strip(whitespace) in name.strip(whitespace):
                return self.course_list.pop(i)
        return None

    def assign_node_depths(self):
        self.r_assign_node_depths(self.root, 0)

    def r_assign_node_depths(self, root, level):
        if root.depth < 0 or root.depth > level:
            root.depth = level
            for c in root.children:
                self.r_assign_node_depths(c, level + 1)

    def find_shortest_path(self, major_index, focus_index, courses_per_term):
        self.build_graph()
        self.assign_node_depths()
        grad_rule = grad.build_rule(major_index, focus_index)

        # find courses with least requirements
        focus_lists = grad.major_focus_lists[major_index]

        # pick the 4 quickest for the selected focus
        chosen_focus_electives = self.pick_n_of_min_depth(4, focus_lists[focus_index])
        #print("Chosen focus elect. ")
        #for n in chosen_focus_electives:
         #   print('  ' + n.course)

        # choose 4 from the other advanced electives
        other_electives_list = []
        for i in range(len(focus_lists)):
            if i != focus_index:
                other_electives_list.extend(focus_lists[i])

        chosen_outside_electives = self.pick_n_of_min_depth(4, other_electives_list)
        #print("Chosen other elect. ")
        #for n in chosen_outside_electives:
         #   print('  ' + n.course )

        base_course_list = re.findall('[A-Z]+ [0-9]+', grad.major_base_courses[major_index], re.I)
        #print("Base courses:")
        #for c in base_course_list:
         #   print('  ' + c)

        base_courses = []
        for c in base_course_list:
            if c in self.added_to_graph:
                node = self.added_to_graph[c]
                base_courses.append(node)
        # print(base_courses)

        # Put all the required course and sort them in order from most prereqs to least
        all_req_courses = base_courses
        all_req_courses.extend(chosen_focus_electives)
        all_req_courses.extend(chosen_outside_electives)
        all_req_courses.sort(key=lambda x: x.depth, reverse=True)
        # print(all_req_courses)

        terms = []
        taken_so_far = []

        # What if all of a courses prereqs aren't in the list? push them to the end of the list?
        loop_count = 0
        while not grad_rule.truthValue(taken_so_far):
            # print("Determined graduation requirements to not be met.")
            this_term = []
            i = 0
            # print("Terms so far:")
            # for t in terms:
            #     print("Term")
            #     for c in t:
            #         print('  ' + c.course)
            while len(this_term) < courses_per_term and i < len(all_req_courses):
                node = all_req_courses[i]
                # print("Checking node {}".format(node.course))
                if node not in taken_so_far and node not in this_term:
                    # print("With prereq rule:")
                    # node.prerequisite_rule.printTree()
                    if node.prerequisite_rule.truthValue(taken_so_far):
                        # print("Added course to term {}".format(node.course))
                        all_req_courses.remove(node)
                        this_term.append(node)
                    else:
                        for c in node.relationships:
                            if c in self.added_to_graph:
                                req = self.added_to_graph[c]
                                if req not in all_req_courses:
                                    all_req_courses.append(req)
                i += 1
                # input("")

            if len(this_term):
                terms.append(this_term)
                # print("Added term:")
                for c in this_term:
                    taken_so_far.append(c.course)
                    # print('  ' + c.course)

            loop_count += 1
            if loop_count > 100:
                print("There was an error, got stuck in a loop.")
                break

        return terms




    def pick_n_of_min_depth(self, n, course_list):
        chosen_electives = []
        for c in course_list:
            if c in self.added_to_graph:
                node = self.added_to_graph[c]
                chosen_electives.append(node)
            if len(chosen_electives) >= n:
                break

        max_i = self.index_of_largest_depth(chosen_electives)

        for c in course_list[n:]:
            if c in self.added_to_graph:
                node = self.added_to_graph[c]
                if node.depth < chosen_electives[max_i].depth and node not in chosen_electives:
                    chosen_electives[max_i] = node
                    max_i = self.index_of_largest_depth(chosen_electives)
        return chosen_electives


    def index_of_largest_depth(self, l):
        largest = 0
        for i in range(len(l)):
            # print(l[i])
            if l[i].depth > l[largest].depth:
                largest = i
        # print(largest)
        return largest

    def print_course_list(self):
        table = Courses.objects.all()
        i = 1
        for course in table:
            print('{:3}. Course: {:3} {:3} Prereq: {}'.format(i, course.CRSE_SUBJECT, course.CRSE_NBR, course.CRSE_PREREQUISITE))
            i += 1

    def print_graph(self):
        self.rprint_graph(self.root, 0)

    def rprint_graph(self, root, level):
        for child in root.children:
            # Indent properly
            if level > 0:
                for i in range(level - 1):
                    print('| ', end='')
                print('`-', end='')
            print('{} - Depth {}'.format(child.course, child.depth))
            self.rprint_graph(child, level + 1)

def test():
    for i in range(8):
        # if i == 3 or i == 6:
        #     continue
        print("\nCS Focus {} Shortest path is:".format(i))
        pf = PathFinder()
        plan = pf.find_shortest_path(grad.Major.CS, i, 3)
        
        for i in range(len(plan)):
            print("Term {}".format(i + 1))
            for c in plan[i]:
                print('  ' + c.course)

    for i in range(5):
        print("\nIS Focus {} Shortest path is:".format(i))
        pf = PathFinder()
        plan = pf.find_shortest_path(grad.Major.IS, i, 3)
        
        for i in range(len(plan)):
            print("Term {}".format(i + 1))
            for c in plan[i]:
                print('  ' + c.course)


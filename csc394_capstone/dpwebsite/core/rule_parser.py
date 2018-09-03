"""
A class to parse prerequisite rules into logical nodes

rules are in the form
`A and B and (C or D) and ~n`

Where logical operators and parentheses can be combined in any
reasonable order. ~n designates a requirement to have taken
n classes.

regexes:
' or (?=\\()' matches an 'or' only if followed by (
'(?<=\\)) or ' matches an 'or' only if preceded by )
' and (?=\\()'
'(?<=\\)) and '

These can be used to split strings by logical operations while keeping parentheses grouped.

e.g. re.split(' or (?=\\()', 'SE 450 or (CSC 301 and SE 430)')
returns ['SE 450', '(CSC 301 or SE 430)']
"""


import dpwebsite.core.logical_node as node
import re

examples = [
    'CSC 431 and (HCI 440 or HCI 441)',
    'CSC 401 and CSC 430 and CSC 435',
    'CSC 401 or CSC 402 or CSC 425',
    'CSC 450 and (CSC 425 or DSC 450) and CSC 406',
    '(CSC 423 or CSC 302) and CSC 419 and ~5',
    '(CSC 301 or CSC 373) and CSC 450 and (HCI 440 or HCI 441)',
    '(CSC 301 or CSC 373) and CSC 450 and (HCI 440 or HCI 441) and ~2(CSC 405, CSC 512, CSC 345)'
]

and_after_paren = '(?<=\\)) and '
and_before_paren = ' and (?=\\()'
or_after_paren = '(?<=\\)) or '
or_before_paren = ' or (?=\\()'
after_paren = '(?<=\\))[ ]+'
course_match = '[A-Z]+ [0-9]+'
min_set = '~[0-9]+\\([A-Za-z0-9, ]+\\)'

class RuleParser:
    @staticmethod
    def parse(rule: str):
        """
        Returns a logical node constructed by breaking the rule into a tree
        """

        rule = rule.strip()
        if len(rule):

            # Handle cases where there is a nested rule first
            if rule.startswith('('):
                split_rule = re.split(after_paren, rule, maxsplit=1)
                split_rule = list(map(lambda x: x.strip(), split_rule))

                if len(split_rule) == 1:
                    return RuleParser.parse(split_rule[0].strip('()'))
                else:
                    #re.I = ignore case
                    if bool(re.match('and', split_rule[1][:3], re.I)):
                        and_node = node.And()
                        and_node.addChild(RuleParser.parse(split_rule[0].strip('()')))
                        and_node.addChild(RuleParser.parse(split_rule[1][3:]))
                        return and_node
                    
                    elif bool(re.match('or', split_rule[1][:2], re.I)):
                        or_node = node.Or()
                        or_node.addChild(RuleParser.parse(split_rule[0].strip('()')))
                        or_node.addChild(RuleParser.parse(split_rule[1][2:]))
                        return or_node

                    else:
                        # Something went wrong
                        print("RuleParser.parse: Could not match a logical operator after a parenthesis")

            else:
                mAnd = re.search('and', rule, re.I)
                mOr = re.search('or', rule, re.I)

                if not mAnd and not mOr:
                    # It's a leaf node
                    if rule.startswith('~'):
                        if bool(re.fullmatch('~[0-9]+', rule)):
                            rule = rule.strip('~')
                            min = int(rule)
                            return node.MinimumLeaf(min)

                        elif bool(re.fullmatch(min_set, rule, re.I)):
                            min_str = re.search('[0-9]+', rule).group()
                            min = int(min_str)
                            courses = re.findall(course_match, rule, re.I)
                            if min > len(courses):
                                print("Minimum Set requirement was larger than its course list.")
                            else:
                                return node.MinimumSetLeaf(min, courses)

                        else:
                            print("RuleParser.parse: Problem parsing a minimum leaf rule.")

                    elif bool(re.fullmatch(course_match, rule, re.I)):
                        return node.CourseLeaf(rule)

                    elif bool(re.fullmatch('None', rule, re.I)):
                        return node.NoRequirement()

                    else:
                        print("RuleParser.parse: Node {} appeared to be a leaf, but was invalid.".format(rule))
                
                elif mAnd and mOr:
                    if mAnd.start() < mOr.start():
                        return RuleParser.buildAndNode(rule, mAnd.start(), mAnd.end())

                    else:
                        return RuleParser.buildOrNode(rule, mOr.start(), mOr.end())

                elif mAnd:
                    return RuleParser.buildAndNode(rule, mAnd.start(), mAnd.end())

                elif mOr:
                    return RuleParser.buildOrNode(rule, mOr.start(), mOr.end())

                else:
                    print("RuleParser.parse: Node was not a leaf, but something went wrong.")

    @staticmethod
    def buildAndNode(rule, sliceStart, sliceEnd):
        and_node = node.And()
        and_node.addChild(RuleParser.parse(rule[0:sliceStart]))
        and_node.addChild(RuleParser.parse(rule[sliceEnd:]))
        return and_node

    @staticmethod
    def buildOrNode(rule, sliceStart, sliceEnd):
        or_node = node.Or()
        or_node.addChild(RuleParser.parse(rule[0:sliceStart]))
        or_node.addChild(RuleParser.parse(rule[sliceEnd:]))
        return or_node

def test():
    for ex in examples:
        rule = RuleParser.parse(ex)
        rule.printTree()

if __name__ == '__main__':
    test()



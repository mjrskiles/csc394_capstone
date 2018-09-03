"""
This is a convenience module to store graduation rules and return a logic node
parsed from its rules.
"""

cs_introductory = 'CSC 400 and CSC 401 and CSC 402 and CSC 403 and CSC 406 and CSC 407'
cs_foundation = 'CSC 421 and CSC 435 and CSC 447 and CSC 453 and SE 450'

# Electives
#   Listed by focus

# Software and Systems development focus
sw_sys_dev = [
    'CSC 436',
    'CSC 438',
    'CSC 439',
    'CSC 443',
    'CSC 448',
    'CSC 461',
    'CSC 462',
    'CSC 471',
    'CSC 472',
    'CSC 475',
    'CSC 534',
    'CSC 536',
    'CSC 540',
    'CSC 548',
    'CSC 549',
    'CSC 551',
    'CSC 552',
    'CSC 553',
    'CSC 595',
    'CNS 450',
    'GAM 690',
    'GAM 691',
    'HCI 441',
    'SE 441',
    'SE 452',
    'SE 459',
    'SE 525',
    'SE 526',
    'SE 554',
    'SE 560',
    'SE 491',
    'SE 591',
    'TDC 478',
    'TDC 484',
    'TDC 568'
]

# Theory focus
theory = [
    'CSC 431',
    'CSC 440',
    'CSC 444',
    'CSC 489',
    'CSC 503',
    'CSC 521',
    'CSC 525',
    'CSC 531',
    'CSC 535',
    'CSC 547',
    'CSC 557',
    'CSC 580',
    'CSC 591',
    'SE 533'
]

# Data Science focus
data_science = [
    'CSC 423',
    'CSC 424',
    'CSC 425',
    'CSC 433',
    'CSC 465',
    'CSC 478',
    'CSC 481',
    'CSC 482',
    'CSC 495',
    'CSC 529',
    'CSC 555',
    'CSC 575',
    'CSC 578',
    'CSC 594',
    'CSC 598',
    'CSC 672',
    'ECT 584',
    'IS 467'
]

# Database Systems focus
db_systems = [
    'CSC 433',
    'CSC 452',
    'CSC 454',
    'CSC 478',
    'CSC 529',
    'CSC 543',
    'CSC 549',
    'CSC 551',
    'CSC 553',
    'CSC 554',
    'CSC 555',
    'CSC 575',
    'CSC 589'
]

# Artifcial Intelligence focus
ai = [
    'CSC 457',
    'CSC 458',
    'CSC 478',
    'CSC 480',
    'CSC 481',
    'CSC 482',
    'CSC 495',
    'CSC 528',
    'CSC 529',
    'CSC 538',
    'CSC 575',
    'CSC 576',
    'CSC 577',
    'CSC 578',
    'CSC 583',
    'CSC 587',
    'CSC 592',
    'CSC 594',
    'ECT 584',
    'GEO 441',
    'GEO 442',
    'IS 467'
]

# Software Engineering focus
se = [
    'SE 430',
    'SE 433',
    'SE 441',
    'SE 452',
    'SE 453',
    'SE 456',
    'SE 457',
    'SE 459',
    'SE 475',
    'SE 477',
    'SE 480',
    'SE 482',
    'SE 491',
    'SE 525',
    'SE 526',
    'SE 529',
    'SE 533',
    'SE 546',
    'SE 549',
    'SE 554',
    'SE 556',
    'SE 560',
    'SE 579',
    'SE 581',
    'SE 582',
    'SE 591'
]

# Game and real-time systems focus
game_rt_sys = [
    'CSC 461',
    'CSC 462',
    'CSC 486',
    'CSC 588',
    'GAM 425',
    'GAM 450',
    'GAM 453',
    'GAM 470',
    'GAM 475',
    'GAM 476',
    'GAM 486',
    'GAM 575',
    'GAM 576',
    'GAM 690',
    'GAM 691',
    'GPH 436',
    'GPH 469',
    'GPH 570',
    'GPH 572',
    'GPH 580',
    'SE 456'
]

# Human computer interaction
hci = [
    'CSC 436',
    'CSC 438',
    'CSC 465',
    'CSC 471',
    'CSC 472',
    'CSC 491',
    'CSC 492',
    'HCI 440',
    'HCI 441',
    'HCI 430',
    'HCI 454'
]

# Research and these options
#   These can be subbed in any focus

thesis_opts = [
    'CSC 695',
    'CSC 698',
    'CSC 697'
]

####################
# IS requirements  #
####################

is_foundation = 'IS 421 and CSC 451 and IS 422 and IS 430 and IS 577'

# Every IS concentration has slightly different Advanced requirements
is_ba_adv = 'CNS 440 and IS 435 and IS 485 and IS 535 and IS 560'
is_bi_adv = 'IS 574 and CSC 423 and IS 549 and (IT 411 or CSC 401) and IT 403'
is_dba_adv = 'IS 549 and CSC 454 and CSC 452 and CSC 554 and (IT 411 or CSC 401)'
is_ent_adv = 'ECT 424 and IS 556 and IS 570 and IS 535'
is_standard_adv = ''

# Business Analysis - take 2
bus_analysis = [
    'ECT 424',
    'IS 444',
    'ECT 480',
    'IS 483',
    'HCI 440',
    'IS 431',
    'IS 440',
    'IS 455',
    'IS 540',
    'IS 556',
    'IS 565',
    'IS 578'
]

# take 3
bus_intel = [
    'CSC 424',
    'CSC 465',
    'CSC 495',
    'CSC 575',
    'GEO 441',
    'HCI 512',
    'ECT 584',
    'IPD 447',
    'IPD 451',
    'IPD 460',
    'IS 452',
    'IS 456',
    'IS 536',
    'IS 550'
]

# take 3
db_admin = [
    'CNS 440',
    'IPD 447',
    'IPD 451',
    'IPD 460',
    'IPD 463',
    'IS 452',
    'IS 505',
    'IS 536',
    'IS 550'
]

# take 3
it_enterprise = [
    'CNS 440',
    'ECT 556',
    'IS 440',
    'IS 444',
    'IS 482',
    'IS 483',
    'IS 500',
    'IS 505',
    'IS 506',
    'IS 535',
    'IS 536',
    'IS 540',
    'IS 550',
    'IS 560',
    'IS 565',
    'IS 579',
    'IS 580'
]

# standard focus just takes 7 from the other focus lists.
standard = []

# Graduation requirements for a masters in CS:
#   Take all introductory and foundation courses (or equivalent credit already completed)
#   For a given focus:
#     Take 4 electives from that focus
#     Take 4 electives from other focuses (excluding the main focus)
#     Students can optionally sub any of the thesis opts for focus reqs
#   Complete a minimum of 52 credit hours (13 courses)

from dpwebsite.core.rule_parser import RuleParser as rp

class Major():
    CS = 0
    IS = 1

# This is a simple enum to allow indexing into an array of focuses
class CSFocus():
    SW_SYSTEMS_DEV = 0
    THEORY = 1
    DATA_SCIENCE = 2
    DATABASE_SYSTEMS = 3
    AI = 4
    SW_ENGINEERING = 5
    GAME = 6
    HCI = 7

class ISFocus():
    BUSINESS_ANALYSIS = 0
    BUSINESS_INTEL = 1
    DB_ADMIN = 2
    IT_ENTERPRISE = 3
    STANDARD = 4

cs_focuses = [sw_sys_dev, theory, data_science, db_systems, ai, se, game_rt_sys, hci]

is_focuses = [bus_analysis, bus_intel, db_admin, it_enterprise, standard]

major_focus_lists = [cs_focuses, is_focuses]

cs_base = cs_introductory + ' and ' + cs_foundation

is_base = is_foundation

is_adv = [is_ba_adv, is_bi_adv, is_dba_adv, is_ent_adv, is_standard_adv]

major_base_courses = [cs_base, is_base]

def build_rule(major, focus_index):
    if major == Major.CS:
        return cs_build_rule(focus_index)
    elif major == Major.IS:
        return is_build_rule(focus_index)

# focus is a value from CSFocus
def cs_build_rule(focus_index):
    try:
        int(focus_index)
    except ValueError:
        print("graduation.build_rule: focus wasn't an int")
    
    grad_rule = ''
    grad_rule += cs_introductory + ' and '
    grad_rule += cs_foundation + ' '

    # add the req for the selected focus
    # The syntax for minimum n of list is ~n(item1, item2, ...etc)
    grad_rule += 'and ~4('

    # it doesn't matter if there's an extra comma at the end
    for course in cs_focuses[focus_index]:
        grad_rule += course + ','

    grad_rule += ') '

    # take 4 other electives
    grad_rule += 'and ~4('

    for i in range(len(cs_focuses)):
        if i != focus_index:
            for course in cs_focuses[i]:
                grad_rule += course + ','

    for opt in thesis_opts:
        grad_rule += opt + ','

    grad_rule += ') '

    # total courses requirement
    grad_rule += ' and ~13'

    # print(grad_rule)

    return rp.parse(grad_rule)

def is_build_rule(focus_index):
    try:
        int(focus_index)
    except ValueError:
        print("graduation.build_rule: focus wasn't an int")
    
    grad_rule = is_base

    if focus_index != ISFocus.STANDARD:
        grad_rule += ' and ' + is_adv[focus_index]

    elective_amount = 0
    if focus_index == ISFocus.BUSINESS_ANALYSIS:
        elective_amount = 3
    elif focus_index == ISFocus.STANDARD:
        elective_amount = 8
    else:
        elective_amount = 4

    grad_rule += ' and ~{}('.format(elective_amount)

    for i in range(len(is_focuses)):
        if i != focus_index:
            for course in is_focuses[i]:
                grad_rule += course + ','
    
    grad_rule += ')'

    # total courses req
    grad_rule += ' and ~13'

    # print(grad_rule)

    return rp.parse(grad_rule)

    

    

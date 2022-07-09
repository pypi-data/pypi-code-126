import copy
from .time_slots import *


def update_remaining_slots(set, depth):
    must_be_children = [] # Init list of courses that must be mapped to child node time slots
    for course in set:
        course = copy.deepcopy(course) # deepcopy so remaining slots remain the same for this course on other branches
        if course.remaining_slots == -1: 
            # first time seeing course, initialize value for how many more time slots (child nodes) are required
            if (depth <= LAST_SCHEDULABLE_TWF_SLOT): course.remaining_slots = 1 # TWF: requires 2 30 minutes slots, 1 remaining after this node
            elif (LAST_TWF_SLOT <= depth <= LAST_SCHEDULABLE_MTH_SLOT): course.remaining_slots = 2 # MTH: requires 3 30 minutes slots, 2 remaining after this node
        else:
            course.remaining_slots = course.remaining_slots - 1 # decrease remaining time slots by one to account for this node
        if course.remaining_slots > 0:
            must_be_children.append(course) # add to must_be_children list if course requires more time slots
                                            # this course will be in all child node course sets
    # Return list of courses that must be included in child node sets
    return must_be_children



# Method removes all courses in the list 'set' from the list 'unaccounted_courses'
def update_unaccounted_courses(unaccounted_courses, set):
    for course in set:
        for unaccounted_course in unaccounted_courses:
            if unaccounted_course.name == course.name:
                unaccounted_courses.remove(unaccounted_course)
    return unaccounted_courses



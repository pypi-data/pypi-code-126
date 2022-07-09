from treelib import Tree, Node                                      # Library for tree data structure 
from .course_list import *       # Defines list of courses to schedule
from .course_subsets import *    # Provides function for generating non-conflicting sets of courses
from .update_node import *       # Provides functions for updating remaining time slots in courses and updating lists of unaccounted courses
from .time_slots import *        # Defines list of time slots
from .bounding import *          # Provides functions for calculation upper and lower bounds
from .format_schedule import *   # Provides functions for formating the schedule list and printing its data
from time import *
import copy


def assign_time_slots(course_list):
    # Init tree data structure
    tree = Tree()

    # Init best lower bound
    best_lower_bound = 0

    best_score = 0      # highest score of node with all courses in branch scheduled
    best_index = 0      # index of node with all courses in branch scheduled with highest score

    # Get all subsets of all non-conflicting courses
    all_subsets = get_subsets(course_list, [], 0)
    subsets = all_subsets

    # Add root to tree and node list
    node_list = [tree.create_node(tag="Root", identifier=0, data=[-1, [], course_list, 0, 0]) ]
    node = node_list[0]

    # Init depth and index variables for each node
    depth = 0
    node_index = 1


    # while there are still possible child nodes to create and their depth does not surpass the # of time slots
    while(len(node_list)>0 and depth<=len(timeslots)):
        # Iterate subsets of non-conflicting courses that can be mapped to the time slot (depth) in the current branch
        for set in subsets:
            
            # Get child node depth (time slot #) by incrementing current node depth
            depth = node.data[0] + 1
            # only continue if there are enough time slots for this depth
            if(depth<LAST_MTH_SLOT):

                # Remove any course in current set from list of unaccounted courses
                unaccounted_courses = copy.deepcopy(node.data[2]) # Get current list of unaccounted courses from node
                unaccounted_courses = update_unaccounted_courses(unaccounted_courses, set) # Update list for child node

                # Get node score of parent node
                score = node.data[4]
                # Add time slot score for each score in current subset to score
                for course in set:
                    score += course.get_score(depth)
                
                # Get upper and lower bounds
                UB = score + get_max_scores(unaccounted_courses)
                LB = score + get_min_scores(unaccounted_courses)

                # Only create child node if best possible score is better then least worst case
                if(UB >= best_lower_bound):

                    # Update best lower bound if LB is greater
                    if LB > best_lower_bound:
                        best_lower_bound = LB

                    # Update each course's # of remaining slots property, get list of courses that have remaining time slots
                    child_node_courses = update_remaining_slots(set, depth)

                    # Check if all courses have been scheduled (for full duration) in branch
                    all_courses_allocated = False
                    if len(unaccounted_courses)==0 and len(child_node_courses)==0:
                        all_courses_allocated = True
                        for course in set:
                            if course.remaining_slots>0: 
                                all_courses_allocated = False # update to false if any courses still require more time slots

                    # Save index if the score is the highest score and all courses have been scheduled in branch
                    if score > best_score and all_courses_allocated:
                        best_score = score
                        best_index = node_index

                    # Make a node name
                    node_name = ""
                    for course in set:
                        node_name += course.name + " " + "|rem.: " + str(course.remaining_slots)
                    node_name += "|depth: " + str(depth) + "|score: " + str(score)
                    if all_courses_allocated:
                        node_name += "|complete"

                    # Add child node to tree and to list of nodes to expand
                    node_list.append(tree.create_node(tag=node_name, identifier=node_index, data=[depth, set, unaccounted_courses, child_node_courses, score], parent=node.identifier))
                    node_index += 1

        # Remove node from list of nodes to expand
        node_list.remove(node)
        if(len(node_list)==0):
            break # break if there are no more nodes to expand

        # Toggle brute force vs branch and bound
        brute_force = False
        if (brute_force):
            # First just try getting the highest scoring child node
            max_node = Node(data=[-1, -1, -1, -1, -1])
            for n in tree.children(node.identifier):
                if (n.data[4] > max_node.data[4]):
                    max_node = n
            node = max_node
        else:
            # Get node with highest score from node list to expand
            node = node_list[0]
            for n in node_list:
                if n.data[4] > node.data[4]:
                    node = n

        must_include = node.data[3] # courses in node set that require more time slots (must be included in all child nodes)
        depth = node.data[0] + 1
        # only consider unaccounted courses if there is enough time slots left in day to fit it in:
        if(LAST_SCHEDULABLE_TWF_SLOT < depth <= LAST_TWF_SLOT):
            subsets = get_subsets(must_include, [], depth)

        elif(LAST_SCHEDULABLE_MTH_SLOT < depth <= LAST_MTH_SLOT):
            subsets = get_subsets(must_include, [], depth)

        else:
            unaccounted = node.data[2] # courses not yet scheduled in branch
            # get all non-conflicting subsets of unaccounted courses that contain all courses in must_include
            subsets = get_subsets(unaccounted, must_include, depth)


    #tree.show()
    #print("best score: ", best_score)

    # Format schedule
    format_schedule(tree, best_index)



def assign_times(course_list, input_json):

    # remove courses with no prof from course_list
    index = 0
    while(index < len(course_list)):
        course = course_list[index]
        if course.prof is None:
            course_list.remove(course)
        else:
            index += 1

    print(f"Found {len(course_list)} courses to assign to timeslots")

    # print input list of course objects
    '''print("list:")
    for course in course_list:
        print("\r")
        print("course: ", course.name)
        print("semester:", course.semester)
        print("prof: ", course.prof)
        print("time slot scores: ", course.score_list, "}")
        print("\r")'''

    start_time = time()
    assign_time_slots(course_list) # run course to time slots branch and bound
    end_time = time()

    # Print schedule
    # print_schedule()

    print("assigned slots in: ", end_time - start_time)

    return format_output(input_json)
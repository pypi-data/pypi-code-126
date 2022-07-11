
# Input: set = list of courses to create non-conflicting subsets for
#        must_include_list = list of courses that must be included in every subset
# Output: list of all non-conflicting subsets. Eact subset contains every course in must_include_list.
# Return type: list of lists, inner lists can be empty or contain any number of course objects
def get_subsets(set, must_include_list, depth):
    # Check if empty set
    if set == []:
        return [must_include_list + []]
    # Get subsets of all elements in set excluding first
    curr_subsets = get_subsets(set[1:], must_include_list, depth)
    
    new_set = []        # List to contain new subsets (containing existing subsets joined with the first element in set
    conflict = False    # Var to check for conflicts between existing subset and first element of set

    for subset in curr_subsets:
        # Check if conflict (scheduled for same semester in reccommended schedule)
        for course in subset:
            if course.semester_conflict(set[0]):
                conflict = True
            elif course.prof_conflict(set[0]):
                conflict = True

        # Add course to new subset only if no courses in the subset conflict
        if not conflict:
            new_set.append([set[0]] + subset)
        
        conflict = False # Reset to check next subset

    # Return existing subsets concatenated with new subsets
    return curr_subsets + new_set
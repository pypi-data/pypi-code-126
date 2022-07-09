
# Init best lower bound
best_lower_bound = 0


# Returns the summation of the maximum time slot scores for each course in given set
def get_max_scores(set):
    max_scores = 0
    for course in set:
        max_scores += course.max_score
    return max_scores


# Returns the summation of the minimum time slot scores for each course in given set
def get_min_scores(set):
    min_scores = 0
    for course in set:
        min_scores += course.min_score
    return min_scores



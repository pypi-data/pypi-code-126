import json
from textwrap import indent

class Course:
 
    # constructor
    def __init__(self, name, semester, prof, time_slot_scores, season):
        self.name = name
        self.semester = semester
        self.prof = prof
        self.score_list = time_slot_scores  # Must be list with size = # time slots
                                            # Each value must be between // figure this out
        self.season = season
        self.remaining_slots = -1
        # Get maximum time slot score (calculating max score property once to speed up upper bound calculation)
        self.max_score = 0
        #(json.dumps((self.name, self.semester, self.prof, self.score_list), indent=2))
        for score in self.score_list:
            if score > self.max_score: self.max_score = score
        # Get minimum time slot score (calculating max score property once to speed up lower bound calculation)
        self.min_score = self.max_score
        for score in self.score_list:
            if score < self.min_score: self.min_score = score
        #print(json.dumps((self.name, self.semester, self.prof, self.score_list, self.min_score, self.max_score), indent=2))
        
        

    # Method returns True if the semesters (recommended program) are the same
    def semester_conflict(self, other_course):
        if other_course.semester == self.semester:   
            return True
        else:
            return False

    # Method returns True if the assigned professor is the same
    def prof_conflict(self, other_course):
        if other_course.prof == self.prof:   
            return True
        else:
            return False

    # Method returns the score for a time slot given it's index
    def get_score(self, time_slot_index):
        return self.score_list[time_slot_index]



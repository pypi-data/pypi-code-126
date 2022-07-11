import json, csv, datetime
from sqlite3 import complete_statement
from xml.dom import InuseAttributeErr
from .course import Course


# Functions takes a list of integers as input. If all integers in the list are zero, a list of the same size containing all ones is returned. Otherwise, the original list is returned
def ensure_non_zeros(score_list):
    all_zeros = True
    for score in score_list:
        if score!=0:
            all_zeros = False
    if all_zeros:
        for score_index in range(len(score_list)):
            score_list[score_index] = 1
    return score_list


def generate_course_list(courses_and_profs):
    obj = get_ppw()

    complete_list = []

    fall_list = []
    spring_list = []
    summer_list = []
    
    for current_semester in courses_and_profs['schedule']:
        for course in courses_and_profs['schedule'][current_semester]:

           course_name = course['course']['code']
           if (course_name not in obj):
               continue
           sem = (obj[course_name]['OnstreamSemester'])
           season = current_semester

           prof = course['sections'][0]['professor']
           if (prof is not None):
               prof = prof['id']

           pref_timeslots = {}
           time_scores = []

           for instructor in courses_and_profs['professors']:
               if prof is instructor['id']:
                
                #    Generate List of PROF Preferences over 27 30minute

                    monday_thursday = [0] * 27
                    tuesday_wednesday_friday = [0] * 27


                    if (current_semester in instructor['preferredTimes']):
                        for day in instructor['preferredTimes'][current_semester]:
                            curr_day_slots = [0] * 27
    
                            for times in instructor['preferredTimes'][current_semester][day]:

                                start_time = datetime.datetime.strptime(str(times[0]), "%H:%M")
                                end_time = datetime.datetime.strptime(str(times[1]), "%H:%M")
                                base_time = datetime.datetime(1900, 1, 1)

                                # Converting Start Time / End Time into index 

                                min_to_start = (start_time - base_time).total_seconds() / 60 
                                min_to_end = (end_time - base_time).total_seconds() / 60 

                                # Subtract BASE Minutes (830 AM = 510minutes, divide by 30 to get starting index)
                                starting_index = int((min_to_start - 510) / 30)

                                # Subtract BASE Minutes by 500 (As END TIME IS NOT a multiple of 30 (10 minutes less) and divide by 30 to get ending index)
                                ending_index= int((min_to_end - 500) / 30)

                                for i in range(starting_index, ending_index):

                                    curr_day_slots[i] = 1

                                    if day == 'monday' or day == 'thursday':
                                        monday_thursday[i] = monday_thursday[i] + 1

                                    if day == 'tuesday' or day == 'wednesday' or  day =='friday':
                                        tuesday_wednesday_friday[i] = tuesday_wednesday_friday[i] + 1
                                
                                pref_timeslots[day] = curr_day_slots

                    pref_timeslots['monday_thursday'] = monday_thursday
                    pref_timeslots['tuesday_wednesday_friday'] = tuesday_wednesday_friday
                    time_scores = tuesday_wednesday_friday + monday_thursday

           complete_list.append(Course(course_name, sem, prof, time_scores, season))

           time_scores = ensure_non_zeros(time_scores)

           if current_semester=="fall":
               fall_list.append(Course(course_name, sem, prof, time_scores, season))
           elif current_semester=="spring":
               spring_list.append(Course(course_name, sem, prof, time_scores, season))
           if current_semester=="summer":
               summer_list.append(Course(course_name, sem, prof, time_scores, season))

    return [complete_list, fall_list, spring_list, summer_list]

def get_ppw():
    ppw = {
            "CSC111" : {
                "CourseID" : "CSC111",
                "CourseName" : "Fundamentals of Programming with Engineering Applications",
                "OnstreamSemester" : "1A",
                "OfferedIn" : "F,Sp",
                "Capacity" : 120
            },
            "ENGR110" : {
                "CourseID" : "ENGR110",
                "CourseName" : "Design & Communication I",
                "OnstreamSemester" : "1A",
                "OfferedIn" : "F",
                "Capacity" : 120
            },
            "ENGR130" : {
                "CourseID" : "ENGR130",
                "CourseName" : "Introduction to Professional Practice",
                "OnstreamSemester" : "1A",
                "OfferedIn" : "F,Sp",
                "Capacity" : 120
            },
            "MATH100" : {
                "CourseID" : "MATH100",
                "CourseName" : "Calculus I",
                "OnstreamSemester" : "1A",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },
            "MATH110" : {
                "CourseID" : "MATH110",
                "CourseName" : "Matrix Algebra for Engineers",
                "OnstreamSemester" : "1A",
                "OfferedIn" : "F",
                "Capacity" : 120
            },
            "PHYS110" : {
                "CourseID" : "PHYS110",
                "CourseName" : "Introductory Physics I",
                "OnstreamSemester" : "1A",
                "OfferedIn" : "F,Sp",
                "Capacity" : 120
            },

            "CSC115" : { 
                "CourseID" : "CSC115",
                "CourseName" : "Fundamentals of Prograaming: II",
                "OnstreamSemester" : "1B",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "ENGR120" : {
                "CourseID" : "ENGR120",
                "CourseName" : "Design & Communication II",
                "OnstreamSemester" : "1B",
                "OfferedIn" : "Sp",
                "Capacity" : 120
            },

            "ENGR141" : {
                "CourseID" : "ENGR141",
                "CourseName" : "Engineering Mechanics - Statics & Dynamics",
                "OnstreamSemester" : "1B",
                "OfferedIn" : "Sp,Su",
                "Capacity" : 120
            },

            "MATH101" : {
                "CourseID" : "MATH101",
                "CourseName" : "Integral Calculus with Applications",
                "OnstreamSemester" : "1B",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "PHYS111" : {
                "CourseID" : "PHYS111",
                "CourseName" : "Introductory Physics II",
                "OnstreamSemester" : "1B",
                "OfferedIn" : "Sp,Su",
                "Capacity" : 120
            },

            "CSC230" : {
                "CourseID" : "CSC230",
                "CourseName" : "Introduction to Computer Architecture",
                "OnstreamSemester" : "2A",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "CHEM101" : {
                "CourseID" : "CHEM101",
                "CourseName" : "Fundamentals of Chemistry from Atoms to Materials",
                "OnstreamSemester" : "2A",
                "OfferedIn" : "F,Su",
                "Capacity" : 120
            },

            "ECE260" : {
                "CourseID" : "ECE260",
                "CourseName" : "Continuous-Time Signals & Systems",
                "OnstreamSemester" : "2A",
                "OfferedIn" : "F,Su",
                "Capacity" : 120
            },

            "MATH122" : {
                "CourseID" : "MATH122",
                "CourseName" : "Logic & Foundations",
                "OnstreamSemester" : "2A",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "SENG265" : {
                "CourseID" : "SENG265",
                "CourseName" : "Software Development Methods",
                "OnstreamSemester" : "2A",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "STAT260" : {
                "CourseID" : "STAT260",
                "CourseName" : "Introduction to Probability & Statistics",
                "OnstreamSemester" : "2A",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "CSC225" : {
                "CourseID" : "CSC225",
                "CourseName" : "Algorithms & Data Structures I",
                "OnstreamSemester" : "2B",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "ECE310" : {
                "CourseID" : "ECE310",
                "CourseName" : "Digital Signal Processing I",
                "OnstreamSemester" : "2B",
                "OfferedIn" : "Sp,Su",
                "Capacity" : 120
            },

            "ECON180" : {
                "CourseID" : "ECON180",
                "CourseName" : "Introduction to Principles of Micro Economics",
                "OnstreamSemester" : "2B",
                "OfferedIn" : "F,Su",
                "Capacity" : 120
            },

            "SENG275" : {
                "CourseID" : "SENG275",
                "CourseName" : "Software Testing",
                "OnstreamSemester" : "2B",
                "OfferedIn" : "Sp,Su",
                "Capacity" : 120
            },

            "SENG310" : {
                "CourseID" : "SENG310",
                "CourseName" : "Human Computer Interaction",
                "OnstreamSemester" : "2B",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "ECE458" : {
                "CourseID" : "ECE458",
                "CourseName" : "Communication Networks",
                "OnstreamSemester" : "3A",
                "OfferedIn" : "Sp",
                "Capacity" : 120
            },

            "CSC226" : {
                "CourseID" : "CSC226",
                "CourseName" : "Algorithms & Data Structues II",
                "OnstreamSemester" : "3A",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "ECE360" : {
                "CourseID" : "ECE360",
                "CourseName" : "Control Theory & Systems",
                "OnstreamSemester" : "3B",
                "OfferedIn" : "F,Sp",
                "Capacity" : 120
            },

            "SENG321" : {
                "CourseID" : "SENG321",
                "CourseName" : "Requirements Engineering",
                "OnstreamSemester" : "3A",
                "OfferedIn" : "F,Sp",
                "Capacity" : 120
            },

            "SENG371" : {
                "CourseID" : "SENG371",
                "CourseName" : "Software Evolution",
                "OnstreamSemester" : "3A",
                "OfferedIn" : "Sp",
                "Capacity" : 120
            },

            "ECE355" : {
                "CourseID" : "ECE355",
                "CourseName" : "Microprocessor-Based Systems",
                "OnstreamSemester" : "3B",
                "OfferedIn" : "F",
                "Capacity" : 120
            },

            "CSC320" : {
                "CourseID" : "CSC320",
                "CourseName" : "Foundations of Computer Science",
                "OnstreamSemester" : "3B",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "CSC360" : {
                "CourseID" : "CSC360",
                "CourseName" : "Operating Systems",
                "OnstreamSemester" : "3B",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "CSC370" : {
                "CourseID" : "CSC370",
                "CourseName" : "Database Systems",
                "OnstreamSemester" : "3B",
                "OfferedIn" : "F,Sp,Su",
                "Capacity" : 120
            },

            "SENG350" : {
                "CourseID" : "SENG350",
                "CourseName" : "Software Architecture & Design",
                "OnstreamSemester" : "3B",
                "OfferedIn" : "F",
                "Capacity" : 120
            },

            "SENG360" : {
                "CourseID" : "SENG360",
                "CourseName" : "Security Engineering",
                "OnstreamSemester" : "3B",
                "OfferedIn" : "F",
                "Capacity" : 120
            },

            "SENG426" : {
                "CourseID" : "SENG426",
                "CourseName" : "Software Quality Engineering",
                "OnstreamSemester" : "4A",
                "OfferedIn" : "Su",
                "Capacity" : 120
            },

            "SENG440" : {
                "CourseID" : "SENG440",
                "CourseName" : "Embedded Systems",
                "OnstreamSemester" : "4A",
                "OfferedIn" : "Su",
                "Capacity" : 120
            },

            "SENG499" : {
                "CourseID" : "SENG499",
                "CourseName" : "Design Project II",
                "OnstreamSemester" : "4A",
                "OfferedIn" : "Su",
                "Capacity" : 120
            },

            "ECE455" : {
                "CourseID" : "ECE455",
                "CourseName" : "Real Time Computer System Design",
                "OnstreamSemester" : "4B",
                "OfferedIn" : "Sp",
                "Capacity" : 120
            },

            "SENG401" : {
                "CourseID" : "SENG401",
                "CourseName" : "Social & Professional Issues",
                "OnstreamSemester" : "4B",
                "OfferedIn" : "Sp",
                "Capacity" : 120
            }

        }
    return ppw

           
           



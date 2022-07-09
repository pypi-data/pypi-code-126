import json, csv, datetime
from sqlite3 import complete_statement
from xml.dom import InuseAttributeErr
from .course import Course


def generate_course_list(courses_and_profs):
    with open("./c1algo1/data/input/SENG_PPW.json", "r") as fh:
        obj = json.load(fh)

    complete_list = []
    
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

    return complete_list

           
           



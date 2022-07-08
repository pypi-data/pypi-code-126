import json
import string
import numpy as np
import copy
import bz2
from os.path import exists

from c1algo2.InputProcessor import DataProcessor
from c1algo2.InputProcessor.ConfigThings import *
from c1algo2.InputProcessor import Helper as Helper

def parse_input(backend_input_data: dict, progression_data: dict) -> dict:
    # Outermost: Dictionary, where keys are courses e.g. "CSC111" and values are dicts.
    # Each dict within a course contains the following structure:
    # {
    #   "CSCS111": {
    #       "2008": 
    #           {
    #               "1": 10,
    #               "2": 10,
    #               "2T": 10,
    #               "3": 10,
    #               "4": 10,
    #               "5": 10,
    #               "6": 10,
    #               "7": 10,
    #               "Fall Enrolment": 50,
    #               "Fall Maximum Enrolment": 60,
    #               "Spring Enrolment": 50,
    #               "Spring Maximum Enrolment": 60,
    #               "Summer Enrolment": 50,
    #               "Summer Maximum Enrolment": 60,
    #               "Year Enrolment": 50,
    #               "Year Maximum Enrolment": 60,
    #           }
    #   }
    # }
    # course{year{term{section{}}}}

    final_input = {}

    for course in backend_input_data:
        offering = course["subjectCourse"]
        year = course["term"][0:4]

        # if the course is already in the dictionary, just append data to that key
        if offering in final_input:

            if year in final_input[offering]:

                if year in progression_data:
                    final_input[offering][year].update(progression_data[year])
                else:
                    # add manually
                    final_input[offering][year].update(null_progression())

                if(course['term'].endswith('09')): # fall
                    final_input[offering][year].setdefault("Fall_Enrollment", 0)
                    final_input[offering][year].setdefault("Fall_MaxEnrollment", 0)
                    final_input[offering][year]["Fall_Enrollment"] += course["enrollment"]
                    final_input[offering][year]["Fall_MaxEnrollment"] += course["maximumEnrollment"]
                    
                if(course['term'].endswith('01')): # spring
                    final_input[offering][year].setdefault("Spring_Enrollment", 0)
                    final_input[offering][year].setdefault("Spring_MaxEnrollment", 0)
                    final_input[offering][year]["Spring_Enrollment"] += course["enrollment"]
                    final_input[offering][year]["Spring_MaxEnrollment"] += course["maximumEnrollment"]
                   
                if(course['term'].endswith('05')): # summer
                    final_input[offering][year].setdefault("Summer_Enrollment", 0)
                    final_input[offering][year].setdefault("Summer_MaxEnrollment", 0)
                    final_input[offering][year]["Summer_Enrollment"] += course["enrollment"]
                    final_input[offering][year]["Summer_MaxEnrollment"] += course["maximumEnrollment"]
                    
                
            else:
                new_year = {}
                final_input[offering][year] = new_year
                # final_input[offering]
                if year in progression_data:
                    final_input[offering][year].update(progression_data[year])
                else:
                    # add manually
                    final_input[offering][year].update(null_progression())

                if(course['term'].endswith('09')): # fall
                    new_year["Fall_Enrollment"] = course["enrollment"]
                    new_year["Fall_MaxEnrollment"] = course["maximumEnrollment"]
                    
                if(course['term'].endswith('01')): # spring
                    new_year["Spring_Enrollment"] = course["enrollment"]
                    new_year["Spring_MaxEnrollment"] = course["maximumEnrollment"]
                if(course['term'].endswith('05')): # summer
                    new_year["Summer_Enrollment"] = course["enrollment"]
                    new_year["Summer_MaxEnrollment"] = course["maximumEnrollment"]

                final_input[offering][year] = new_year
                
                
        # if the course is new, add as a new key
        else:
            
            final_input[course["subjectCourse"]] = {course["term"][0:4]: {}}
            year = course["term"][0:4]
            
            new_year = {}
            
            #final_input[course['subjectCourse']][year].update(null_progression())
            if(course['term'].endswith('09')): # fall
                new_year["Fall_Enrollment"] = course["enrollment"]
                new_year["Fall_MaxEnrollment"] = course["maximumEnrollment"]
            if(course['term'].endswith('01')): # spring
                new_year["Spring_Enrollment"] = course["enrollment"]
                new_year["Spring_MaxEnrollment"] = course["maximumEnrollment"]
            if(course['term'].endswith('05')): # summer
                new_year["Summer_Enrollment"] = course["enrollment"]
                new_year["Summer_MaxEnrollment"] = course["maximumEnrollment"]

            final_input[course['subjectCourse']][year] = new_year
            final_input[course['subjectCourse']][year].update(null_progression())

    return final_input

def null_progression() -> dict:
    empty_data = {
        "1": 0,
        "2": 0,
        "2T": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0
    }
    return empty_data

def model_1_output(input_file: dict) -> dict:

    # use deepcopy to change iterable objects in the dictionary
    result = copy.deepcopy(input_file)
    for course in result:
        for year in result[course]:

            result[course][year]["Year_Enrollment"] = 0
            result[course][year]["Year_MaxEnrollment"] = 0

            if "Fall_Enrollment" in result[course][year]:
                result[course][year]["Year_Enrollment"] += result[course][year]["Fall_Enrollment"]
                result[course][year]["Year_MaxEnrollment"] += result[course][year]["Fall_MaxEnrollment"]
                result[course][year].pop("Fall_Enrollment")
                result[course][year].pop("Fall_MaxEnrollment")
            if "Spring_Enrollment" in result[course][year]:
                result[course][year]["Year_Enrollment"] += result[course][year]["Spring_Enrollment"]
                result[course][year]["Year_MaxEnrollment"] += result[course][year]["Spring_MaxEnrollment"]
                result[course][year].pop("Spring_Enrollment")
                result[course][year].pop("Spring_MaxEnrollment")
            if "Summer_Enrollment" in result[course][year]:
                result[course][year]["Year_Enrollment"] += result[course][year]["Summer_Enrollment"]
                result[course][year]["Year_MaxEnrollment"] += result[course][year]["Summer_MaxEnrollment"]
                result[course][year].pop("Summer_Enrollment")
                result[course][year].pop("Summer_MaxEnrollment")
    return result

def parse_output_for_backend(predictor_output: dict, dummy: bool) -> dict:
    # predictor_output:
    #
    # Outermost: Dictionary, where keys are courses e.g. "CSC111" and values are lists of numpy arrays.
    # Each list contains 3 numpy arrays with values(capacities for all sections): Fall Maximum Enrolment, Spring Maximum Enrolment, Summer Maximum Enrolment.
    # Example: {"CSC111": [[150], [100], [80]], "CSC115": [[250], [200], [150]], "MATH100": [[250, 250, 250], [80, 80], [70]]....}
    #
    # Return Value:
    # Refer to Data Model.

    if(dummy):
        Helper.decompress_file('Output/dummy_out.json.bz2', 'Output/dummy_out.json')
        file = open('Output/dummy_out.json', 'r')
        dummy_output = json.load(file)
        print('returning dummy')
        return(dummy_output)
    
    fall_offerings = []
    spring_offerings = []
    summer_offerings = []
    first_year_copy = []

    if(exists(COMPRESSED_NON_CORE_FIRST_YEAR_PATH)):
        print("Extracting existing first year data ..")
        with open(NON_CORE_FIRST_YEAR_OUTPUT_PATH, 'wb') as new_file, bz2.BZ2File(COMPRESSED_NON_CORE_FIRST_YEAR_PATH, 'rb') as file:
            decompressor = bz2.BZ2Decompressor()
            for data in iter(lambda: file.read(100*1024), b''):
                new_file.write(data)

        data_file = open(NON_CORE_FIRST_YEAR_OUTPUT_PATH, 'r')
        first_year_copy = json.load(data_file)
    else:
        print("Getting fresh copy of first year data ..")
        first_year_copy = get_prev_year_course_data(2022)
    
    predictor_output.update(first_year_copy)
    core_course_titles = get_json(CORE_COURSES_INPUT_PATH)

    for key in predictor_output:
        value = predictor_output[key]
        if(key in core_course_titles):
            title = core_course_titles[key]['course_title']
        else:
            # TODO: get missing titles
            title = "dummy_title"
        
        # if value[0] is non-empty then the course sections contained there should be scheduled in the FALL semester.
        if value[0] != []: 
            fall_offerings.append(build_offering_dict(key, value[0], title))
        # if value[1] is non-empty then the course sections contained at there should be scheduled in the SPRING semester.
        if value[1] != []:
            spring_offerings.append(build_offering_dict(key, value[1], title))
        # if value[2] is non-empty then the course sections contained at there should be scheduled in the SUMMER semester.
        if value[2] != []:
            summer_offerings.append(build_offering_dict(key, value[2], title))

    print('Returning fomatted output')
    return {"fall": fall_offerings,
            "spring": spring_offerings,
            "summer": summer_offerings}

def build_offering_dict(course_code: string, sections: list, title: string) -> dict:
    offering_dict = {
        "course": {
            "code": course_code,
            "title": title,
            "pengRequired": False
        },
        "sections": []
    }
    for capacity in sections:
        offering_dict['sections'].append({
            "professor": None,
            "capacity": capacity,
            "timeSlots": None
        })
    
    return(offering_dict)

def get_prev_year_course_data(current_year):
    data_processor = DataProcessor.DataProcessor()
    complete_core_courses = data_processor.get_historical_clean_core_course_offerings()

    current_year = current_year - 1
    combined_dict = {}

    for course in complete_core_courses:
        if(course['courseNumber'][0] == '1' and course['subject'] != 'CSC' and course['subject'] != 'SENG'):
            if course['subjectCourse'] in combined_dict:
                if(course['term_year'] == str(current_year) and course['semester'] == '09'): # fall
                    combined_dict[course['subjectCourse']][0].append(course['maximumEnrollment'])
                if(course['term_year'] == str(current_year) and course['semester'] == '01'): # spring
                    combined_dict[course['subjectCourse']][1].append(course['maximumEnrollment'])
                if(course['term_year'] == str(current_year) and course['semester'] == '05'): # summer
                    combined_dict[course['subjectCourse']][2].append(course['maximumEnrollment'])
            else:
                if(course['term_year'] == str(current_year) and course['semester'] == '09'): # fall
                    combined_dict[course['subjectCourse']] = [[course['maximumEnrollment']],[],[]]
                if(course['term_year'] == str(current_year) and course['semester'] == '01'): # spring
                    combined_dict[course['subjectCourse']] = [[],[course['maximumEnrollment']],[]]
                if(course['term_year'] == str(current_year) and course['semester'] == '05'): # summer
                    combined_dict[course['subjectCourse']] = [[],[],[course['maximumEnrollment']]]

    return(combined_dict)

def main():
    dataprocessor = DataProcessor.DataProcessor()
    result = parse_output_for_backend({"CSC225": [[100], [150], []], "CSC226": [[100], [150], []], "SENG310": [[100], [150], [20]], "ECE310": [[100], [150], [60]]}, False)
    out_file = open("Output/final_out.json", "w")
    json.dump(result, out_file, indent=6)
    
     # open the JSON file with the cleaned up courses

    #decompress json file containing historical offerings from .bz file
    with open('InputProcessor/Input/Given_Input/banner_clean.json', 'wb') as new_file, bz2.BZ2File('InputProcessor/Input/Given_Input/banner_clean.json.bz2', 'rb') as file:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda: file.read(100*1024), b''):
            new_file.write(data)

    #decompress json file containing historical offerings from .bz file
    with open('InputProcessor/Input/Given_Input/progression_data.json', 'wb') as new_file, bz2.BZ2File('InputProcessor/Input/Given_Input/progression_data.json.bz2', 'rb') as file:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda: file.read(100*1024), b''):
            new_file.write(data)


    file = open("InputProcessor/Input/Given_Input/banner_clean.json",)
    backend_input = json.load(file)

    file = open("InputProcessor/Input/Given_Input/progression_data.json",)
    progression_data = json.load(file)
    sequence_input = parse_input(backend_input, progression_data)
    size_input = model_1_output(sequence_input)

    model_1_input = open("InputProcessor/Input/model_1_input.json", "w")
    json.dump(size_input, model_1_input, indent=6)

    model_2_input = open("InputProcessor/Input/model_2_input.json", "w")
    json.dump(sequence_input, model_2_input, indent=6)
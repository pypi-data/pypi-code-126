from inspect import CORO_SUSPENDED
import numpy as np
from sklearn.linear_model import LinearRegression
from c1algo2 import data
from c1algo2.InputProcessor import DataProcessor
import pickle

def create_model_inputs(hist_data, program_enrollment, schedule) -> tuple([dict, dict, list]):
    """creates DataProcessor Object which initializes model input data
    """
    data_processor = DataProcessor.DataProcessor()
    complete_historical_core_courses = data_processor.get_historical_clean_core_course_offerings()
    model_1_input, model_2_input = data_processor.get_historical_core_courses(complete_historical_core_courses)
    data_processor.print_model_1_input_to_json(model_1_input)
    data_processor.print_model_2_input_to_json(model_2_input)
    return model_1_input, model_2_input, data_processor.core_course_names

def create_model_1_input(model_1_input: dict) -> tuple([dict, dict]):
    """Creates Model_1_input (ALl Courses) Object which initializes formats model 1 input data
    """
    x_years = {}
    y_enrollments = {}
    for course in model_1_input:
        x_years[course], y_enrollments[course] = create_model_1_course(model_1_input[course])
    return x_years, y_enrollments

def create_model_1_course(course: dict) -> tuple([np.array, np.array]):
    """Creates Model_1_input (1 course) 
    """
    x_year = [] # x_year[i] = course[year].key()[ij] (year i, semester j)
    y_enrollment = [] # y_enrollment[i] = course[year][semester]["maximumEnrollment"]
    for i_year in course:
        x_year.append(int(i_year))
        y_enrollment.append(int(course[i_year]["Year_MaxEnrollment"]))
    x_year = np.array(x_year, dtype=np.int32).reshape(-1,1)
    y_enrollment = np.array(y_enrollment, dtype=np.int32)
    return x_year, y_enrollment

def create_model_2_input(model_2_input: dict) -> tuple([dict, dict]):
    """Creates Model_2_input (All courses) object which formats model 2 input per course
    """
    x = {}
    y = {}
    for course in model_2_input:
        x[course], y[course] = create_model_2_course(model_2_input[course])
    return x, y

def create_model_2_course(course: dict) -> tuple([np.array, np.array]):
    """creates Model_2_input (1 course)
    """
    x_year_enrollment = []
    y_semesters = []

    # We want to do a conversion so that course sequencing is grouped by academic year (September-August) than by absolute year
    for year in course:
        prev_year = str(int(year)-1)
        enrollment_for_year = 0
        enrollment = [0,0,0]
        if prev_year in course.keys():
            if "Fall_MaxEnrollment" in course[prev_year]:
                enrollment[0] = course[prev_year]["Fall_MaxEnrollment"]
                enrollment_for_year += course[prev_year]["Fall_MaxEnrollment"]
            if "Spring_MaxEnrollment" in course[year]:
                enrollment[1] = course[year]["Spring_MaxEnrollment"]
                enrollment_for_year += course[year]["Spring_MaxEnrollment"]
            if "Summer_MaxEnrollment" in course[year]:
                enrollment[2] = course[year]["Summer_MaxEnrollment"]
                enrollment_for_year += course[year]["Summer_MaxEnrollment"]

        x_year_enrollment.append([prev_year, enrollment_for_year])       # So, for example, if we're looking at the 2008-9 period, this will be 2008
        y_semesters.append(enrollment)
        
    x_year_enrollment = np.array(x_year_enrollment, dtype=np.int32)
    y_semesters = np.array(y_semesters, dtype=np.int32)
    return x_year_enrollment, y_semesters
    
def round_floats_to_ints(float_list: list) -> list:
    int_list = []
    for float_value in float_list:
        int_value = round(float_value)
        int_list.append(int_value)
    return int_list

def round_floats_to_ints_2(float_list_list: list) -> list:
    int_list_list = []
    for float_list in float_list_list:
        int_list = []
        for float_value in float_list:
            int_value = round(float_value)
            int_list.append(int_value)
        int_list_list.append(int_list)
    return int_list_list

def normalize_output(output):
    for course in output:
        max_value = max(output[course])
        # Remove negative values.
        output[course] = [max(0, i) for i in output[course]]
        # Remove all values lower than the square root of the max value. This
        # is to eliminate "close to 0 but not quite" errors. Potential errors
        # here: e.g. what if 5 students do a project in 1 semester, but only 1
        # in another?
        output[course] = [0 if i < max_value**(1/2) else i for i in output[course]]
        # Set values of 0 to None.
        output[course] = [None if i == 0 else i for i in output[course]]

def main():
    historical_data = pickle.load(open("InputProcessor/Input/Given_Input/historical_data", "rb"))
    previous_enrollment = pickle.load(open("InputProcessor/Input/Given_Input/previous_enrolment", "rb"))
    schedule = pickle.load(open("InputProcessor/Input/Given_Input/schedule", "rb"))

    result = forecast(historical_data, previous_enrollment, schedule)

def forecast(historical_data, previous_enrollment, schedule):
    verbose=True

    # model_2_inputs = data.parse_input(historical_data, previous_enrollment)
    # model_1_inputs = data.model_1_output(model_2_input)

    # model_1_inputs, model_2_inputs, core_course_names =  create_model_inputs(historical_data, previous_enrollment)
    # x_years, y_enrollments = create_model_1_input(model_1_inputs)
    # x_year_enrollment, y_semesters = create_model_2_input(model_2_inputs)

    sequencer_inputs = data.parse_input(historical_data, previous_enrollment)
    sizer_inputs = data.model_1_output(sequencer_inputs)

    courses = data.get_courses(schedule)
    
    sizer = LinearRegression()
    sequencer = LinearRegression()
    
    x_years, y_enrollments = create_model_1_input(sizer_inputs)
    x_year_enrollment, y_semesters = create_model_2_input(sequencer_inputs)
    
    outputDict = {}
    
    for course in courses:
        sizer.fit(x_years[course], y_enrollments[course])
        sequencer.fit(x_year_enrollment[course], y_semesters[course])
        r_sq_1 = sizer.score(x_years[course],y_enrollments[course])
        r_sq_2 = sequencer.score(x_year_enrollment[course], y_semesters[course])
        y1_pred_floats = sizer.predict(x_year_enrollment[course][:,0].reshape(-1,1))
        y1_pred = round_floats_to_ints(y1_pred_floats)
        x_2 = np.array([x_year_enrollment[course][:,0], y1_pred]).transpose()
        y2_pred_floats = sequencer.predict(x_2)
        y2_pred = round_floats_to_ints_2(y2_pred_floats)

        outputDict[course] = y2_pred[0]

        # if verbose:
        #     print("    **** "+ str(course) + " Predicted Sequencing ****")
        #     for input, pred in zip(x_year_enrollment[course],y2_pred):
        #         print("Year: " + str(int(input[0])) + "     Size: " + str(int(input[1])) + "    Prediction:" + str(pred))
    
    # output = data.parse_output_for_backend(
    #     # y2_pred to be in the format below or change output_for_backend to have y2_pred's format
    #     outputDict,
    #     schedule,
    #     dummy=False
    # )

    normalize_output(outputDict)

    schedule = data.fill_capacities(schedule, outputDict, 2022)

    print(outputDict)

    return schedule

if __name__ == "__main__":
    main()
import pandas
import matplotlib as plt
import numpy as np

pandas.set_option('display.max_columns', 500)
df = pandas.read_csv('uiuc-gpa-dataset.csv')
grade_data = df[['A+', 'A', 'A-', 'B+', 'B', 'B-', \
                 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']].values
course_title = df['Course Title'].values
subject = df[['Subject']].values
years = df['YearTerm'].values
instructor = df['Primary Instructor'].values
course_number = df['Number'].values


"""
calcGPA
inputs: grades- a list of ints length 12 ordered in A+, A..., F format
return value- the gpa for a class
helper function to find gpa for a class
returns-gpa of the class
"""


def calcGPA(grades):
    total_students = sum(grades)
    mult = 4
    gpa = 0.00
    for k in range(0, 12):
        if (k > 1):
            if (k % 3 != 0 and k != 12):
                mult = round(mult - (1 / 3), 2)
            elif (k == 12):
                mult = 0
            else:
                mult = round(mult - .34, 2)
        gpa = gpa + grades[k] * mult
    gpa = round(gpa / total_students, 2)
    return gpa


"""
getclassrows
input- list of subjects and class abbreviation
helper function to find class row indexs
given a class subject abbrivation 
return-the rows in the dataset that that class appears
"""


def getclassrows(list_a, abrv):
    if (abrv not in list_a):
        return 'error not a valid subject'
    row_indexs = []
    for k in range(0, len(list_a)):
        if (abrv == list_a[k]):
            row_indexs.append(k)
    return row_indexs


"""
getGPA
inputs-subject abbreviation
gets gpa given subject abbreviation
return-list of gpas of the subject"""


def getGPA(abrv):
    row_indexes = getclassrows(subject, abrv)
    gpas = []
    for k in range(0, len(row_indexes)):
        gpas.append(calcGPA(grade_data[row_indexes[k]]))
    return gpas


"""
getcoursetitle
inputs-subject abbreviation
gets coursetitle given subject abbreviation
return-list of course titles of the subject
"""


def getcoursetitle(name):
    row_indexes = getclassrows(subject, name)
    names = []
    for k in range(0, len(row_indexes)):
        names.append(course_title[row_indexes[k]])
    return names


"""
getyear
inputs-subject abbreviation
gets year and seimister given subject abbreviation
return-list of years and semisters of the subject
"""


def getyear(abrv):
    row_indexes = getclassrows(subject, abrv)
    year = []
    for k in range(0, len(row_indexes)):
        year.append(years[row_indexes[k]])
    return year


"""
getinstructor
inputs-subject abbreviation
gets instructor given subject abbreviation
return-list of instructors of the subject
"""


def getinstructor(abrv):
    row_indexes = getclassrows(subject, abrv)
    name = []
    for k in range(0, len(row_indexes)):
        name.append(instructor[row_indexes[k]])
    return name


"""
getcoursenumber
inputs-subject abbreviation
gets course number given subject abbreviation
return-list of course numbers of the subject
"""


def getcoursenumber(abrv):
    row_indexes = getclassrows(subject, abrv)
    num = []
    for k in range(0, len(row_indexes)):
        num.append(str(course_number[row_indexes[k]]))
    return num





"""
combine_lists
inputs-subject abbreviation
combins the getGPA, getYear... ect. lists into one 2d list
returns- the combinned list
"""


def combine_lists(abrv):
    list1 = getcoursetitle(abrv)
    list2 = getGPA(abrv)
    list3 = getyear(abrv)
    list4 = getinstructor(abrv)
    list5 = getcoursenumber(abrv)
    rtrn_list = [[]]
    for k in range(0, len(list1)):
        rtrn_list[k].append(list1[k])  # course title
        rtrn_list[k].append(list3[k])  # Year/seimister
        rtrn_list[k].append(list5[k])  # coursenum
        rtrn_list[k].append(list4[k])  # instructor
        rtrn_list[k].append(list2[k])  # gpa
        rtrn_list.append([])
    del rtrn_list[-1]
    return (rtrn_list)



"""
avegpa_year
inputs-subject abbreviation
condenses the combined list combine_lists function so the list has the average gpa for all sections for the given year/seimister
returns-list with year/seimister, course number and average gpa for that course in that year/seimister
"""


def avegpa_year(abrv):
    alldata = combine_lists(abrv)
    gpa_year = [[]]
    gpa_sum = 0.0
    gpa = 0.0
    num = 1.0
    index = 0
    reset = True
    for k in range(0, len(alldata)):
        reset = False
        if (k == 0):
            gpa_year[index].append(alldata[k][1])
            reset = True
        elif (alldata[k][1] not in gpa_year[index]):
            gpa_year.append([])
            index = index + 1
            gpa_year[index].append(alldata[k][1])
            reset = True
            gpa = gpa_sum / num
            gpa = round(gpa, 2)
            gpa_year[index - 1][2] = gpa
            gpa = 0.0
            num = 1.0
            gpa_sum = 0.0
        if (alldata[k][2] not in gpa_year[index] and reset == False):
            gpa_year.append([])
            index = index + 1
            gpa_year[index].append(alldata[k][1])
            gpa_year[index].append(alldata[k][2])
            gpa_year[index].append(alldata[k][4])
            gpa = gpa_sum / num
            gpa = round(gpa, 2)
            gpa_year[index - 1][2] = gpa
            gpa = 0.0
            num = 1.0
            gpa_sum = alldata[k][4]
        elif (alldata[k][2] not in gpa_year[index]):
            gpa_year[index].append(alldata[k][2])
            gpa_year[index].append(alldata[k][4])
            gpa_sum = alldata[k][4]
        else:  # duplicate year and course number (2 or more offerings of that course in a year)
            num = num + 1
            gpa_sum = gpa_sum + alldata[k][4]
    return gpa_year

"""
filters
inputs-subject abbreviation, year/seimister(optional) course number (optional
filters data based on user inputs. If user inputs just the abreviation it returns all clases in that subject.
If the user enters the year and/or course number it returns the classes that meet that requirment
returns-filtered list based on given requirments
"""


def filters(abrv, year="", number=""):
    alldata = combine_lists(abrv)
    filtered = [[]]
    if (year == "" and number == ""):
        return alldata
    if (number == ""):
        for k in range(0, len(alldata)):
            if (year in alldata[k]):
                filtered.append(alldata[k])
        del filtered[0]
        return filtered
    else:
        for k in range(0, len(alldata)):
            if (year in alldata[k] and number in alldata[k]):
                filtered.append(alldata[k])
        del filtered[0]
    return filtered


"""
makeinputreadable
input-string 
This is a helper function to allow the filters function to work on the Website. It splits the string on spaces and 
then enters this string into the filters function.
returns-list from filters fucntion based on the given input
"""


def makeinputreadable(input):
    inputs = input.split()
    correct_size = True
    while correct_size:
        if (len(inputs) < 3):
            inputs.append("")
        else:
            correct_size = False
    return filters(inputs[0], inputs[1], inputs[2])



"""
make_dataframe
input-string containing course abbreviation and year/semister(optional) and course number(optional) all of these are seperated by a space
makes dataframe given text input from website
returns-data table with displaying the course data
"""


def make_dataframe(text):
    words = text.split()
    if (words[0] not in subject):
        return 'error not a valid subject'
    alldata = makeinputreadable(text)
    data = pandas.DataFrame(alldata, columns=["Class", "Year and Seimester", "Course Number", "Instructor", "GPA"])
    return data


"""
make_sorted_dataframe
inputs-string containing course abbreviation and year/semister(optional) and course number(optional) all of these are seperated by a space
same as make_dataframe function except sorts the datafram from highest to lowest gpa
returns-data table sorted from highest to lowest gpa
"""


def make_sorted_dataframe(text):
    words = text.split()
    if (words[0] not in subject):
        return 'error not a valid subject'
    alldata = makeinputreadable(text)
    alldata.sort(key=lambda x: x[4], reverse=True)
    data = pandas.DataFrame(alldata, columns=["Class", "Year and Seimester", "Course Number", "Instructor", "GPA"])
    return data


"""
make_reverse_sorted_dataframe
inputs-string containing course abbreviation and year/semister(optional) and course number(optional) all of these are seperated by a space
same as make_dataframe function except sorts the datafram from highest to lowest gpa
returns-data table sorted from lowest to highest gpa
"""


def make_reverse_sorted_dataframe(text):
    words = text.split()
    if (words[0] not in subject):
        return 'error not a valid subject'
    alldata = makeinputreadable(text)
    alldata.sort(key=lambda x: x[4], reverse=False)
    data = pandas.DataFrame(alldata, columns=["Class", "Year and Seimester", "Course Number", "Instructor", "GPA"])
    return data

# def stats(abrv):
#     gpa_year =
#     return
#
# def plot_data():
print(filters("AAS", "100"))

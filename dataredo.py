import pandas
import matplotlib as plt
import numpy as np

#first commit
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
calcGPA: Calculates Grade Point Average
inputs: grades- a list of ints length 12 ordered in A+, A..., F format. 
These grades are only for one Class section.
return value- the gpa for a class for that section.
helper function to find gpa for a class
returns-gpa of the class
"""


def calcGPA(grades):
    out = 0.
    for k in zip(grades, [4., 4., 3.67, 3.33, 3., 2.67, 2.33, 2., 1.67, 1.33, 1., 0.67, 0.]):
        out += int(k[0]) * k[1]
    return round(out / sum([int(k) for k in grades]), 2)


#list that stores all of the data
alldata = [[]]

def makedata(abrv, number = "", year =""):
    print(year)
    if (abrv not in subject):
        return "error not a valid subject"
    i = 0
    if (year == "" and number == ""):
        for k in range(0, len(subject)):
            if (abrv == subject[k]):
                # datas[i].append(course_title[1])
                alldata[i].append(course_title[k])  # course title
                alldata[i].append(years[k])  # Year/seimister
                alldata[i].append(str(course_number[k]))  # coursenum
                alldata[i].append(instructor[k])  # instructor
                alldata[i].append(calcGPA(grade_data[k]))  # gpa
                alldata[i].append(str(sum(grade_data[k])))
                alldata.append([])
                i += 1
    elif (year == ""):
        for k in range(0, len(subject)):
            if (abrv == subject[k] and number == str(course_number[k])):
                # datas[i].append(course_title[1])
                alldata[i].append(course_title[k])  # course title
                alldata[i].append(years[k])  # Year/seimister
                alldata[i].append(str(course_number[k]))  # coursenum
                alldata[i].append(instructor[k])  # instructor
                alldata[i].append(calcGPA(grade_data[k]))  # gpa
                alldata[i].append(str(sum(grade_data[k])))
                alldata.append([])
                i += 1
    elif (number == ""):
        for k in range(0, len(subject)):
            if (abrv == subject[k] and year == years[k]):
                # datas[i].append(course_title[1])
                alldata[i].append(course_title[k])  # course title
                alldata[i].append(years[k])  # Year/seimister
                alldata[i].append(str(course_number[k]))  # coursenum
                alldata[i].append(instructor[k])  # instructor
                alldata[i].append(calcGPA(grade_data[k]))  # gpa
                alldata[i].append(str(sum(grade_data[k])))
                alldata.append([])
                i += 1
    else:
        for k in range(0, len(subject)):
            if (abrv == subject[k] and number == str(course_number[k]) and year == years[k]):
                # datas[i].append(course_title[1])
                alldata[i].append(course_title[k])  # course title , 0
                alldata[i].append(years[k])  # Year/seimister, 1
                alldata[i].append(str(course_number[k]))  # coursenum, 2
                alldata[i].append(instructor[k])  # instructor, 3
                alldata[i].append(calcGPA(grade_data[k]))  # gpa, 4
                alldata[i].append(str(sum(grade_data[k])))  #number of students, 5
                alldata.append([])
                i += 1
    del alldata[-1]
    return



#not true average just average by section, mean may be communitive

def calc_course_average():
    if not alldata:
        return "No course has been selected yet"
    dictf = dict()
    courses = []
    for k in range(0, len(alldata)):
        if alldata[k][2] in dictf.keys():
            l = dictf[alldata[k][2]]
            l.append(alldata[k][4])
            dictf.update({alldata[k][2] : l})
        else:
            dictf[alldata[k][2]] = [alldata[k][4]]
            courses.append(alldata[k][0])
    gpaAverages = [[]]
    i = 0
    for k in dictf:
        aGpa = round(sum(dictf[k]) / len(dictf[k]), 2)
        gpaAverages[i].append(courses[i])
        gpaAverages[i].append(k)
        gpaAverages[i].append(str(aGpa))
        gpaAverages.append([])
        i += 1
    del gpaAverages[-1]
    return gpaAverages



"""
avegpa_year
inputs-subject abbreviation
condenses the combined list combine_lists function so the list has the average gpa for all sections for the given year/seimister
returns-list with year/seimister, course number and average gpa for that course in that year/seimister
"""


def avegpa_year(abrv):
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
        else:  # duplicate year and course number (2 or more offerings of that course in a year)
            num = num + 1
            gpa_sum = gpa_sum + alldata[k][4]
    return gpa_year



def main():
    makedata("CS")
    agpa = calc_course_average()
    # print(agpa)
    # print(alldata)

if __name__ == '__main__':
    main()
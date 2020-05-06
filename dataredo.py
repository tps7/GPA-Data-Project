import pandas
import matplotlib.pyplot as plt
import numpy as np

#first commit
pandas.set_option('display.max_columns', 500)
df = pandas.read_csv('uiuc-gpa-dataset.csv')
grade_data = df[['A+', 'A', 'A-', 'B+', 'B', 'B-', \
                 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']].values
course_title = df['Course Title'].values
subject = df['Subject'].values
years = df['YearTerm'].values
instructor = df['Primary Instructor'].values
course_number = df['Number'].values

"""
run
inputs: the input from the website in the format it would be on the website
This function will be called in main it basically sets up all the functions to run.
This function sets up the local varible input which holds the input from the website.
Input is submited in format [Subject, Number, Year/Sem] code only works if inputs are in that order;
outputs list of inputs
"""

orginput = ""
input = []
def run(inputs):
    orginput = inputs
    inputs = inputs.split()
    if inputs[0] not in subject:
        return "error not a valid subject"
    correct_size = True
    while correct_size:
        if (len(inputs) < 3):
            inputs.append("")
        else:
            correct_size = False
    global input
    input = inputs
    return


"""
calcGPA: Calculates Grade Point Average
inputs: grades- a list of ints length 12 ordered in A+, A..., F format. 
These grades are only for one Class section.
return value- the gpa for a class for that section.
helper function to find gpa for a class
returns-gpa of the class
"""


def calcGPA(grades):
    sums = 0
    sums += grades[0] * 4
    sums += grades[1] * 4
    sums += grades[2] * 3.67
    sums += grades[3] * 3.33
    sums += grades[4] * 3
    sums += grades[5] * 2.67
    sums += grades[6] * 2.33
    sums += grades[7] * 2
    sums += grades[8] * 1.67
    sums += grades[9] * 1.33
    sums += grades[10] * 1
    sums += grades[11] * .67
    sums += grades[12] * 0
    students = sum(grades)
    return round(sums / students, 2)
    # out = 0.
    # for k in zip(grades[0: 12], [4., 4., 3.67, 3.33, 3., 2.67, 2.33, 2., 1.67, 1.33, 1., 0.67, 0.]):
    #     out += int(k[0]) * k[1]
    # return round(out / sum([int(k) for k in grades[0 : 12]]), 2)


#list that stores all of the data
alldata = [[]]
def makedata():
    global alldata
    alldata = [[]]
    abrv = input[0]
    number = input[1]
    year = input[2]
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




def getMean():
    classGrades = dict()
    courses = []
    q = 0
    for k in range(0, len(subject)):
        if str(course_number[k]) in classGrades.keys() and subject[k] == input[0]:
            l = np.array(classGrades[str(course_number[k])])
            r = np.array(grade_data[k])
            l = np.add(l, r)
            classGrades.update({str(course_number[k]): l})
        elif subject[k] == input[0]:
            classGrades[str(course_number[k])] = np.array(grade_data[k])
            courses.append(course_title[k])
    gpaAverages = [[]]
    i = 0
    for k in classGrades:
        aGpa = calcGPA(classGrades[k])
        gpaAverages[i].append(courses[i])
        gpaAverages[i].append(k)
        gpaAverages[i].append(str(aGpa))
        gpaAverages.append([])
        i += 1
    del gpaAverages[-1]
    return gpaAverages

"""
Note on GPA diffrences. 
GPA differs between average of averages and overall averages. Classes like CS 101 that have class sizes of varying 
from ~30 to over 400 will have diffrent GPA's because the GPA of the class of 30 is weighted equally as the GPA of the 
class of 400. Whereas the whole average every A in the class counts the same. 
However it later may be nice to have a GPA that holds each year semister equally, but I doubt this 
would vary much from my overall average. Maybe chart on course varance overtime?
"""

# def calc_course_average():
#     if not alldata:
#         return "No course has been selected yet"
#     classGrades = dict()
#     courses = []
#     for k in range(0, len(alldata)):
#         if alldata[k][2] in classGrades.keys():
#             l = classGrades[alldata[k][2]]
#             print(alldata[k][5])
#             l.append(alldata[k][4])
#             classGrades.update({alldata[k][2] : l})
#         else:
#             classGrades[alldata[k][2]] = [alldata[k][4]]
#             courses.append(alldata[k][0])
#     print(classGrades)
#     gpaAverages = [[]]
#     i = 0
#     for k in classGrades:
#         print(sum(classGrades[k]))
#         aGpa = round(sum(classGrades[k]) / len(classGrades[k]), 2)
#         gpaAverages[i].append(courses[i])
#         gpaAverages[i].append(k)
#         gpaAverages[i].append(str(aGpa))
#         gpaAverages.append([])
#         i += 1
#     del gpaAverages[-1]
#     return gpaAverages

# def make_plots():
#     ave = getMean()
#     print(ave)
#     plt.xlabel('Class')
#     plt.ylabel('GPA')
#     plt.show()
#     plt.plot.bar(ave[:][1], ave[:][2])

def make_dataframe():
    data = pandas.DataFrame(alldata, columns=["Class", "Year and Seimester", "Course Number", "Instructor", "GPA", "# of students"])
    # global websiteData
    # websiteData = data
    return data



def main():
    run("CS")

    makedata()
    q = getMean()
    # make_plots()
    print(q)

if __name__ == '__main__':
    main()
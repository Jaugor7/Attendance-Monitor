from django.shortcuts import render
import csv
import glob
import pandas as pd

# Create your views here.

def index(request):
    return render(request, 'index.html')


def createAttendence():

    path_csv=glob.glob("./AttendaceManagementSystem/Attendance/*.csv")
    
    df = pd.read_csv(path_csv[0], delimiter=',', encoding='UTF-8')
    combined_csv_data = pd.concat([pd.read_csv(f, delimiter=',', encoding='UTF-8') for f in path_csv])
    combined_csv_data.to_csv('Attendance.csv')


def teacherView(request):
    students = []
    records = dict()

    createAttendence()

    with open('Attendance.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        fields = next(csvreader)

        for line in csvreader:

            name = line[2].strip("[']").split()
            firstName = name[0]
            lastName = ""
            if len(name) > 1:
                lastName = name[1]

            rollNumber = line[1]

            records[rollNumber] =  {
                'firstName': firstName,
                'lastName': lastName,
            }

        for (key,recordDict) in records.items():
            tempDict = {
                'rollNumber' : key,
                'lastName' : recordDict['lastName'],
                'firstName' : recordDict['firstName']
            }
            students.append(tempDict)

    context = {
        'students': sorted(students, key = lambda x: x['rollNumber']),
    }
    return render(request, 'teacherView.html', context)


def studentView(request, rollNumber):
    studentRecords = []
    firstName = ""
    lastName = ""

    with open('Attendance.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        fields = next(csvreader)

        for line in csvreader:

            if line[1] != rollNumber:
                continue

            name = line[2].strip("[']").split()
            print(name)

            firstName = name[0]
            if len(name) > 1:
                lastName = name[1]

            tempDict = {
                'date': line[3],
                'time': line[4],
            }

            studentRecords.append(tempDict)
        
    context = {
        'firstName': firstName,
        'lastName': lastName,
        'rollNumber': rollNumber,
        'studentRecords' : studentRecords,
    }

    return render(request, 'studentView.html', context)


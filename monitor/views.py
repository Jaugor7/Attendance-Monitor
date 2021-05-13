from django.shortcuts import render
import csv

# Create your views here.

def index(request):
    return render(request, 'index.html')

def teacherView(request):
    students = []
    records = dict()

    with open('Attendance.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        fields = next(csvreader)

        for line in csvreader:

            name = line[1].strip("[']").split()
            firstName = name[0]
            lastName = ""
            if len(name) > 1:
                lastName = name[1]

            rollNumber = line[0]

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

            if line[0] != rollNumber:
                continue

            print(line)

            name = line[1].strip("[']").split()

            firstName = name[0]
            if len(name) > 1:
                lastName = name[1]

            tempDict = {
                'date': line[2],
                'time': line[3],
            }

            studentRecords.append(tempDict)
        
    context = {
        'firstName': firstName,
        'lastName': lastName,
        'rollNumber': rollNumber,
        'studentRecords' : studentRecords,
    }

    return render(request, 'studentView.html', context)


"""
Recording link: xxxxxxxxxxxxxxx

1.	Staff Overtime Pay: 
You are given 1_OT.csv file by the Chief Technical Officer (CTO) in the department during an
 interview for an intern position in the Data Analytics department of a manufacturing company. 
 This file contains the working hours of 1200 staff in the company on a particular day. 
 Each record corresponds to one unique staff in the file. The file contains information on StaffID, 
 Department, Total Hours clocked for the day. The normal working hour for all staff is 8 hours, 
 any additional hours after the first 8 hours is considered as overtime (OT). The OT hours is capped 
 at 4 hours maximum. This is to ensure that the staff do not overwork themselves for additional pay. 
 This would mean that even a staff works for 20 hours, he/she will still be paid 8 hours normal rate 
 and 4 hours OT rate. The finance department uses this file for payroll computation.

Provide your solution based on the following requirements:
•	The company CEO would like to know the OT payments of the 1200 staff in the given file.
•	You are required to tabulate the result in the following format:
__________________________________________________
| Department Number |  Number of people working OT |
__________________________________________________
|                   |                              |
__________________________________________________
	
To value add to the analytics, your interviewer would like you to think of one additional analysis 
that the management of the company may be interested to find out. Present your suggested solution 
and explain how such analysis add values to the company.
"""

import csv


def readCSV():
    with open('test.csv') as f:
        test = csv.reader(f)
        testArray = []
        for row in test:
            # print(','.join(row))
            # print(row)
            testArray.append(row)
    # print(testArray)
    # print(testArray[1][1])
    # testing = int(testArray[1][1]) + int(testArray[1][2])
    # print(testing)
    return testArray


def processingCSV(testArray):
    testArray.pop(0)
    print(testArray)
    """deptArray = []
    hoursArray = []"""
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    counter7 = 0
    counter8 = 0

    OTHoursPay = 0
    OTHoursTotal = 0

    noOfWorkers = len(testArray)

    for i in range(len(testArray)):
        deptNo = testArray[i][1]
        hourNo = int(testArray[i][2])
        if hourNo < 8:
            continue  # skip current worker if never work OT
        # for workers that exceed 8 hour work
        hourDiff = hourNo - 8
        OTHoursTotal += hourDiff
        if hourDiff > 4:
            hourDiff = 4
        OTHoursPay += hourDiff
        match(deptNo):  # for workers that exceed 8 hour work
            case "1":
                # print("test")
                counter1 += 1
                """hourDiff = hourNo - 8
                if hourDiff > 4:
                    hourDiff = 4"""
            case "2":
                # print("test")
                counter2 += 1
            case "3":
                # print("test")
                counter3 += 1
            case "4":
                # print("test")
                counter4 += 1
            case "5":
                # print("test")
                counter5 += 1
            case "6":
                # print("test")
                counter6 += 1
            case "7":
                # print("test")
                counter7 += 1
            case "8":
                # print("test")
                counter8 += 1
            case _:
                print("Error reading a department number cell")
    avgOTHours = OTHoursTotal/noOfWorkers
    return counter1, counter2, counter3, counter4, counter5, counter6, counter7, counter8, OTHoursPay, OTHoursTotal, avgOTHours
    """print(counter1)
    print(counter2)
    print(counter3)
    print(counter4)
    print(counter5)
    print(counter6)
    print(counter7)
    print(counter8) """


def program():
    testArray = readCSV()
    deptTuple = processingCSV(testArray)
    # print(deptTuple)
    print("| Department Number |  Number of people working OT  |")
    for i in range(1, len(deptTuple)-2):
        print("|         ", i, "       |               ",
              deptTuple[i-1], "            | ")
    print("Total OT Hours liable for compensation: ", deptTuple[8])
    print("Total OT Hours: ", deptTuple[9])
    print("Average OT Hours per worker: ", deptTuple[10])


program()

"""

CISC-121 2023W
Name:   Enhao Fan
Student Number: 20340476
Email:  21ef30@queensu.ca
Date: 2023-03-02

I confirm that this assignment solution is my own work and conforms to
Queen's standards of Academic Integrity

"""

import csv

# Function to read the dataset from CSV file and store in list of dictionaries
def readData(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Function to display information given an electoral district number
def displayInfo(data, edNum):
    for row in data:
        if 'Electoral District Number' in row and int(row['Electoral District Number']) == edNum:
            print("Number of polling stations:", row['Polling Stations'])
            print("Number of valid ballots:", row['Valid Ballots'])
            print("Total ballots cast:", row['Total Ballots Cast'])
            print("Percentage of voter turnout:", row['Percentage of Voter Turnout'])
            return
    print("Invalid electoral district number")
# Function to get a list of unique electoral district names for a given province
def uniqueDistricts(data, province):
    districts = []
    for row in data:
        if row['Province Name'].lower() == province.lower():
            districts.append(row['Electoral District Name'])
    return districts

# Function to find the maximum value and associated electoral district name for a given key
def findMax(data, key):
    maxVal = float('-inf')
    maxED = ''
    for row in data:
        val = float(row[key])
        if val > maxVal:
            maxVal = val
            maxED = row['Electoral District Name']
    return (maxVal, maxED)

# Function to find the minimum value and associated electoral district name for a given key
def findMin(data, key):
    minVal = float('inf')
    minED = ''
    for row in data:
        val = float(row[key])
        if val < minVal:
            minVal = val
            minED = row['Electoral District Name']
    return (minVal, minED)

# Function to calculate the total number of ballots cast in every Canadian province and territory
def totalVotes(data):
    provinces = {}
    for row in data:
        province = row['Province Name']
        ballots = float(row['Total Ballots Cast'])
        if province in provinces:
            provinces[province] += ballots
        else:
            provinces[province] = ballots
    return [{'Province Name': p, 'Total Ballots Cast': provinces[p]} for p in provinces]

# Function to sort the supplied list of dictionaries in situ (in-place) into increasing order based on the specified key
def selectionSort(data, key):
    for i in range(len(data)-1):
        min_idx = i
        for j in range(i+1, len(data)):
            if float(data[j][key]) < float(data[min_idx][key]):
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

# Function to search for an electoral district based on its electoral district number and return the percentage of voter turnout in that district using binary search
def binarySearch(data, edNum):
    left, right = 0, len(data)-1
    while left <= right:
        mid = (left + right) // 2
        if int(data[mid]['Electoral District Number']) == edNum:
            return float(data[mid]['Percentage of Voter Turnout'])
        elif int(data[mid]['Electoral District Number']) < edNum:
            left = mid + 1
        else:
            right = mid - 1
    return -1
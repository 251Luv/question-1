"""

CISC-121 2023W
Name:   Enhao Fan
Student Number: 20340476
Email:  21ef30@queensu.ca
Date: 2023-03-02

I confirm that this assignment solution is my own work and conforms to
Queen's standards of Academic Integrity

"""

# Main program
import functions3

# Main program
filename = 'table_tableau11.csv'
data = functions3.readData(filename)

while True:
    print("\nPlease choose an option from the following menu:\n")
    print("1. Display information for a specific electoral district")
    print("2. Get a list of unique electoral districts for a given province")
    print("3. Find the maximum value for a specific attribute")
    print("4. Find the minimum value for a specific attribute")
    print("5. Calculate the total number of ballots cast in every Canadian province and territory")
    print("6. Sort the dataset based on a specific attribute")
    print("7. Binary search to find the percentage of voter turnout for an electoral district")
    print("0. Exit\n")
    option = input("Option: ")

    if option == "0":
        print("Exiting the program...")
        break

    elif option == "1":
        edNum = int(input("Enter electoral district number: "))
        functions3.displayInfo(data, edNum)

    elif option == "2":
        province = input("Enter province name: ")
        districts = functions3.uniqueDistricts(data, province)
        print("Unique electoral districts in", province, "are:")
        for district in districts:
            print(district)

    elif option == "3":
        key = input("Enter attribute name (Electors/Population/Polling Stations/Valid Ballots/Rejected Ballots/Total Ballots Cast): ")
        maxVal, maxED = functions3.findMax(data, key)
        print("Maximum value of", key, "is", maxVal, "in electoral district", maxED)

    elif option == "4":
        key = input("Enter attribute name (Electors/Population/Polling Stations/Valid Ballots/Rejected Ballots/Total Ballots Cast): ")
        minVal, minED = functions3.findMin(data, key)
        print("Minimum value of", key, "is", minVal, "in electoral district", minED)

    elif option == "5":
        provinces = functions3.totalVotes(data)
        print("Total number of ballots cast in every Canadian province and territory:")
        for province in provinces:
            print(province['Province Name'], ":", province['Total Ballots Cast'])

    elif option == "6":
        key = input("Enter attribute name (Electors/Population/Polling Stations/Valid Ballots/Rejected Ballots/Total Ballots Cast): ")
        functions3.selectionSort(data, key)
        print("Dataset sorted based on", key, "attribute.")

    elif option == "7":
        edNum = int(input("Enter electoral district number: "))
        data.sort(key=lambda row: int(row['Electoral District Number']))
        percTurnout = functions3.binarySearch(data, edNum)
        if percTurnout == -1:
            print("Electoral district not found.")
        else:
            print("Percentage of voter turnout for electoral district", edNum, "is", percTurnout)

    else:
        print("Invalid option. Please choose again.\n")
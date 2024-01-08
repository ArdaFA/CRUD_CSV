# import csv 
# # in order to read any file, we should open it in a read mode
# with open('./users.csv') as file:
#    csv_reader = csv.reader(file, delimiter=',')
#    lineCount = 0
#    for row in csv_reader: 
#         if lineCount == 0:
#             print(f'Column names are {", ".join(row)}')
#             lineCount += 1
#         else:
#             print(row[0], row[1], row[2])
#             # row[0] = first name 
#             # row[1] = last name
#             # row[2] = age
#             lineCount += 1
# print(f'Processed {lineCount} lines.')

import pandas as pd

fileName = input("Filename: ")
# Read the CSV file into a DataFrame
df = pd.read_csv(f'./{fileName}.csv')

while True:
    userSelection = input("What do you want to read?\n"
                     "First Name = f\n"
                     "Last Name = l\n"
                     "Age = a\n"
                     "See all: s\n"
                     "Enter 'q' to quit\n"
                     "Your selection: ")

    if userSelection == 's':
        print(df)
    elif userSelection == 'f':
        index = input("Enter the index you want to read: ")
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(df):
                selectedUser = df.at[index, 'First Name']
                print(f'First Name of {index}: {selectedUser}')
            else:
                print("Invalid index. Please enter a valid index.")
        else:
            print("Invalid input. Please enter a valid index.")
    elif userSelection == 'l':
        index = input("Enter the index you want to read: ")
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(df):
                selectedUser = df.at[index, 'Last Name']
                print(f'Last Name of {index}: {selectedUser}')
            else:
                print("Invalid index. Please enter a valid index.")
        else:
            print("Invalid input. Please enter a valid index.")
    elif userSelection == 'a':
        index = input("Enter the index you want to read: ")
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(df):
                selectedUser = df.at[index, 'Age']
                print(f'Age of {index}: {selectedUser}')
            else:
                print("Invalid index. Please enter a valid index.")
        else:
            print("Invalid input. Please enter a valid index.")
    elif userSelection == 'q':
        break



'''
1- Creating a CSV file 
2- Adding row 
3- Adding Multiple row
4- Reading rows
5- 2nd approach
    i) Reading 
    ii) Writing 
6- Append New Rows at the end of the file 
7- Updating (update cell, column, row)
8- Deleting (column, row, cell)
'''

# from csv import writer

# with open('./users.csv', 'w', newline='') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(['First Name', 'Last Name', 'Age'])

#     data = [
#         ('Magnus', 'Carlsen', '32'),
#         ('Hikaru', 'Nakamura', '35'),
#         ('Hans', 'Niemann', '20')
#     ]

#     while True:
#         user_input = input("Enter 'w' to add a new row or 'q' to quit: ")
#         if user_input == 'w':
#             name = input("Name: ")
#             last_name = input("Last Name: ")
#             age = input("Age: ")
#             new_row = [name, last_name, age]
#             data.append(new_row)
#         elif user_input == 'q':
#             break

#     for row in data:
#         csv_writer.writerow(row)

import pandas as pd

df = pd.read_csv('./users.csv')
while True:
    user_input = input("to write enter 'w' \n"
                     "Enter 'q' to quit\n"
                     "Your selection: ")
    if user_input == 'w':
        name = input("Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        # Create a new row to add to the DataFrame
        new_data = {'First Name': name, 'Last Name': last_name, 'Age': age}

        # Append the new data to the DataFrame
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        # Save the updated DataFrame back to the CSV file
        df.to_csv('./users.csv', index=False)
    
    elif user_input == 'q':
        break





        
     
    
        

    

#   csv_writer.writerows(data)

# in order to read any file, we should open it in a read mode
# with open('./users.csv') as file:
#     print([row.split('\t') for row in file.read().split('\n')]) 

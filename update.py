# importing the pandas library 
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('./users.csv')

while True:
    index = input("Which index do you want to update (enter 'q' to quit)? ")
    
    if index == 'q':
        break

    if not index.isdigit():
        print("Invalid index. Please enter a valid index.")
        continue

    index = int(index)

    if 0 <= index < len(df):
        oldColumn = input("Which column do you want to update (First Name, Last Name, Age)? ")
        
        if oldColumn not in df.columns:
            print(f"Column '{oldColumn}' does not exist in the DataFrame.")
            continue

        newValue = input(f"New {oldColumn} value: ")
        
        # Update the DataFrame with the new value
        df.at[index, oldColumn] = newValue

        print("Updated!")
        print(df)

        # Save the updated DataFrame back to the CSV file
        df.to_csv('./users.csv', index=False)
    else:
        print("Invalid index. Please enter a valid index.")



# updating the column value/data 
#df.loc[5, 'Name'] = 'SHIV CHANDRA'

# writing into the file 
#df.to_csv("AllDetails.csv", index=False) 

#print(df) 

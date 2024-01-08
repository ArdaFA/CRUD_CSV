import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('./users.csv')

# Specify the index of the row you want to delete
index_to_delete = input("Which index do you want to delete? ")
index_to_delete = int(index_to_delete)

# Delete the row by index
df = df.drop(index_to_delete)

# Save the updated DataFrame back to the CSV file
df.to_csv('./users.csv', index=False)
print("deleted!")
print(df)

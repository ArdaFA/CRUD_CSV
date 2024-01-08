import requests
import pandas as pd

# url = "http://127.0.0.1:5000/cars/3"
# response = requests.get(url)

# Get user input for the ID
user_input = input("Enter the ID: ")

# Construct the URL with the user input
url = f"http://127.0.0.1:5000/cars/{user_input}"

# Send a GET request to the constructed URL
response = requests.get(url)

df = pd.read_csv(f'./users.csv')
index = input("Enter the index you want to compare from csv: ")
if index.isdigit():
    index = int(index)
    if 0 <= index < len(df):
        selectedUser = df.at[index, 'First Name']
        print(f'Name of {index} from csv: {selectedUser}')
    else:
        print("Invalid index. Please enter a valid index.")
else:
    print("Invalid input. Please enter a valid index.")

if response.status_code == 200:
    data = response.json()
    print("Data from the API is down below")
    print("Name:", data["name"])
    print("Model:", data["model"])
    if data["name"] == selectedUser:
        print("Matched! ALL SAFE")
    else:
        print("Data from api and csv has not matched! SOMETHING WENT WRONG!")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


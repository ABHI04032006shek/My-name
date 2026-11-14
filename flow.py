import pandas as pd
import os

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Amit', 'Rahul', 'Priya'],
    'Age': [22, 24, 21],
    'Salary': [25000, 35000, 30000]
})

# Get current working directory
current_path = os.getcwd()

# Create a new folder inside current folder
new_folder = os.path.join(current_path, "Dataset")

os.makedirs(new_folder, exist_ok=True)

# Save CSV inside the new folder
file_path = os.path.join(new_folder, "data.csv")

df.to_csv(file_path, index=False)

print("Saved at:", file_path)
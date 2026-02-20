import pandas as pd
import os

data = {'Name': ['Abhishek', 'Ishan', 'Tilak', 'SKY', 'Hardik', 'Dube'],
        'Age': [22, 24, 26, 28, 30, 32],
        'City': ['ahmedabad', 'Hyderabad', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai']}


df = pd.DataFrame(data)

# Add new row
new_row_loc = {'Name': 'GF1', "Age": 20, 'City': 'Jammu'}
df.loc[len(df.index)] = new_row_loc

# Ensure data dir path exists
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define file path
file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")

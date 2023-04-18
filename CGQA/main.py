import pandas as pd
import string
import os

# Set directory path
directory_path = os.path.join(os.getcwd(), 'MCQA-teste')

# Get all file names in directory
file_names = os.listdir(directory_path)

df_list = []

for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    print(file_path)
    df = pd.read_csv(file_path)

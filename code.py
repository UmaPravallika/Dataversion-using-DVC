import pandas as pd
import os

print("***Taking input***")

data={
    "Name":["Ram","Sita","Radha","Krishna"],
    "age":[25,20,16,18],
    "City":["Ayodhya","Srilanka","Barsana","Vridhavan"]
}

# Convert data into dataframe :
df=pd.DataFrame(data)
print(df)

# Adding new row to df for V2 :
#new_record={'Name': 'GF1', 'Age': 20, 'City': 'City1'}
#df.loc[len(df.index)]=new_record

# Adding new row to df for V3 :
# new_record={'Name': 'GF2', 'Age': 30, 'City': 'City2'}
# df.loc[len(df.index)]=new_record

#print("After appending new record for v3 : \n",df)

# Ensure that data dir exist before :
data_dir="data_dir"
os.makedirs(data_dir,exist_ok=True)

# Define a directory to save the file : 
file_path=os.path.join(data_dir,"Sample_data_to_csv")

#Convert file into csv :
df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path} successfully!!!")
#################################
# List all non-standard packages to be imported by your 
# script here (only missing packages will be installed)
from ayx import Package
Package.installPackages(['azure-storage-file-datalake','pandas'])


#################################
from ayx import Alteryx
from azure.storage.filedatalake import DataLakeServiceClient
import pandas as pd



#################################
df = Alteryx.read("#1")


#################################
storage_account_name = df.iloc[0,0]
storage_account_key = df.iloc[0,1]
file_system = df.iloc[0,2]
directory = df.iloc[0,3]


#################################
# Create connection method
def initialize_storage_account(storage_account_name, storage_account_key):
    
    try:  
        global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
    
    except Exception as e:
        print(e)


#################################
# Connect to account
initialize_storage_account(storage_account_name, storage_account_key)


#################################
def list_directory_contents(file_system, directory):
    try:
        file_paths = []

        file_system_client = service_client.get_file_system_client(file_system = file_system)

        paths = file_system_client.get_paths(path = directory)

        for path in paths:
            file_paths.append(path.name)

        return file_paths

    except Exception as e:
     print(e)


#################################
# List directory contents
results = list_directory_contents(file_system, directory)


#################################
# Create dataframe
df = pd.DataFrame(results)


#################################
# Write to output #1
Alteryx.write(df,1)


#################################

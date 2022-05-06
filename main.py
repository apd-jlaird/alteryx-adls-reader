import configparser
from azure.storage.filedatalake import DataLakeServiceClient

# Import config file
config = configparser.ConfigParser()
config.read('config.ini')

# Import config parameters
storage_account_name = config['sandbox']['storage_account_name']
storage_account_key = config['sandbox']['storage_account_key']
file_system = config['sandbox']['file_system']
directory = config['sandbox']['directory']

# Create connection method
def initialize_storage_account(storage_account_name, storage_account_key):
    
    try:  
        global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
    
    except Exception as e:
        print(e)

# Connect to account
initialize_storage_account(storage_account_name, storage_account_key)

# Create directory contents method
def list_directory_contents(file_system, directory):
    try:
        
        file_system_client = service_client.get_file_system_client(file_system = file_system)

        paths = file_system_client.get_paths(path = directory)

        for path in paths:
            print(path.name + '\n')

    except Exception as e:
     print(e)

# List directory contents
list_directory_contents(file_system, directory)
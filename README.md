# Alteryx ADLS Reader
## Purpose
Lists the contents of a directory in a specific Azure Data Lake Storage bucket. This makes it possible to read multiple files into Alteryx from an ADLS bucket using a Batch Macro.

## Configuration
This package requires a credentials CSV file structured as follows:

| storage_account_name  | storage_account_key | file_system | files |
| ------------- | ------------- | ------------- | ------------- |
| account name  | API key  | bucket name  | directory  |
  
The credentials file should be connected to input #1 of the Python tool in Alteryx:
  
  ![image](https://user-images.githubusercontent.com/86577586/167873774-1bed087e-4cdf-4757-8127-ec611ba4430b.png)

## Resources
https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-directory-file-acl-python
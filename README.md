# Alteryx ADLS Reader
This package requires a credentials CSV file structured as follows:

| storage_account_name  | storage_account_key | file_system | files |
| ------------- | ------------- | ------------- | ------------- |
| <account name>  | <API key>  | <bucket name>  | directory  |
  
The credentials file should be connected to input #1 of the Python tool in Alteryx:
  
  ![image](https://user-images.githubusercontent.com/86577586/167873774-1bed087e-4cdf-4757-8127-ec611ba4430b.png)

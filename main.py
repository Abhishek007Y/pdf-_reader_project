import camelot
import xlwt
import json
# password = "6983827427"
password="0503@5036"


data = camelot.read_pdf("sbi.pdf",password=password,pages='all',flavour='lattice')


print(data)
table_data = []

# Iterate over each table and store the data in the array
# for table in data:
#     table_data.append(table.df.values.tolist())

# # Print the table data
# print(table_data)
# print(json.dumps(table_data))

for table in data:
        # Convert the table to a Pandas DataFrame
        df = table.df
        
        # Extract the data from the DataFrame
        # arr = df.values
        arr = df.replace('\n', '', regex=True).values


        # Define the column names
        column_names = ['TRANSACTION DATE', 'PARTICULARS', 'WITHDRAWLS', 'DEPOSIT', 'BALANCE']

        # Convert the 2D array to a list of dictionaries
        result_list = [dict(zip(column_names, row)) for row in arr[1:].tolist()]

        # Add the extracted data to the list of table data
        table_data.append(result_list)

print(table_data)
import csv
import pandas as pd

df = pd.read_csv('test_data.csv')

# compare_column = df.transaction
# rows, columns = df.shape
# for i in range(columns):
#     print(df.columns[i])

# # print(df.transaction.unique())
trx_list = df.transaction.unique()
message = df.message.unique()
print(trx_list)
print(message)

# for trx in trx_list:
#     for msg in message:
for trx in trx_list:
    print(trx)
    transaction_names = df.loc[df[trx]]
    # transaction_names = df.loc[df['transaction'] == 'TRX001']      
    message_texts = transaction_names.loc[df['message_type'].str.contains("LOGIN|LOGIN_SUCCESS|LOGIN_FAILURE|ORDER_MADE|ORDER_ACCEPTED|ORDER_DELIVERED", case=False)]
    print(message_texts)

  











# a = 'level'
# #String that you want to search
# with open('test_data.csv', 'r') as file:
#     reader = csv.reader(file, delimiter = ',')
#     for line in reader: #Iterates through the rows of your csv
#         print(line) #line here refers to a row in the csv
#         if a in str(line): #If the string you want to search is in the row
#             print("String found in first row of csv")
#         break


# with open('test_data.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=',')
#     columns_list = []

#     for row in reader:
#         columns_list.append(row)
#         break

# print(columns_list[0][7])
# test_csv = pd.read_csv('test_data.csv', usecols=columns_list[0])
# #column = test_csv.transaction
# print(test_csv['transaction'].str.contains('TRX001'))



# transaction = csv.reader(columns_list[0][7])
# print(transaction)




# with open('test_data.csv', 'r') as file:
#     for line in file.readlines():
#         array = line.split(',')
#         first_item = array[0]

#     num_columns = len(array)
#     file.seek(0)

#     reader = csv.reader(file, delimiter=' ')
#     included_cols = [1, 2, 7]

#     for row in reader:
#         content = list(row[i] for i in included_cols)
#         print(content)

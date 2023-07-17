import tabula
import pandas
import numpy


password = "0503@5036"
tabular_data = tabula.read_pdf("sbi.pdf", password=password, pages='all')

df = tabular_data[1].fillna("")
print(list((df.columns.values)))

# print(df)
dfs = []
for i, g in df.groupby(df['Unnamed: 1'].str.startswith('TRANSFER').cumsum()):
    
    # g.reset_index(drop=True, inplace=True)
    # # g=g[1:]
    # # print(g)
    # dfs.append(g) 

    header = g.iloc[0]
    g = g[1:]
    g.columns = header
    g.reset_index(drop=True, inplace=True)
    # print(g)
    dfs.append(g)

# print(dfs)
# print each dataframe separately

list=[]
for i, d in enumerate(dfs):
    if i==0:
        continue

    print(f"DataFrame {i+1}:")  
    # print(d)
    
    head=header["Unnamed: 1"]
    for col in d.columns:
        val=d[col].values
        val.tolist()
        if val not in list:
            list.append(val)    

print(list)

    





# print(list((df.columns.values)))
# print(df)
# dfs = []
# for i, g in df.groupby(df['Unnamed: 1'].str.startswith('TRANSFER').cumsum()):
#     g.reset_index(drop=True, inplace=True)
#     g=g.iloc[1:]
#     dfs.append(g) 
# result_df = pandas.concat(dfs, ignore_index=True)


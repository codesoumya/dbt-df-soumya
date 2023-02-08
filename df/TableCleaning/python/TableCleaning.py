import pandas as pd
import math

df = df_helper.get_table("table")
metadata = df_helper.get_table_metadata("table")

print("Table Name : ",metadata.Name)
# print(metadata.Tags)
# Row Drop With NULL Method
def DropRowWithNull(data: pd.DataFrame, null_percentage=90):
    prevRowCount = len(data.axes[0])
    if null_percentage < 100:
        NullFree = data.dropna(thresh=math.ceil(len(data.columns) * (1 - null_percentage / 100)))
        only_na = data[~data.index.isin(NullFree.index)]
        data = NullFree.reset_index().drop('index', axis=1)
    elif null_percentage == 100:
        NullFree = data.dropna(thresh=1)
        only_na = data[~data.index.isin(NullFree.index)]
        data = NullFree.reset_index().drop('index', axis=1)
    currRowCount = len(data.axes[0])
    print("Number of Row Droped : ",(prevRowCount-currRowCount))   
    print("The Index of Droped Rows : ",list(only_na.index)) 
    return data

# Column drop with nulll value
def DropColumnWithNull(data: pd.DataFrame, null_percentage=90):
    dropedColList = []
    for col in data.columns:
        if data[col].isna().sum() * 100 / len(data[col]) > null_percentage:
            dropedColList.append(col)
            data.drop(col, axis=1, inplace=True)
    print("Number of Column Droped : ",len(dropedColList))
    print("Droped Columns : ",dropedColList)        
    return data

# impute column wise
def ColumnWiseImpute(data: pd.DataFrame):
    counter = 0
    for col in data:
        # if 'ZipCode' or 'telephone' or 'coordinates' in metadata.Columns[counter].Tags:
        #     data[col].fillna('Not Available', inplace=True)
        if 'String' in metadata.Columns[counter].Tags:
            data[col].fillna('NULL', inplace=True)
        elif 'Integer' in metadata.Columns[counter].Tags:
            mean = data[col].mean()
            data[col].fillna(mean, inplace=True)
        elif 'MixedIntegerFloat' or 'Floating' in metadata.Columns[counter].Tags:
            mean = data[col].mean()
            data[col].fillna(mean, inplace=True)
        counter+=1    
    return data  


# Main Execution
def CleanerFunction(df:pd.DataFrame):
    # if 'TableContainsNullValues' in metadata.Tags: # tag checking on Table Meta Data  
    df = DropRowWithNull(df)
    df = DropColumnWithNull(df)
    df = ColumnWiseImpute(df)
    df.drop_duplicates()
    # else :
    #     df_helper.publish(df)
    #     print("Table is Fine")
    # print(df.isnull().sum())
    df_helper.publish(df)
CleanerFunction(df)

      





import pandas as pd

def columns_min_detect(df_temp,minimum_cells):
    keepcols = []
    for column in df_temp.iloc[:,:-1]:
        if df_temp[column].astype(bool).sum(axis=0)>minimum_cells:
            keepcols.append(column)
    return keepcols
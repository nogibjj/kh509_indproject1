import pandas as pd 
import matplotlib.pyplot as plt


def calc_desc_stat(dataset_col):
    out=dataset_col.describe()
    return out

def boxplot_of_cols(df_wanted, col1=None, col2=None, col3=None, file_name=None):
    list_of_columns = []
    if col1:
        list_of_columns.append(col1)
    if col2:
        list_of_columns.append(col2)
    if col3:
        list_of_columns.append(col3)
    if len(list_of_columns) == 0:
        return print("There are no columns to plot")
    
    df_to_plot = df_wanted[list_of_columns]
    ax = df_to_plot.boxplot()
    
    if file_name:
        plt.savefig(file_name)
    plt.savefig("boxplot")
    plt.show()
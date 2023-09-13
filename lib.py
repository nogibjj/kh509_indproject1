import pandas as pd 
import matplotlib.pyplot as plt


def calc_desc_stat(dataset_col):
    out=dataset_col.describe()
    return round(out,2)

def boxplot_of_col(df_wanted, col):
    df_wanted.boxplot(column=col)
    plt.show()
    plt.savefig(str(col.columns) + ".png")
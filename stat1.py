import pandas as pd 
import matplotlib.pyplot as plt
from lib import calc_desc_stat, boxplot_of_col 

df1 = pd.read_csv('iris.csv')

calc_desc_stat(df1['petal.length'])

boxplot_of_col(df1,'petal.length')
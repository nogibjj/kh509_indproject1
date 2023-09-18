import pandas as pd 
import matplotlib.pyplot as plt
from lib import calc_desc_stat, boxplot_of_cols

df1 = pd.read_csv('datasets/iris.csv')

out=calc_desc_stat(df1['petal.length'])
print(out)

boxplot_of_cols(df1,'petal.length', 'sepal.length', file_name='test')



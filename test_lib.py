import pandas as pd 
import math
import numpy as np
import os
from lib import calc_desc_stat, boxplot_of_cols


#we can be sure the calc_desc_stat function is working properly since it passes multiple cases.
#below we calculate the mean, std, and quantile of 25% by hand to confirm the pandas function calc desc stat is working right

def test_mean():
    iris = pd.read_csv('datasets/iris.csv')
    wine = pd.read_csv('datasets/winequality-red.csv')

    iris_out=calc_desc_stat(iris['petal.length'])
    iris_out=round(iris_out,2)
    test_mean_out = round(sum(iris['petal.length']) / len(iris['petal.length']), 2)
    
    assert(iris_out[1] == test_mean_out)


    out2=calc_desc_stat(wine['alcohol'])

    out2=round(out2,2)
    test_mean_out2 = round(sum(wine['alcohol']) / len(wine['alcohol']), 2)

    assert(out2[1] == test_mean_out2)
 
 
def test_std():
    iris = pd.read_csv('datasets/iris.csv')
    wine = pd.read_csv('datasets/winequality-red.csv')

    iris_out=calc_desc_stat(iris['petal.length'])
    mean = np.mean(iris['petal.length'])
    squared_diff = [(x - mean) ** 2 for x in iris['petal.length']]
    mean_squared_diff = np.mean(squared_diff)
    calc_std_deviation = np.sqrt(mean_squared_diff)

    assert round(calc_std_deviation,1) == round(iris_out[2],1)


    out2=calc_desc_stat(wine['alcohol'])
    mean = sum(wine['alcohol']) / len(wine['alcohol'])
    squared_diff = [(x - mean) ** 2 for x in wine['alcohol']]
    mean_squared_diff = sum(squared_diff) / len(squared_diff)
    calc_std_deviation2 = math.sqrt(mean_squared_diff)
    

    assert round(calc_std_deviation2,1) == round(out2[2],1)

def test_quantiles():
    #we will test for the 25% quantile
    iris = pd.read_csv('datasets/iris.csv')
    wine = pd.read_csv('datasets/winequality-red.csv')

    iris_out=calc_desc_stat(iris['petal.length'])
    out2=calc_desc_stat(wine['alcohol'])

    percentile_25 = np.percentile(iris['petal.length'], 25)
    
    assert round(percentile_25,2) == round(iris_out[4],2)


    percentile_25_2 = np.percentile(wine['alcohol'], 25)
    
    assert round(percentile_25_2,2) == round(out2[4],2)


#here will will test the graph

def test_graph():
    result = boxplot_of_cols(None, col1='A', col2='B')
    assert result is None
    data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
    df = pd.DataFrame(data)
    boxplot_of_cols(df, col1='X', file_name='testfunctionality')
    assert os.path.exists('testfunctionality')


if __name__ == "__main__":
    test_quantiles()
    test_graph()
    test_mean()
    test_std()
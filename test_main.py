import pandas as pd
from  lib import calc_desc_stat, boxplot_of_cols

#data = {'Height': [5.1, 6.2, 5.1, 5.2]}

#testing_df = pd.DataFrame(data)
#out=calc_desc_stat(testing_df['Height'])

def test_calc_desc_for_iris():
    data = pd.read_csv("data/iris_data.csv")


    results = calc_desc_stat(data['petal.length'])
    assert 'Target Column' in results
    assert '25th Quantile' in results
    assert 'Mean' in results
    assert 'Median' in results
    assert 'Standard Deviation' in results

def test_does_graph_save():
    df1 = pd.read_csv('datasets/iris.csv')
    boxplot_of_cols(df1, 'petal.length', 'sepal.length', file_name='test.png')
    import os
    assert os.path.exists('test.png')


if __name__ == '__main__':
    test_does_graph_save()
    test_calc_desc_for_iris()

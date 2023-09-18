import pandas as pd
from  lib import calc_desc_stat, boxplot_of_cols

data = {'Height': [5.1, 6.2, 5.1, 5.2]}

testing_df = pd.DataFrame(data)
#out=calc_desc_stat(testing_df['Height'])

def test_calc_desc_for_iris():
    data = pd.read_csv("data/iris_data.csv")


    results = calc_desc_stat(data['petal.length'])
    assert 'Target Column' in results
    assert '25th Quantile' in results
    assert 'Mean' in results
    assert 'Median' in results
    assert 'Standard Deviation' in results

def does_graph_save():
    #boxplot_of_col(testing_df,'Height')
    #assert os.path.isfile("boxplot.png")
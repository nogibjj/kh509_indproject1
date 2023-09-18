import pandas as pd
from  lib import calc_desc_stat, boxplot_of_cols

#data = {'Height': [5.1, 6.2, 5.1, 5.2]}

#testing_df = pd.DataFrame(data)
#out=calc_desc_stat(testing_df['Height'])

def test_calc_desc_for_iris():
    data = pd.read_csv("datasets/iris.csv")
    assert calc_desc_stat(None) == "There is nothing to calculate, please input a dataframe column"
    output=calc_desc_stat(data['petal.length'])
    assert round(output[1],2) == 3.76




def test_does_graph_plot():
    break_list = [1,2,3]
    result = boxplot_of_cols(None, col1='A', col2='B')
    assert result == "This is the wrong input, you have <class 'NoneType'>"

    output = boxplot_of_cols(break_list, col1='A', col2='B')
    assert output == "This is the wrong input, you have <class 'list'>"


if __name__ == '__main__':
    test_does_graph_plot()
    test_calc_desc_for_iris()

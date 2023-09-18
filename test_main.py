import pandas as pd
from  lib import calc_desc_stat, boxplot_of_cols

#data = {'Height': [5.1, 6.2, 5.1, 5.2]}

#testing_df = pd.DataFrame(data)
#out=calc_desc_stat(testing_df['Height'])

def test_calc_desc_for_iris():
    data = pd.read_csv("datasets/iris.csv")
    results = calc_desc_stat(data['petal.length'])



def test_does_graph_plot():
    import os
    df1 = pd.read_csv('datasets/iris.csv')
    test_dir = os.path.dirname(__file__)
    csv_file_path = os.path.join(test_dir, 'datasets', 'iris.csv')
    df1 = pd.read_csv(csv_file_path)
    plot_file_path = os.path.join(test_dir, 'sepal vs petal')
    boxplot_of_cols(df1, 'petal.length', 'sepal.length', file_name=plot_file_path)
    assert os.path.exists(plot_file_path)


if __name__ == '__main__':
    test_does_graph_plot()
    test_calc_desc_for_iris()

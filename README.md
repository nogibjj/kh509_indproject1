# Continuous Integration using GitHub Actions of Python Data Science Project
Individual Project #1
Katelyn Hucker (kh509)

# Summary and Goals
My individual project uses two datasets: wine_quality.csv and iris.csv. The project has the goal to calculate descriptive statistics from a dataframe column, and plot boxplots to compare different columns within a dataframe. The functions are defined in the lib.py file, which are then called in both the jupytr notebooks, stat1.py. The jupytr notebook uses the wine_quality.csv, while stat1.py uses iris.csv. They both perform function calls from the lib.py file. They output graphs and descriptive statistics based on function inputs. 

# Requirements.txt:
### This code uses the following libraries to lint, test, format, plot, and calculate for the project. 

ruff==0.0.284
pytest==7.1.3
black==22.3.0
pandas==2.0.0 
pytest-cov==4.0.0
pylint==2.15.3
matplotlib==3.7.0
nbval==0.10.0
nbqa==1.7.0
boto3==1.24.87


# Worflow 

The project workflow is as followed when a push is made to repo:

- Establish a virtual environment for python3
- Install the dependencies listed above
- Lints code with Rust Ruff linter, as it is faster than pylint
- Format with python black
- Perform test cases to confirm the functions are working properly and user inputs are valid.

# Descriptions of the python files

### lib.py 

lib.py contains the functions calc_desc_stat and boxplot_of_cols. calc_desc_stat takes in a dataframe column and performs the pandas function calculate descriptive statstics. boxplot_of_cols takes in a dataframe, up to three columns, and a file_name flag. The user can determine what they want to plot and what they would like to save the file as. All these optional inputs have defaults as None. The file_name also reverts to a base name if there is not one that is given.  


### stat1.py 

stat1.py uses the iris.csv. It produces the descriptive statistics for the petal.length data. We see important information like mean, quantiles, etc. This is then plotted as a boxplot and compared to the sepal length data within the same dataset. 

### Here is the plot from iris.csv:

![image](https://github.com/nogibjj/kh509_indproject1/assets/143521756/0e7be0d7-c986-4d60-a928-d15eb9e50cb4)


### desc_stat.ipynb

desc_stat.ipynb is a jupyter notebook that performs functions in lib.py on the wine_quality.csv. The notebook outputs what the dataframe looks like and then uses the functions imported from lib.py. We see the descriptive statistics for the alcohol column. This shows the average alcohol content for red wine is 10.42. It also shows the quantiles, min, max, count, std, etc. It then plots 2 boxplots one of alcohol content and one of fixed acidity in the same figure. 

### Here is the plot for wine_quality.csv

![image](https://github.com/nogibjj/kh509_indproject1/assets/143521756/ee646c69-265b-48be-a985-399db0e63e37)


### testing

There are two test files. test_lib.py tests if the functions are working properly by calculating the descriptive statistics by hand and comparing. The test_main.py tests how users interact with the script. It checks if they enter the right or wrong things in the function and then asserts the outputs are correct. 

  

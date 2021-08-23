import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from scipy import stats

warnings.filterwarnings("ignore")

"""
NAME 
    data_inspector
DESCRIPTION
    This module brings different functions to make EDA, data cleaning easier. 
    
MODULE CONTENTS
    1. line_plot
    2. plot_skewed_feature
    3. show_distribution
    4. plot_scatter
    5. plot_correlation
    6. get_correlation (pearson)
    7. histogram 
    8. plot_bar
    9. box_plot
    10. datasetShape
    11. diagnostic_plots
    12. divideFeatures
    13. fillNan
    14. plot_cont_kde
    15. calculating_missing_values
"""


# fucntion to plot line_plot
# Reference: https://notebook.community/mzohaib10/datascience-starters/visualization-in-matplotlib/visualization-in-matplotlib

def line_plot(data, x_data, y_data, x_label="", y_label="", title=""):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(data[x_data], data[y_data], lw = 2, color = '#539caf', alpha = 1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)



# fucntion to plot sample skewed feature
# Refernce: 

def plot_skewed_feature(data, column):
    plt.figure(figsize=(10,4))
    sns.distplot(data[column])
    plt.show()
    
    
# fucntion to show data distributions

def show_distribution(data, column):

    fig, ax = plt.subplots(figsize=(10,5))
    sns.histplot(data, x=column, kde=True, ax=ax)
    plt.show()


# fucntion to show scatter plots
# Reference: https://notebook.community/mzohaib10/datascience-starters/visualization-in-matplotlib/visualization-in-matplotlib
        
def plot_scatter(data,x_data, y_data):

    plt.figure(figsize=(15,5))
    plt.scatter(data[x_data], data[y_data], color='r')
    plt.title(f'{x_data} vs {y_data}', fontsize=15, fontweight='bold')
    plt.xlabel(f'{x_data}', fontsize=15, fontweight='bold')
    plt.ylabel(f'{y_data}', fontsize=15, fontweight='bold')
    plt.grid()
    
    
# fucntion to show correlations
# Reference: https://seaborn.pydata.org/examples/many_pairwise_correlations.html

def plot_correlation(data):
    corr = data.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(corr, mask = mask, annot=True)
    plt.show()

# fucntion to get pearson correlations and P value
# Reference: https://github.com/PacktPublishing/Hands-on-Exploratory-Data-Analysis-with-Python/blob/master/Chapter%2011/Chapter11.ipynb

def get_correlation(column_1, column_2, data):
  pearson_corr, p_value = pearsonr(data[column_1], data[column_2])
  print("Correlation between {} and {} is {}".format(column_1, column_2, pearson_corr))
  print("P-value of this correlation is {}".format(p_value))
  

# fucntion to show histogram
# Reference: https://notebook.community/mzohaib10/datascience-starters/visualization-in-matplotlib/visualization-in-matplotlib
    
def histogram(data,column, x_label, y_label, title):
    _, ax = plt.subplots()
    ax.hist(data[column], color = '#539caf')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

# fucntion to plot bar
# Reference: https://notebook.community/mzohaib10/datascience-starters/visualization-in-matplotlib/visualization-in-matplotlib
    
def plot_bar(data, column, xlabel, ylabel, title):

    ax = data[column].value_counts().sort_values().plot(kind='bar',figsize=(10,5), grid=True)
    ax.set(
        xlabel = xlabel,
        ylabel = ylabel,
        title = title)
    plt.show()
 
# fucntion to create boxplot of all features

 
def box_plot(data):

    plt.subplots(figsize=(15,6))
    data.boxplot(patch_artist=True, sym="k.")
    plt.xticks(rotation=90)
   
# fucntion to get dataset's columns and rows
    
def datasetShape(data):
    rows, cols = data.shape
    print("The dataframe has",rows,"rows and",cols,"columns.")
    
# fucntion to get a total diagnostic result
# Reference: https://www.kaggle.com/asimislam/tutorial-python-subplots
   
def diagnostic_plots(data, variable):
    # function takes a dataframe (df) and
    # the variable of interest as arguments

    # define figure size
    plt.figure(figsize=(25, 5))

    # creating histogram
    plt.subplot(1, 5, 1)
    sns.histplot(data[variable], bins=30)
    plt.title('Histogram')

    # creating Q-Q plot
    plt.subplot(1, 5, 2)
    stats.probplot(data[variable], dist="norm", plot=plt)
    plt.ylabel('Variable quantiles')

    # creating boxplot
    plt.subplot(1, 5, 3)
    sns.boxplot(y=data[variable])
    plt.title('Boxplot')
    
    plt.show()



# function to select numerical and categorical features

def divideFeatures(data):
    numerical_features = data.select_dtypes(include=[np.number])
    categorical_features = data.select_dtypes(include=[np.object])
    return numerical_features, categorical_features


# fucntion to fill the Nan values with a specific value

def fillNan(data, column, value):
    data[column].fillna(value, inplace = True)
    
    
    
 # fucntion to plot kde
 # Reference: https://www.analyticsvidhya.com/blog/2020/10/optimizing-exploratory-data-analysis-using-functions-in-python/
   
    
def plot_cont_kde(data, var, l=10, b=5):
    mini = data[var].min()
    maxi = data[var].max()
    ran = data[var].max()-data[var].min()
    mean = data[var].mean()
    skew = data[var].skew()
    kurt = data[var].kurtosis()
    median = data[var].median()
    st_dev = data[var].std()
    points = mean-st_dev, mean+st_dev
    fig, axes = plt.subplots(1, 2)
    sns.boxplot(data=data, x=var, ax=axes[0])
    sns.distplot(a=data[var], ax=axes[1], color='#ff4125')
    sns.lineplot(points, [0, 0], color='black', label="std_dev")
    sns.scatterplot([mini, maxi], [0, 0],
                    color='orange', label="min/max")
    sns.scatterplot([mean], [0], color='red', label="mean")
    sns.scatterplot([median], [0], color='blue', label="median")
    fig.set_size_inches(l, b)
    plt.title('std_dev = {}; kurtosis = {};nskew = {}; range = {}; nmean = {}; median =  {};'
              .format((round(points[0],2),round(points[1],2)),
                      round(kurt,2),round(skew,2),(round(mini,2),round(maxi,2),
                                round(ran,2)),round(mean,2), round(median,2)))
    

# fucntion to calculate and plot missing values
# Reference: https://stackoverflow.com/questions/51070985/find-out-the-percentage-of-missing-values-in-each-column-in-the-given-dataset

def calculating_missing_values(data):
    missing = data.isna().sum().sort_values(ascending = True)
    missing = missing[missing !=0]
    missing_percentage = missing/data.shape[0]*100
    # return missing, missing_percentage
    if data.isna().any().sum()>0:
        missing, missing_percentage = calculating_missing_values(data)
        missing.plot(kind ='bar', figsize=(30,10))
        plt.title('Missing Values')
        plt.show()
    else:
        print ('No missing values here')
        
        
        
        
# python3 setup.py sdist bdist_wheel
# twine upload --skip-existing dist/*
# twine upload dist/*
'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def bar_plot(pre_universe):

    plt.figure(figsize=(8, 6))
    sns.countplot(data=pre_universe, x='fta')
    plt.title('Bar Plot of FTA')
    plt.xlabel('FTA')
    plt.ylabel('Count')
    plt.savefig('data/part3_plots/bar_plot.png')
    plt.close()


# 2. Hue the previous barplot by sex
def bar_plot_with_hue(pre_universe):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=pre_universe, x='fta', hue='sex')
    plt.title('Bar Plot of FTA by Sex')
    plt.xlabel('FTA')
    plt.ylabel('Count')
    plt.savefig('data/part3_plots/bar_plot_with_hue.png')
    plt.close()


# 3. Plot a histogram of age_at_arrest
def histogram_age(pre_universe):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=pre_universe, x='age_at_arrest')
    plt.title('Histogram of Age at Arrest')
    plt.xlabel('Age at Arrest')
    plt.ylabel('Frequency')
    plt.savefig('data/part3_plots/histogram_age_at_arrest.png')
    plt.close()


# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histogram_age_groups(pre_universe):
    bins = [18, 21, 30, 40, 100]
    labels = ['18–21', '21–30', '30–40', '40+']
    pre_universe['age_group'] = pd.cut(pre_universe['age_at_arrest'], bins=bins, labels=labels, right=False)

    plt.figure(figsize=(8, 6))
    sns.countplot(data=pre_universe, x='age_group', order=labels)
    plt.title('Histogram of Age at Arrest (Grouped)')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.savefig('data/part3_plots/histogram_age_groups.png')
    plt.close()
'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt
##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def cat_plot_felony_rearrest(pre_universe_merged):
    pre_universe_merged['charge_type'] = pre_universe_merged['has_felony_charge'].map({True: 'Felony', False: 'Non-Felony'})
    sns.catplot(data=pre_universe_merged, kind='bar',
                x='charge_type', y='prediction_felony',
                aspect=1.5)
    plt.title('Prediction for Felony Rearrest by Charge Type')
    plt.xlabel('Current Charge Type')
    plt.ylabel('Predicted Felony Rearrest')
    plt.savefig('data/part4_plots/felony_rearrest_prediction.png')
    plt.close()

# 2. Repeat for nonfelony
def cat_plot_nonfelony_rearrest(pre_universe_merged):
    pre_universe_merged['charge_type'] = pre_universe_merged['has_felony_charge'].map({True: 'Felony', False: 'Non-Felony'})
    sns.catplot(data=pre_universe_merged, kind='bar',
                x='charge_type', y='prediction_nonfelony',
                aspect=1.5)
    plt.title('Prediction for Nonfelony Rearrest by Charge Type')
    plt.xlabel('Current Charge Type')
    plt.ylabel('Predicted Nonfelony Rearrest')
    plt.savefig('data/part4_plots/nonfelony_rearrest_prediction.png')
    plt.close()

# In a print statement, answer the following question: What might explain the difference between the plots?
print("What might explain the difference between the plots?")
print("The model predicts that people who have a current felony are more likely to be rearrested for a less serious crime. This could be due to the fact that people with felony charges don't want to be charged again or because they are on probation, have had access to counciling, etc.")


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def cat_plot_felony_rearrest_hue(pre_universe_merged):
    sns.catplot(data=pre_universe_merged, kind='bar',
                x='has_felony_charge', y='prediction_felony',
                hue='y_felony', aspect=1.5)
    plt.title('Prediction for Felony Rearrest by Charge Type and Actual Rearrest')
    plt.xlabel('Has Felony Charge')
    plt.ylabel('Predicted Felony Rearrest')
    plt.savefig('data/part4_plots/felony_rearrest_prediction_hue.png')
    plt.close()
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?
print("What does it mean that prediction for arrestees with a current felony charge, but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, but who did get rearrested for a felony crime?")
print("This shows that the model focuses more on the current charge when making predictions,and how severe they are. So, if someone has a felony charge now, the model gives them a higher risk score even if they don’t actually get rearrested. Meanwhile, someone with a less serious charge might get a lower score, even if they do get rearrested for a felony.")

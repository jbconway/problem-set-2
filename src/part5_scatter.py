'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
def scatterplot_felony_nonfelony(pred_universe):
    plt.clf()
    sns.lmplot(data=pred_universe, x='prediction_felony', y='prediction_nonfelony',
               hue='y_felony', aspect=1.5,palette={True: 'red', False: 'blue'})
    plt.title('Scatter Plot of Felony vs Nonfelony Predictions')
    plt.xlabel('Prediction for Felony Rearrest')
    plt.ylabel('Prediction for Nonfelony Rearrest')
    plt.savefig('data/part5_plots/scatterplot_felony_nonfelony.png')
    plt.close()
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
print("What can you say about the group of dots on the right side of the plot?")
print("There are more red dots on the right side of the plot which means that people who have a current felony charge are predicited to more likely have a rearrest for both a felony and nonfelony charge")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
def scatterplot_felony_rearrest(pred_universe):
    sns.scatterplot(data=pred_universe, x='prediction_felony', y='y_felony', alpha=0.6)
    plt.title('Scatter Plot of Felony Rearrest Prediction vs Actual Rearrest')
    plt.xlabel('Prediction for Felony Rearrest')
    plt.ylabel('Actual Felony Rearrest')
    plt.savefig('data/part5_plots/scatterplot_felony_rearrest.png')
    plt.close()
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
print("Would you say based off of this plot if the model is calibrated or not?")
print("The model seems somewhat calibrated because people with higher predicted scores are more likely to have actually been rearrested. But it’s not perfect, since those with lower predicted scores did still get rearrested.")

# BAR CHART 1: Average Total Sick Days Per Town
# Question: Which town had the highest average total sick days?

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
df = pd.read_excel('sickle_cell_dataset_100_rows.xlsx')

# Step 2: Check the data loaded correctly
print(df.head())

avg_sick_days = df.groupby('Town')['Total Sick Days'].mean().round()
print(avg_sick_days)


# Step 5: Plot the bar chart
avg_sick_days.plot(kind='bar', color=['steelblue', 'coral', 'mediumseagreen'], edgecolor='black')

# Step 6: Add labels and title
plt.title('Average Total Sick Days Per Town', fontsize=14)
plt.xlabel('Town', fontsize=12)
plt.ylabel('Average Sick Days', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('average_sick_days_per_town.png')


#I OMMITTED BAR CHART 2


# BAR CHART 3: Median Hemoglobin Level by Sickle Cell Type
# Question: Do children with HbSS have lower typical hemoglobin than HbSC?

# Check the sickle cell types in our data
print(df['Sickle_Cell_Type'].unique())
print(df['Sickle_Cell_Type'].value_counts())

# Group by Sickle_Cell_Type, calculate median hemoglobin
median_hb = df.groupby('Sickle_Cell_Type')['Hemoglobin_Level_g_dL'].median()

print(median_hb)

# Plot
median_hb.plot(kind='bar', color=['mediumorchid', 'crimson'], edgecolor='black')

plt.title('Median Hemoglobin Level by Sickle Cell Type', fontsize=14)
plt.xlabel('Sickle Cell Type', fontsize=12)
plt.ylabel('Median Hemoglobin (g/dL)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('median_hemoglobin_level_by_cell_type.jpg')





#PIE CHARTS OF OUR THREE CHARTS







# PIE CHART: Average Total Sick Days Per Town
# Same question, different visualization: Which town had the highest average total sick days?

# Step 3: Plot the pie chart
plt.figure(figsize=(7, 7))

avg_sick_days.plot(
    kind='pie',
    colors=['steelblue', 'coral', 'mediumseagreen'],
    autopct='%1.1f%%',
    startangle=90,
    
)

# Step 4: Add title and clean up
plt.title('Average Total Sick Days Per Town', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.savefig('average_sick_days_pie_chart.png')
plt.show()
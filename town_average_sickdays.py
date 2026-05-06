# BAR CHART 1: Average Total Sick Days Per Town
# Question: Which town had the highest average total sick days?

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('sickle_cell_dataset_100_rows.xlsx')

# LINE GRAPH: Number of Diagnoses Per Year
# Question: How has the number of diagnoses changed over the years?
# Count diagnoses per year


diagnoses_per_year = df.groupby('Diagnosis_Year')['Child_ID'].count()
print(diagnoses_per_year)

# Create the line graph
plt.figure(figsize=(8, 5))

# LINE GRAPH: The Shortcut Method
# Step 1: Calculate the summary
diagnoses_per_year = df.groupby('Diagnosis_Year')['Child_ID'].count()

# Step 2: Create the line graph using the .plot shortcut
# We just change kind='bar' to kind='line'
diagnoses_per_year.plot(
    kind='line', 
    color='steelblue', 
    marker='o', 
    linewidth=2
)

# Step 3: Add labels and title (Same as before)
plt.title('Number of Diagnoses Per Year', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Children Diagnosed', fontsize=12)

plt.tight_layout()
plt.show()

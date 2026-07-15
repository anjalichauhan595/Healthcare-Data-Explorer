import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/heart.csv")

# Preview the first five rows
print(df.head())

# Display the dataset dimensions
print("\nDataset shape:")
print(df.shape)

# Display the column names
print("\nColumn names:")
print(df.columns)

# Data types of each column
# This helped in identifying categoriacal and numerical columns for further analysis
print("\nData types:")
print(df.dtypes)

# Understanding the summary statistics of the dataset
print("\nSummary statistics:")
print(df.describe())

# Determining whether there is a target = 1 pr presence of heart diesease means that the average age of the patients is higher
print("\nAverage age of patients with heart disease (target=1):")
print(df.groupby('target')['age'].mean())

# Checking why there are 1025 rows when there are around 300 patients
print(df.duplicated().sum())
'''The answer shows that there are actually only 302 patients. 1025 (originalentries) - 723 (duplicates) = 302 (unique patients). 
This is important to know because it means that the dataset has been duplicated multiple times, 
which could affect the analysis and results. It is important to remove duplicates before proceeding with
any further analysis.'''

# Removing duplicates from the dataset
''' 
print("\nExample duplicated rows:")
print(df[df.duplicated()].head())
duplicate() creates true/false labels for each row
df[df.duplicated()] this shows the rows where duplicated is truue
head is shows the 5 duplicated rows

This output does not show the correct response because duplicates occur much later
print("\nAll duplicated records (including the originals):")
print(df[df.duplicated(keep=False)].head(10))

So the next step is find the duplicates.
To do we will filter for the known duplicated record using several column conditions.

'''
df_clean = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df_clean.shape)

'''
Duplicates can affect the averages. Therefore, we must re-check age by heart disease status.
'''
print("\nAverage age by heart disease status after removing duplicates:")
print(df_clean.groupby("target")["age"].mean())

'''
According to this dataset, patients with heart disease have lower mean age as compared to patients without heart disease.
This does not align with my initial hypothesis and must not be interpreted as a general medical conclusion.
'''

plt.hist(df_clean["age"])

plt.title("Age Distribution of Patients")
plt.xlabel("Age (years)")
plt.ylabel("Number of Patients")

plt.savefig("outputs/age_distribution_histogram.png")

plt.show()
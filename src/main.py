from data_loader import load_data
from data_cleaning import remove_duplicates
from exploratory_analysis import display_dataset_overview, summarize_dataset
from visualization import (plot_age_distribution, plot_age_by_heart_disease, plot_correlation_heatmap)

df = load_data("data/heart.csv")
df_cleaned = remove_duplicates(df)
display_dataset_overview(df_cleaned)
summarize_dataset(df_cleaned)
plot_age_distribution(df_cleaned)
plot_age_by_heart_disease(df_cleaned)
plot_correlation_heatmap(df_cleaned)

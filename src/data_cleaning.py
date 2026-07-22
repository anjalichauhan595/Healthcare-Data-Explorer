def remove_duplicates(df):
    duplicate_count = df.duplicated().sum()
    print(f"Removed {duplicate_count} duplicate rows from the dataset.")

    df_cleaned = df.drop_duplicates()
    return df_cleaned

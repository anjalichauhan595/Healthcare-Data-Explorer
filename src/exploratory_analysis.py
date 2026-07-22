def display_dataset_overview(df):
    print("=" * 50)
    print("DATASET OVERVIEW")
    print("=" * 50)

    print("First 5 rows of the dataset:")
    print(df.head(5))

    print("\nDataset shape:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns)

    print("\nData types:")
    print(df.dtypes)

    print()

def summarize_dataset(df):
   
    print("=" * 50)
    print("SUMMARY STATISTICS")
    print("=" * 50)

    print(df.describe())

    print()
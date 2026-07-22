import matplotlib.pyplot as plt


def plot_age_distribution(df):
    plt.figure(figsize=(8, 6))
    plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age Distribution in the Cleveland Heart Disease Dataset')

    plt.tight_layout()
    plt.savefig('outputs/age_distribution_histogram.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_age_by_heart_disease(df):
    plt.figure(figsize=(8, 6))

    #Filter the dataset
    ages_with_disease = df[df['target'] == 1]['age']
    ages_without_disease = df[df['target'] == 0]['age']

    #Create boxplot
    plt.boxplot([ages_with_disease, ages_without_disease], tick_labels=['With Heart Disease', 'Without Heart Disease'])
    plt.xlabel('Heart Disease Status')
    plt.ylabel('Age')
    plt.title('Age Distribution by Heart Disease Status')
    plt.tight_layout()
    plt.savefig('outputs/age_by_heart_disease_boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()
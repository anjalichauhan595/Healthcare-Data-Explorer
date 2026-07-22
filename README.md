# 🫀 Healthcare Data Explorer

## Project Overview

The Healthcare Data Explorer is a Python-based data analysis project that explores the Cleveland Heart Disease dataset. The project demonstrates a complete exploratory data analysis (EDA) workflow, including data loading, cleaning, visualization, and statistical exploration using a modular software design.

The goal of this project was to explore the Cleveland Heart Disease dataset through a reproducible exploratory data analysis (EDA) pipeline while applying software engineering best practices such as modular programming, version control, and data visualization.
---


## Dataset

This project uses the **Cleveland Heart Disease Dataset**, a widely used dataset for machine learning and healthcare analytics.

The dataset contains patient information including:

* Age
* Sex
* Chest pain type
* Resting blood pressure
* Cholesterol
* Fasting blood sugar
* Resting ECG results
* Maximum heart rate
* Exercise-induced angina
* ST depression (oldpeak)
* Number of major vessels
* Thalassemia status
* Heart disease diagnosis (target)

---

## Project Structure

```text
Healthcare-Data-Explorer/
│
├── data/
│   └── heart.csv
│
├── outputs/
│   ├── age_distribution_histogram.png
│   ├── age_by_heart_disease_boxplot.png
│   └── correlation_matrix_heatmap.png
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   ├── visualization.py
│   └── main.py
│
├── README.md
└── .gitignore
```

---

## Features

* Load the Cleveland Heart Disease dataset
* Detect and remove duplicate records
* Display dataset overview
* Generate summary statistics
* Visualize age distribution with a histogram
* Compare age distributions using a box plot
* Explore relationships between variables using a correlation heatmap
* Organize analysis into reusable Python modules

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Git
* GitHub
* VS Code

---

## Key Findings

During the exploratory analysis:

* The original dataset contained a large number of duplicate records, which were removed before analysis.
* Patients with and without heart disease showed different age distributions.
* Correlation analysis highlighted relationships between several clinical variables and heart disease, while also demonstrating the importance of interpreting correlations carefully.
* Because this dataset is observational, the results identify associations rather than causal relationships.

---

## Lessons Learned

This project strengthened my understanding of:

* Modular Python programming
* Data cleaning workflows
* Exploratory Data Analysis (EDA)
* Data visualization
* Git version control
* Scientific interpretation of healthcare data
* Building reproducible data analysis pipelines

---

## Future Improvements

Potential future extensions include:

* Interactive dashboard using Streamlit
* Machine learning models for heart disease prediction
* Feature importance analysis
* ROC curve evaluation
* Additional statistical hypothesis testing

---

## Running the Project

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd Healthcare-Data-Explorer
```

Run the analysis pipeline:

```bash
python src/main.py
```

Generated visualizations will be saved in the `outputs/` directory.

---

## Author

**Anjali Chauhan**

Master's Student in Bioinformatics at San Jose State UNiversity

This project was created as part of a portfolio focused on applying software engineering principles to biological and healthcare data analysis.


import pandas as pd

# Part 01: Overview

# Load data
filepath = '../data/Sleep_health_and_lifestyle_dataset.csv'
data = pd.read_csv(filepath)

# Clear data
data_df = data[['Quality of Sleep', 'Stress Level']]

# Part 02: Descriptive Statistics

# Calculate the variance
variance_df = pd.DataFrame(data_df.var()).transpose()
variance_df.index = ['variance']

# Calculate IQR
Q1 = data_df.quantile(0.25)
Q3 = data_df.quantile(0.75)
IQR = Q3 - Q1

IQR_df = pd.DataFrame(IQR).transpose()
IQR_df.index = ['IQR']

# Calculate Range
Range = data_df.max() - data_df.min()
Range_df = pd.DataFrame(Range).transpose()
Range_df.index = ['Range']

descriptive_stat_df = pd.concat([data_df.describe(), variance_df, IQR_df, Range_df])


def extract_measures(column_name, input_df):
    extracted_stat = input_df[column_name]

    extracted_stat = {
        "count": extracted_stat['count'],
        "mean": extracted_stat['mean'],
        "std": extracted_stat['std'],
        "min": extracted_stat['min'],
        "25%": extracted_stat['25%'],
        "50%": extracted_stat['50%'],
        "75%": extracted_stat['75%'],
        "max": extracted_stat['max'],
        "var": extracted_stat['var'],
        "IQR": extracted_stat['IQR'],
        "Range": extracted_stat['Range']
    }
    return extracted_stat

col1_ext = extract_measures('Stress Level', descriptive_stat_df)
col2_ext = extract_measures('Quality of Sleep', descriptive_stat_df)
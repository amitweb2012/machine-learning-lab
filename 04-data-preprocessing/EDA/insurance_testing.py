# EDA(Exploratory Data Analysis) for insurance dataset

import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import warnings
from scipy.stats import pearsonr

warnings.filterwarnings('ignore')

df = pd.read_csv('insurance.csv')

print(df.shape, df.head(), df.info(), df.describe(), sep='\n\n')
print(df.columns, sep='\n\n')
print(df.isnull().sum(), sep='\n\n')

numeric_columns = ['age', 'bmi', 'children','charges']
categorical_columns = ['sex', 'smoker', 'region']

# for col in numeric_columns:
#     plt.figure(figsize=(10, 5))
#     sns.histplot(df[col], kde=True)
#     plt.title(f'Distribution of {col}')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.show()

# for col in categorical_columns:
#     plt.figure(figsize=(10, 5))
#     sns.countplot(data=df, x=col)
#     plt.title(f'Distribution of {col}')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.show()

# optional: heartmap to visualize correlations
# for col in numeric_columns:
#     plt.figure(figsize= (6,4))
#     sns.boxplot(x = df[col])
#     plt.title(f'Distribution of {col}')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.show()

# find correlation between numeric columns
# correlation_matrix = df[numeric_columns].corr()
# plt.figure(figsize=(8, 6))
# sns.heatmap(df.corr(numeric_only=True),annot=True)
# # sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Correlation Matrix of Numeric Columns')
# plt.show()

# Data Cleaning and preprocessing

df_cleaned = df.copy()
# cleaning the data by removing duplicates and handling missing values
df_cleaned.drop_duplicates(inplace=True)
df_cleaned.dropna(inplace=True)
print(df_cleaned.shape, df_cleaned.head(), df_cleaned.info(), df_cleaned.describe(), sep='\n\n')
print(df_cleaned.isnull().sum(), sep='\n\n')
print(df_cleaned.columns, df_cleaned.dtypes, sep='\n\n')
print(df_cleaned['age'].unique(), df_cleaned['bmi'].unique(), df_cleaned['children'].unique(), df_cleaned['charges'].unique(), sep='\n\n')
# converting categorical columns value sex and smoker to 1 and 0, and region to 0,1,2,3
df_cleaned['sex'] = df_cleaned['sex'].map({'male': 1, 'female': 0})
df_cleaned['smoker'] = df_cleaned['smoker'].map({'yes': 1, 'no': 0})
df_cleaned['region'] = df_cleaned['region'].map({'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3})
df_cleaned['age'] = df_cleaned['age'].astype('int64')
df_cleaned['charges'] = df_cleaned['charges'].astype('int64')
df_cleaned['children'] = df_cleaned['children'].astype('int64')
df_cleaned['bmi'] = df_cleaned['bmi'].round(2)
df_cleaned.rename(columns={'sex' :'is_female','smoker': 'is_smoker','region': 'region_code'},inplace = True)
df_cleaned.head()

print(df_cleaned.head())
print(df['region'].value_counts(), df_cleaned['region_code'].value_counts(), sep='\n\n')

# Preprocessing for region column and back value 0,1,2,3 to northwest, northeast, southwest, southeast

df_cleaned['region_code'] = df_cleaned['region_code'].map({0: 'northwest', 1: 'northeast', 2: 'southwest', 3: 'southeast'})
df_cleaned.rename(columns={'region_code': 'region'}, inplace=True)
df_cleaned = pd.get_dummies(df_cleaned,columns = ['region'],drop_first=True)
print(df_cleaned.head())
df_cleaned = df_cleaned.astype(int)
print(df_cleaned.head())
df_cleaned.to_csv('insurance_cleaned_after_all_onehot.csv', index=False)

# Feature Engineering and Extraction
# sns.histplot(df['bmi'])
# plt.show()

df_cleaned['bmi'] = df_cleaned['bmi'].astype(int)
df_cleaned['bmi'].value_counts()

# BMI categories and feature engineering bacause human body mass index (BMI) is a measure of body fat 
# based on height and weight that applies to adult men and women. 
# It is calculated by dividing a person's weight in kilograms by the square of their height in meters. 
# The resulting number is then used to categorize individuals into different BMI categories, 
# which can provide insight into their overall health and risk for certain health conditions.
# and it's ranges are as follows:
# Underweight: BMI < 18.5
# Normal weight: 18.5 <= BMI < 25
# Overweight: 25 <= BMI < 30
# Obesity: BMI >= 30
# def bmi_category(bmi):
#     if bmi < 18.5:
#         return 'Underweight'
#     elif 18.5 <= bmi < 25:
#         return 'Normal'
#     elif 25 <= bmi < 30:
#         return 'Overweight'
#     else:
#         return 'Obesity'

# df_cleaned['bmi_category'] = df_cleaned['bmi'].apply(bmi_category)
# print(df_cleaned.head())

# Categorize BMI using the same lower-inclusive boundaries as the function above.
df_cleaned['bmi_category'] = pd.cut(
    df_cleaned['bmi'],
    bins=[-np.inf, 18.5, 25, 30, np.inf],
    labels=['Underweight', 'Normal', 'Overweight', 'Obesity'],
    right=False
)
print(df_cleaned.head())

# one hot encoding
df_cleaned = pd.get_dummies(df_cleaned, columns=['bmi_category'], drop_first=False)
print(df_cleaned.head())

# change to int type
df_cleaned = df_cleaned.astype(int)
print(df_cleaned.head())
print(df_cleaned.info())

df_cleaned.to_csv('insurance_cleaned_after_all_onehot.csv', index=False)

# Feature scaling and normalization
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_cleaned['age'] = scaler.fit_transform(df_cleaned[['age']])
df_cleaned['bmi'] = scaler.fit_transform(df_cleaned[['bmi']])
df_cleaned['children'] = scaler.fit_transform(df_cleaned[['children']])

print(df_cleaned.head())
df_cleaned.to_csv('insurance_cleaned_after_feature_scaling.csv', index=False)


# What is the correlation between the features and the target variable 'charges'?
# Correlation is a statistical measure that indicates the strength and direction of the linear relationship between two variables.
# It ranges from -1 to 1, where:
# - A value of 1 indicates a perfect positive linear relationship (as one variable increases,
# - A value of -1 indicates a perfect negative linear relationship (as one variable increases, the other decreases),
# - A value of 0 indicates no linear relationship.

# Pearson correlation coefficient
# The Pearson correlation coefficient is a measure of the linear relationship between two variables. It ranges from -1 to 1, where:
# - A value of 1 indicates a perfect positive linear relationship (as one variable increases,
# - A value of -1 indicates a perfect negative linear relationship (as one variable increases, the other decreases),
# - A value of 0 indicates no linear relationship.

selected_features = [
    'age', 'bmi', 'children', 'is_female', 'is_smoker',
    'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_Underweight', 'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obesity'
]

correlations = {
    feature: pearsonr(df_cleaned[feature], df_cleaned['charges'])[0]
    for feature in selected_features
}
correlation_df = pd.DataFrame(list(correlations.items()), columns=['Feature', 'Pearson Correlation'])
correlation_df.sort_values(by='Pearson Correlation', ascending=False)
print(correlation_df)

# Checking the correlation between features and target variable 'charges' using heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df_cleaned.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Features and Target Variable')
plt.show()

# Chi-square test of independence for categorical features and target variable 'charges'
from scipy.stats import chi2_contingency

categorical_features = ['is_female', 'is_smoker', 'region_northwest', 'region_southeast', 'region_southwest']
alpha = 0.05

df_cleaned['charges_bin'] = pd.qcut(df_cleaned['charges'], q=4, labels=False)
chi2_results = {}

for col in categorical_features:
    contingency = pd.crosstab(df_cleaned[col], df_cleaned['charges_bin'])
    chi2_stat, p_val, _, _ = chi2_contingency(contingency)
    decision = 'Reject Null (Keep Feature)' if p_val < alpha else 'Accept Null (Drop Feature)'
    chi2_results[col] = {
        'chi2_statistic': chi2_stat,
        'p_value': p_val,
        'Decision': decision
    }

chi2_df = pd.DataFrame(chi2_results).T
chi2_df = chi2_df.sort_values(by='p_value')
print(chi2_df)
final_df = df_cleaned[['age', 'is_female', 'bmi', 'children', 'is_smoker', 'charges','region_southeast','bmi_category_Obesity']]
print(final_df.head())
final_df.to_csv('insurance_cleaned_after_feature_selection.csv', index=False)


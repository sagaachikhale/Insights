# -*- coding: utf-8 -*-
"""Project1TechSus.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DDNCkOPQX8k4WsH5QNLvKEzTvvEPU9rZ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

path = '/content/drive/MyDrive/Project 1/Technology & Sustainability/AI Preparedness Index Dataset.csv'
df = pd.read_csv(path, encoding='latin-1')
df.head(1)

df.info()

df['ISO'].nunique()

df.isnull().sum()

df[df.isnull().any(axis=1)]

df.loc[72,'Individuals using the Internet (% of population)'] = 51.5

df.dropna(inplace=True)

df[df['Country'] == 'India']

df.duplicated().sum()

################################################################################################################################################################################

df.head(1)

"""# **Use following tables to see top 5 and bottom 5 AIPI**"""

top_5_countries = df.sort_values(by='AI preparedness Index', ascending=False).head(5)

print("Top 5 Countries by AI Preparedness Index:")
top_5_countries[['Country', 'AI preparedness Index']].reset_index(drop=True)
## India's rank is 72 and China's rank is 30 and Russia's rank is 45

bottom_5_countries = df.sort_values(by='AI preparedness Index', ascending=True).head(5)
print("\nBottom 5 Countries by AI Preparedness Index:")
bottom_5_countries[['Country', 'AI preparedness Index']].reset_index(drop=True)

top_5_countries_gdp = df.sort_values(by='GDP per capita (current US$)', ascending=False).head(5)

print("Top 5 Countries by GDP per capita:")
top_5_countries_gdp[['Country', 'GDP per capita (current US$)']].reset_index(drop=True)

correlation_columns = [ 'AI preparedness Index',  'GDP per capita (current US$)', 'GDP per capita growth (annual %)', 'Innovation and Economic Integration', 'Digitial Infrastructure',  'Regulation and Ethics','Human Capital and Labor Market Policies']
corr_df = df[correlation_columns]
correlation_matrix = corr_df.corr()
ai_corr = correlation_matrix['AI preparedness Index'].drop('AI preparedness Index')

print("Correlation of AI Preparedness Index with other variables:")
ai_corr

plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

"""# **AIPI vs GDP**"""

AIPI_GDP_Corr = df['AI preparedness Index'].corr(df['GDP per capita (current US$)'])
AIPI_GDP_Corr

plt.figure(figsize=(8,6))
sns.regplot(  data=df, x='GDP per capita (current US$)',y='AI preparedness Index', scatter_kws={'alpha':0.6}, line_kws={'color':'red'})

plt.title('AI Preparedness Index vs GDP per Capita', fontsize=14)
plt.xlabel('GDP per Capita (current US$)', fontsize=12)
plt.ylabel('AI Preparedness Index', fontsize=12)
plt.grid(True)
plt.show()

correlation = df['AI preparedness Index'].corr(df['GDP per capita (current US$)'])
print(f"Correlation between AI Preparedness Index and GDP per Capita: {correlation:.2f}")

top_10_countries = df.sort_values(by='AI preparedness Index', ascending=False).head(10)
top_10_countries = top_10_countries.rename(columns={'Country':'Country_AIPI', 'AI preparedness Index':'AIPI'})
top_10_countries = top_10_countries[['Country_AIPI', 'AIPI']].reset_index(drop=True)

top_10_countries_GDP = df.sort_values(by='GDP per capita (current US$)', ascending=False).head(10)
top_10_countries_GDP = top_10_countries_GDP.rename(columns={'Country':'Country_GDP', 'GDP per capita (current US$)':'GDP'})
top_10_countries_GDP = top_10_countries_GDP[['Country_GDP', 'GDP']].reset_index(drop=True)

combined_table = pd.concat([top_10_countries, top_10_countries_GDP], axis=1)

print("Top 10 Countries by AI Preparedness Index and GDP per Capita:")
combined_table

"""# **AIPI vs GDP per capita growth**"""

AIPI_GDP_Growth_Corr = df['AI preparedness Index'].corr(df['GDP per capita growth (annual %)'])
AIPI_GDP_Growth_Corr
# approx -0.19

plt.figure(figsize=(8,6))
sns.regplot( data=df, x='GDP per capita growth (annual %)',  y='AI preparedness Index',  scatter_kws={'alpha':0.6}, line_kws={'color':'red'})

plt.title('GDP per Capita Growth vs AI Preparedness Index', fontsize=14)
plt.xlabel('GDP per capita growth (annual %)', fontsize=12)
plt.ylabel('AI preparedness Index', fontsize=12)
plt.grid(True)
plt.show()

correlation = df['AI preparedness Index'].corr(df['GDP per capita growth (annual %)'])
print(f"Correlation between AI Preparedness Index and GDP per Capita Growth: {correlation:.2f}")

"""# **APIP vs Digitial Infrastructure**"""

df.head(1)

AIPI_Digi_inter_Corr = df['AI preparedness Index'].corr(df['Secure Internet servers (per 1 million people)'])
AIPI_Digi_inter_Corr

AIPI_Digi_infra_Corr = df['AI preparedness Index'].corr(df['Digitial Infrastructure'])
AIPI_Digi_infra_Corr

plt.figure(figsize=(8,6))
sns.regplot( data=df,  x='Digitial Infrastructure', y='AI preparedness Index',scatter_kws={'alpha':0.6},line_kws={'color':'red'})

plt.title('Digital Infrastructure vs AI Preparedness Index', fontsize=14)
plt.xlabel('Digital Infrastructure', fontsize=12)
plt.ylabel('AI preparedness Index', fontsize=12)
plt.grid(True)
plt.show()

correlation = df['AI preparedness Index'].corr(df['Digitial Infrastructure'])
print(f"Correlation between AI Preparedness Index and Digital Infrastructure: {correlation:.2f}")

top_10_countries = df.sort_values(by='AI preparedness Index', ascending=False).head(10)
top_10_countries = top_10_countries.rename(columns={'Country':'Country_AIPI', 'AI preparedness Index':'AIPI'})
top_10_countries = top_10_countries[['Country_AIPI', 'AIPI']].reset_index(drop=True)

top_10_countries_Digi = df.sort_values(by='Digitial Infrastructure', ascending=False).head(10)
top_10_countries_Digi = top_10_countries_Digi.rename(columns={'Country':'Country_Digi', 'Digitial Infrastructure':'Digi'})
top_10_countries_Digi = top_10_countries_Digi[['Country_Digi', 'Digi']].reset_index(drop=True)

combined_table1 = pd.concat([top_10_countries, top_10_countries_Digi], axis=1)

print("Top 10 Countries by AI Preparedness Index and Digitial Infrastructure:")
combined_table1

"""# **AIPI vs Regulation and Ethics**"""

AIPI_Regulations_Corr = df['AI preparedness Index'].corr(df['Regulation and Ethics'])
AIPI_Regulations_Corr

plt.figure(figsize=(8,6))
sns.regplot(  data=df, x='Regulation and Ethics', y='AI preparedness Index',scatter_kws={'alpha':0.6},line_kws={'color':'red'})

plt.title('Regulation and Ethics vs AI Preparedness Index', fontsize=14)
plt.xlabel('Regulation and Ethics', fontsize=12)
plt.ylabel('AI preparedness Index', fontsize=12)
plt.grid(True)
plt.show()

correlation = df['AI preparedness Index'].corr(df['Regulation and Ethics'])
print(f"Correlation between AI Preparedness Index and Regulation and Ethics: {correlation:.2f}")

top_10_countries = df.sort_values(by='AI preparedness Index', ascending=False).head(10)
top_10_countries = top_10_countries.rename(columns={'Country':'Country_AIPI', 'AI preparedness Index':'AIPI'})
top_10_countries = top_10_countries[['Country_AIPI', 'AIPI']].reset_index(drop=True)

top_10_countries_Regulations = df.sort_values(by='Regulation and Ethics', ascending=False).head(10)
top_10_countries_Regulations = top_10_countries_Regulations.rename(columns={'Country':'Country_Regulations', 'Regulation and Ethics':'Regulations_Ethics'})
top_10_countries_Regulations = top_10_countries_Regulations[['Country_Regulations', 'Regulations_Ethics']].reset_index(drop=True)

combined_table2 = pd.concat([top_10_countries, top_10_countries_Regulations], axis=1)

print("Top 10 Countries by AI Preparedness Index and Regulation and Ethics:")
combined_table2

"""# **AIPI vs Human Capital and Labor Market Policies**"""

AIPI_HR_Corr = df['AI preparedness Index'].corr(df['Human Capital and Labor Market Policies'])
AIPI_HR_Corr

plt.figure(figsize=(8,6))
sns.regplot(  data=df,  x='Human Capital and Labor Market Policies', y='AI preparedness Index', scatter_kws={'alpha':0.6}, line_kws={'color':'red'})

plt.title('Human Capital and Labor Market Policies vs AI Preparedness Index', fontsize=14)
plt.xlabel('Human Capital and Labor Market Policies', fontsize=12)
plt.ylabel('AI preparedness Index', fontsize=12)
plt.grid(True)
plt.show()

correlation = df['AI preparedness Index'].corr(df['Human Capital and Labor Market Policies'])
print(f"Correlation between AI Preparedness Index and Human Capital and Labor Market Policies: {correlation:.2f}")

top_10_countries = df.sort_values(by='AI preparedness Index', ascending=False).head(10)
top_10_countries = top_10_countries.rename(columns={'Country':'Country_AIPI', 'AI preparedness Index':'AIPI'})
top_10_countries = top_10_countries[['Country_AIPI', 'AIPI']].reset_index(drop=True)

top_10_countries_HC_LMP = df.sort_values(by='Human Capital and Labor Market Policies', ascending=False).head(10)
top_10_countries_HC_LMP = top_10_countries_HC_LMP.rename(columns={'Country':'Country_HC_LMP', 'Human Capital and Labor Market Policies':'HC_LMP'})
top_10_countries_HC_LMP = top_10_countries_HC_LMP[['Country_HC_LMP', 'HC_LMP']].reset_index(drop=True)

combined_table3 = pd.concat([top_10_countries, top_10_countries_HC_LMP], axis=1)
print("Top 10 Countries by AI Preparedness Index and Human Capital and Labor Market Policies:")
combined_table3

"""# **AIPI vs Innovation and Economic Integration**"""

df.head(1)

AIPI_Innov_Corr = df['AI preparedness Index'].corr(df['Innovation and Economic Integration'])
AIPI_Innov_Corr

plt.figure(figsize=(8,6))
sns.regplot( data=df,  x='Innovation and Economic Integration', y='AI preparedness Index', scatter_kws={'alpha':0.6}, line_kws={'color':'red'})

plt.title('Innovation & Economic Integration vs AI Preparedness Index', fontsize=14)
plt.xlabel('Innovation and Economic Integration', fontsize=12)
plt.ylabel('AI preparedness Index', fontsize=12)
plt.grid(True)
plt.show()

correlation = df['AI preparedness Index'].corr(df['Innovation and Economic Integration'])
print(f"Correlation between AI Preparedness Index and Innovation & Economic Integration: {correlation:.2f}")

"""# **Corr between GDP and other parameters except AIPI**"""

df.head(1)

correlation_columnss = [ 'GDP per capita (current US$)', 'Innovation and Economic Integration','Digitial Infrastructure', 'Regulation and Ethics', 'Human Capital and Labor Market Policies']
corr_dff = df[correlation_columnss]

correlation_matrixx = corr_dff.corr()
gdp_corr = correlation_matrixx['GDP per capita (current US$)'].drop('GDP per capita (current US$)')

print("Correlation of GDP per capita (current US$) with other variables except AIPI:")
gdp_corr
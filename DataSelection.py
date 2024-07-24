import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

def confusion_anaylsis(df):
    correlation_matrix = df.corr()

    precipcover_corr = correlation_matrix[['precipcover']].sort_values(by='precipcover', ascending=False)
    long_corr = correlation_matrix[['long']].sort_values(by='long', ascending=False)
    lat_corr = correlation_matrix[['lat']].sort_values(by='lat', ascending=False)

    combined_corr = pd.concat([precipcover_corr, long_corr, lat_corr], axis=1)
    filtered_combined_corr = combined_corr[(combined_corr.abs() > 0.2).any(axis=1)]

    print(filtered_combined_corr)

    # precipcover_corr = correlation_matrix[['precipcover']].sort_values(by='precipcover', ascending=False)
    # precipcover_corr = precipcover_corr[abs(precipcover_corr) > 0.2].dropna()
    # print(precipcover_corr)

    plt.figure(figsize=(10, 6))
    sns.heatmap(precipcover_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation with precipcover')
    plt.show()
    return

def read_data(directory = "merged_data.xlsx"):
    df = pd.read_excel(directory)
    
    df = df.select_dtypes(include=['number'])
    df = df.drop(['snow', 'snowdepth', 'moonphase'], axis=1)

    df.fillna(0, inplace=True)
    
    confusion_anaylsis(df)
    return df


read_data()
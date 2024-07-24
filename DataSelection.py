import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

def confusion_anaylsis(df):
    correlation_matrix = df.corr()

    precipcover_corr = correlation_matrix[['precipcover']].sort_values(by='precipcover', ascending=False)

    print(precipcover_corr)

    plt.figure(figsize=(10, 6))
    sns.heatmap(precipcover_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation with precipcover')
    plt.show()
    return

def read_data(directory = "raindata/raindata2023-2024.csv"):
    df = pd.read_csv(directory)
    print(df)
    
    df = df.select_dtypes(include=['number'])
    df = df.drop(['snow', 'snowdepth', 'moonphase'], axis=1)

    df.fillna(0, inplace=True)
    
    confusion_anaylsis(df)
    return df


read_data()
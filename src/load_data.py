import pandas as pd
import seaborn as sns

def load_iris_data():
    df = sns.load_dataset('iris')
    df = df.dropna()
    return df

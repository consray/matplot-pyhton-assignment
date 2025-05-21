def basic_stats(df):
    return df.describe()

def group_by_species(df):
    return df.groupby('species').mean()

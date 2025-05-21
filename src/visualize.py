import matplotlib.pyplot as plt
import seaborn as sns

def line_chart(df):
    plt.plot(df.index, df['sepal_length'], label='Sepal Length')
    plt.plot(df.index, df['petal_length'], label='Petal Length')
    plt.title('Trend of Sepal and Petal Lengths')
    plt.xlabel('Index')
    plt.ylabel('Length (cm)')
    plt.legend()
    plt.tight_layout()
    plt.show()

def bar_chart(df):
    df.groupby('species')['petal_length'].mean().plot(kind='bar', color='skyblue')
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.tight_layout()
    plt.show()

def histogram(df):
    plt.hist(df['sepal_width'], bins=10, color='lightgreen', edgecolor='black')
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def scatter_plot(df):
    sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.tight_layout()
    plt.show()

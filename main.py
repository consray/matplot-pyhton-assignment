from src.load_data import load_iris_data
from src.analysis import basic_stats, group_by_species
from src.visualize import line_chart, bar_chart, histogram, scatter_plot

df = load_iris_data()
print(basic_stats(df))
print(group_by_species(df))

line_chart(df)
bar_chart(df)
histogram(df)
scatter_plot(df)

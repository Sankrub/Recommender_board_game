import pandas as pd


class Graph:
    def __init__(self, csv_name):
        self.data = pd.read_csv(csv_name)

    def create_histogram(self, fig, ax):
        ax.clear()
        ax.hist(self.data['average'], bins=20)
        ax.set_xlabel('Average Rating')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of Average Rating')

    def create_boxplot(self, fig, ax):
        ax.clear()
        self.data.boxplot(column=['average'], ax=ax)
        ax.set_ylabel('Average Rating')
        ax.set_title('Boxplot of Average Rating')

    def create_scatterplot(self, fig, ax):
        ax.clear()
        self.data.plot(kind='scatter', x='minage', y='average', ax=ax)
        ax.set_xlabel('Minimum Age')
        ax.set_ylabel('Average Rating')
        ax.set_title('Scatterplot of Average Rating vs Minimum Age')

    def get_histogram_data(self):
        return self.data['average']

    def get_boxplot_data(self):
        return self.data['average']

    def get_scatterplot_data(self):
        return self.data[['minage', 'average']]

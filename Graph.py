import pandas as pd
import seaborn as sns
from collections import defaultdict
import ast
class Graph:
    def __init__(self, csv_name):
        self.data = pd.read_csv(csv_name)
        self.data['boardgameartist'] = self.data['boardgameartist'].apply(
            lambda x: ast.literal_eval(x) if pd.notnull(x) else [])
        self.artist_to_games = defaultdict(list)
        for idx, row in self.data.iterrows():
            for artist in row['boardgameartist']:
                self.artist_to_games[artist].append(row['name'])
        self.artist_counts = {artist: len(games) for artist, games in self.artist_to_games.items()}
        self.artist_df = pd.DataFrame(list(self.artist_counts.items()), columns=['Artist', 'Game Count'])
        self.artist_df = self.artist_df.sort_values('Game Count', ascending=True)

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

    def create_bar_chart(self, fig, ax):
        ax.clear()
        if 'Artist' in self.artist_df.columns and 'Game Count' in self.artist_df.columns:
            sns.barplot(x='Game Count', y='Artist', data=self.artist_df.tail(20), palette='viridis', ax=ax)
            ax.set_xlabel('Number of Games')
            ax.set_ylabel('Artist')
            ax.set_title('Number of Games by Artist')
            ax.set_yticklabels(ax.get_yticklabels(), rotation=45)
            ax.tick_params(axis='y', labelsize=6)

        else:
            raise ValueError("The data does not contain the necessary columns.")


    def get_histogram_data(self):
        return self.data['average']

    def get_boxplot_data(self):
        return self.data['average']

    def get_scatterplot_data(self):
        return self.data[['minage', 'average']]

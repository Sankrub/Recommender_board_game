import pandas as pd


class Data:
    def __init__(self, csv_name):
        self.data = pd.read_csv(csv_name)

    def get_top_recommendations(self, min_players, max_players, min_age, min_playtime, max_playtime):
        filtered_games = self.data[
            (self.data['minplayers'] <= min_players) &
            (self.data['maxplayers'] >= max_players) &
            (self.data['minage'] <= min_age) &
            (self.data['minplaytime'] >= min_playtime) &
            (self.data['maxplaytime'] <= max_playtime)
            ]
        top_games = filtered_games.nlargest(10, 'average')
        return top_games

    def get_game_info(self, game_name):
        game_row = self.data.loc[self.data['name'] == game_name]
        print(game_row)
        if game_row.empty:
            return None
        game_description = game_row['description'].values[0]
        return game_description

        # Create an instance of the Data class

    def find_min(self):
        min_play = min(self.data["minplayers"])
        max_play = max(self.data["minplayers"])
        return min_play, max_play

    def find_max(self):
        min_play = min(self.data["maxplayers"])
        max_play = max(self.data["maxplayers"])
        return min_play, max_play


data = Data('boardgames1.csv')

# Get top recommendations based on user-defined criteria
min_players = 3
max_players = 50
min_age = 7
min_playtime = 10
max_playtime = 120

top_recommendations = data.get_top_recommendations(min_players, max_players, min_age, min_playtime, max_playtime)
print(top_recommendations)
for index, game_name in enumerate(top_recommendations['name']):
    print(f"{index + 1}. {game_name}")

# game_name = 'Gloomhaven'
# game_des = data.get_game_info(game_name)
# print(game_des)

# one, two = data.find_max()
# print(one, two)
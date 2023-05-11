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

    def get_game_info(self, game_idx, top_games):
        game_idx -= 1
        if 0 <= game_idx < len(top_games):
            game_name = top_games["name"].iloc[game_idx]
            game_description = top_games['description'].iloc[game_idx]
            return game_name, game_description
        else:
            return None, None

    def get_top_by_average(self, n=30):
        top_games = self.data.nlargest(n, 'average')
        return top_games

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
# min_players = 3
# max_players = 50
# min_age = 7
# min_playtime = 10
# max_playtime = 120

# top_recommendations = data.get_top_recommendations(min_players, max_players, min_age, min_playtime, max_playtime)
# print(top_recommendations)
# for index, game_name in enumerate(top_recommendations['name']):
#     print(f"{index + 1}. {game_name}")

# game_name = 'Gloomhaven'
# game_des = data.get_game_info(game_name)
# print(game_des)

# one, two = data.find_max()
# print(one, two)

top_30_games = data.get_top_by_average()
print(top_30_games)
for index, game_name in enumerate(top_30_games['name']):
    print(f"{index + 1}. {game_name}")

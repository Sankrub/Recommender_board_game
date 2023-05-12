import pandas as pd


class Data:
    def __init__(self, csv_name):
        self.data = pd.read_csv(csv_name)

    def get_top_recommendations(self, min_players, max_players, min_age, min_playtime, max_playtime):
        """
        Get top 10 games from user input
        :param min_players: minimum player int
        :param max_players: maximum player int
        :param min_age: minimum age int
        :param min_playtime: minimum play time int
        :param max_playtime: maximum play time int
        :return:
        """
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
        """
        get game description by there index
        :param game_idx: games index
        :param top_games: list of the games
        :return: game name and description
        """
        game_idx -= 1
        if 0 <= game_idx < len(top_games):
            game_name = top_games["name"].iloc[game_idx]
            game_description = top_games['description'].iloc[game_idx]
            return game_name, game_description
        else:
            return None, None

    def get_top_by_average(self, n=30):
        """
        Find top 30 games by there average
        :param n: number of games want to find default 30
        :return: list of 30 games
        """
        top_games = self.data.nlargest(n, 'average')
        return top_games


data = Data('boardgames1.csv')




import pandas as pd
import random

# Загрузка данных из CSV-файла
data = pd.read_csv(r'C:\Users\slinm\Desktop\Новая папка\Football_Result_Predict\football_scores.csv')


# Функция для высчитывания вероятности победы, поражения, ничьи и вероятного счета для пары команд
def calculate_probability(home_team, guest_team):
    home_team_data = data[data['Home'] == home_team]
    guest_team_data = data[data['Guest'] == guest_team]

    # Вычисление вероятности победы
    total_games = home_team_data.shape[0]
    home_team_wins = home_team_data[home_team_data['Home Score'] > home_team_data['Guest Score']].shape[0]
    home_team_win_probability = home_team_wins / total_games

    # Вычисление вероятности поражения
    home_team_losses = home_team_data[home_team_data['Home Score'] < home_team_data['Guest Score']].shape[0]
    home_team_loss_probability = home_team_losses / total_games

    # Вычисление вероятности ничьи
    home_team_draws = home_team_data[home_team_data['Home Score'] == home_team_data['Guest Score']].shape[0]
    home_team_draw_probability = home_team_draws / total_games

    # Вычисление вероятного счета
    home_team_avg_scored = home_team_data['Home Score'].mean()
    home_team_avg_conceded = home_team_data['Guest Score'].mean()
    guest_team_avg_scored = guest_team_data['Guest Score'].mean()
    guest_team_avg_conceded = guest_team_data['Home Score'].mean()

    home_team_expected_score = home_team_avg_scored * guest_team_avg_conceded / home_team_avg_conceded
    guest_team_expected_score = guest_team_avg_scored * home_team_avg_conceded / guest_team_avg_conceded

    return home_team_win_probability, home_team_loss_probability, home_team_draw_probability, home_team_expected_score, guest_team_expected_score


# Ввод названий команд пользователем
# home_team = input("Введите название домашней команды: ")
# guest_team = input("Введите название гостевой команды: ")

# Вычисление вероятностей победы, поражения, ничьи и вероятного счета
# win_probability, loss_probability, draw_probability, home_team_expected_score, guest_team_expected_score = calculate_probability(home_team, guest_team)


# # Вывод результатов
# print("Вероятность победы команды", home_team, "над командой", guest_team, ":", win_probability)
# print("Вероятность поражения команды", home_team, "от команды", guest_team, ":", loss_probability)
# print("Вероятность ничьей между командами", home_team, "и", guest_team, ":", draw_probability)
# print("Ожидаемый счет для команды", home_team, ":", home_team_expected_score)
# print("Ожидаемый счет для команды", guest_team, ":", guest_team_expected_score)

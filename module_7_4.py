
# входные данные

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = ''

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# использование %

result1 = "В команде Мастера кода участников: %s ! " % team1_num
print(result1)
result2 = "Итого сегодня в командах участников: %s и %s !" % (team1_num,team2_num)
print(result2)

 # использование формат

result3 = "Команда Волшебники данных решили задач:{}!".format(score_2)
print(result3)
result4 = "Команда Волшебники данных решили задачи за {} с!".format(team1_time)
print(result4)

# использование f строки

result5 = f'Команды решили {score_1} и {score_2} задач.'
print(result5)
result6 = f'Результат битвы:{challenge_result}!'
print(result6)
result7 = f'Сегодня было решено {tasks_total} задач в среднем по {time_avg} секунды на задачу!.'
print(result7)


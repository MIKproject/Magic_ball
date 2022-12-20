#  Подключаем модуль рандом, time, tqdm
from random import *
import time
from tqdm import tqdm
from colorama import init
init()
from colorama import Fore

#  Создаем список progressbar
mylist = [1, 2, 3]

#  Создаем список ответов
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно", "Ничего нельзя, а все можно"]

#  Приветсвенное сообщение
print('Привет, Я - Magic Ball , и я знаю ответ на любой твой вопрос.')

# Узнаем имя пользователя
name_user = input('Как Вас зовут? ')

#  Приветствуем пользователя
print(f'Привет, {name_user}!')

while True:
    question = input(f'{name_user}, задайте свой вопрос: ') #  Запрашиваем вопрос у пользователя
    for i in tqdm(mylist): #  Включаем progressbar
        time.sleep(1)
    print(Fore.LIGHTMAGENTA_EX + choice(answers)) #  Случайный ответ пользователю из списка answers
    init(autoreset=True)
    question_again = input('Имеются еще вопросы (да/нет): ') #  Спрашиваем пользователя
    if question_again in 'да': #  Если да, повторяем цикл
        continue
    else:
        break #  Если нет, то обрываем цикл

print('Возвращайся если возникнут вопросы!') #  Прощаемся с пользователем

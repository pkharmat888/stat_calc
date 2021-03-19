import pandas as pd
import numpy as np
from termcolor import cprint


class StatExamplesCounter:

    def __init__(self):
        self.data_list = []
        self.prumer = 0
        self.prumer_exponentiation = 0
        self.smerodatna_odchylka = 0
        self.rozptyl = 0
        self.variacni_koeficient = 0
        self.variacni_rozpeti = 0
        self.relativni_prumerna_odchylka = 0
        self.variacni_koeficient_relativni_prumerne_odchylky = 0

    def data_inputting(self):
        cprint('Введите числа поочередно через пробел', color='green')
        while not self.data_list:
            try:
                user_input = input('Введите число: ')
                user_input = map(float, user_input.split())
                self.data_list.extend(user_input)
                print(self.data_list)
            except ValueError as exc:
                print(f'Ошибка типа  - "{exc}". Вы должны ввести числа.')

    def variacni_rozpeti_counting(self):
        maximum = max(self.data_list)
        minimum = min(self.data_list)
        self.variacni_rozpeti = maximum - minimum
        print(f'Variacni rozpeti = "{self.variacni_rozpeti}"')

    def relativni_prumerna_odchylka_counting(self):
        list_delta_x = []
        for number in self.data_list:
            delta_x = abs(number - self.prumer)
            list_delta_x.append(delta_x)
        delta_x_celkem = sum(list_delta_x)
        self.relativni_prumerna_odchylka = delta_x_celkem / len(list_delta_x)
        print(f'Relativni prumerna odchylka "d" = "{round(self.relativni_prumerna_odchylka, 5)}"')

    def variacni_koeficient_relativni_prumerne_odchylky_counting(self):
        self.variacni_koeficient_relativni_prumerne_odchylky = (self.relativni_prumerna_odchylka / self.prumer) * 100
        print(f'"d%" = "{round(self.variacni_koeficient_relativni_prumerne_odchylky, 9)} %"')

    def prumer_counting(self):
        self.prumer = np.mean(self.data_list)
        print(f'Prumer = "{self.prumer}"')

    def rozptyl_counting(self):
        summa = 0
        for number in self.data_list:
            number_exponentiation = number ** 2
            summa += number_exponentiation
        self.rozptyl = summa / len(self.data_list)
        self.rozptyl = self.rozptyl - self.prumer_exponentiation
        print(f'Rozptyl = "{self.rozptyl}"')

    def prumer_exponentiation_counting(self):
        self.prumer_exponentiation = self.prumer ** 2

    def smerodatna_odchylka_counting(self):
        res = np.sqrt(self.rozptyl)
        res = complex(res)
        self.smerodatna_odchylka = round(res.real, 9)
        print(f'Směrodatná odchylka = "{self.smerodatna_odchylka}"')

    def variacni_koeficient_counting(self):
        self.variacni_koeficient = (self.smerodatna_odchylka / self.prumer) * 100
        print(f'Variabilita = "{round(self.variacni_koeficient, 9)} %"')

    def global_counting(self):
        self.data_inputting()
        self.variacni_rozpeti_counting()
        self.prumer_counting()
        self.relativni_prumerna_odchylka_counting()
        self.variacni_koeficient_relativni_prumerne_odchylky_counting()
        self.prumer_exponentiation_counting()
        self.rozptyl_counting()
        self.smerodatna_odchylka_counting()
        self.variacni_koeficient_counting()


class StatExamplesCounterV2(StatExamplesCounter):

    def __init__(self):
        super().__init__()
        self.pocet_list = []

    def intervals_inputting(self):
        cprint('Введите числа поочередно через пробел', color='green')
        while True:
            try:
                user_input = input('Вводите интервалы в скобочках. Пример - "(xx, xx)": ')
                if user_input == 'end':
                    break
                user_input = list(map(float, user_input.split()))
                a, b = user_input
                interval_prumer = (a + b)/2
                self.data_list.append(interval_prumer)
            except ValueError as exc:
                print(f'Ошибка типа  - "{exc}". Вы должны ввести числа.')
        print(self.data_list)

    def pocet_inputting(self):
        cprint('Введите числа поочередно через пробел', color='green')
        while not self.pocet_list:
            try:
                user_input = input('Вводите числа: ')
                user_input = list(map(int, user_input.split()))
                self.pocet_list.extend(user_input)
            except ValueError as exc:
                print(f'Ошибка типа  - "{exc}". Вы должны ввести числа.')
        print(self.pocet_list)

    def prumer_counting(self):
        prumer = [interval * pocet for interval, pocet in zip(self.data_list, self.pocet_list)]
        self.prumer = sum(prumer)/sum(self.pocet_list)
        print(f'Intervalovy prumer {self.prumer}')

    def rozptyl_counting(self):
        rozpt = [(interval**2) * pocet for interval, pocet in zip(self.data_list, self.pocet_list)]
        rozpt = sum(rozpt) / sum(self.pocet_list)
        self.rozptyl = rozpt - self.prumer_exponentiation
        print(f'Rozptyl = "{self.rozptyl}"')

    def global_counting(self):
        self.intervals_inputting()
        self.pocet_inputting()
        self.variacni_rozpeti_counting()
        self.prumer_counting()
        self.relativni_prumerna_odchylka_counting()
        self.variacni_koeficient_relativni_prumerne_odchylky_counting()
        self.prumer_exponentiation_counting()
        self.rozptyl_counting()
        self.smerodatna_odchylka_counting()
        self.variacni_koeficient_counting()

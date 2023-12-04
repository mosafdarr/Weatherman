from Calculations import Calculations
from Parser import MONTHS
from math import ceil
from termcolor import colored


class Reports:
    def __init__(self):
        self.calculations = Calculations()

    def annual_report(self, year):
        min_temp, max_temp, max_humidity = self.calculations.annual_calculation(year)
        print(
            "Highest: ",
            max_temp["max_temperature"],
            "C on ",
            MONTHS[max_temp["max_temp_month"] - 1],
            max_temp["max_temp_day"],
        )
        print(
            "Lowest: ",
            min_temp["min_temperature"],
            "C on ",
            MONTHS[min_temp["min_temp_month"] - 1],
            min_temp["min_temp_day"],
        )

        # There's one problem that kept occuring when i was coding that this humidity value never changes
        # but the days and month keep changing. despite reading the code for many time i kept on facing the same mistake
        print(
            "Humidity: ",
            max_humidity["max_humidity"],
            "% on ",
            MONTHS[max_humidity["max_humidity_month"] - 1],
            max_humidity["max_humidity_day"],
        )

        return True

    def monthly_report(self, year, month):
        min_temps, max_temps, mean_humidities = self.calculations.monthly_calculation(
            year, month
        )
        print("Highest Average: ", ceil(max_temps["avg_temp_max"]), "C")
        print("Lowest Average: ", ceil(min_temps["avg_temp_min"]), "C")
        print(
            "Average Mean Humidity: ", ceil(mean_humidities["avg_humidity_mean"]), "%"
        )

    def bar_chart_report(self, year, month):
        min_temperature, max_temperature = self.calculations.bar_chart_calculation(
            year, month
        )
        for val in range(min_temperature):
            text = colored("-", "red", attrs=["reverse", "blink"])
            print(text, end="")
        print(min_temperature, "C")

        for val in range(max_temperature):
            text = colored("+", "blue", attrs=["reverse", "blink"])
            print(text, end="")
        print(max_temperature, "C")

from Parser import Parser
from Parser import MIN_TEMP, MAX_TEMP, MAX_HUMIDITY, MEAN_HUMIDITY


class Calculations:
    def __init__(self) -> None:
        self.__parser__ = Parser()

    def annual_calculation(self, year):
        min_temp = {
            "min_temperature": 65537,
            "min_temp_month": 0,
            "temperature": 0,
            "min_temp_day": 0,
        }

        max_temp = {
            "max_temperature": -65537,
            "max_temp_month": 0,
            "temperature": 0,
            "max_temp_day": 0,
        }

        max_humidity = {
            "max_humidity": -65537,
            "max_humidity_month": 0,
            "humidity": 0,
            "max_humidity_day": 0,
        }

        # MIN_TEMP
        for month_key, days_data in MIN_TEMP[year].items():
            for day, temp in days_data.items():
                if temp == "" or temp == " ":
                    continue
                temperature = int(temp)
                if temperature > min_temp["min_temperature"]:
                    continue
                min_temp["min_temp_day"] = day
                min_temp["min_temperature"] = temperature
                min_temp["min_temp_month"] = month_key

        # MAX_TEMP
        for month_key, days_data in MAX_TEMP[year].items():
            for day, temp in days_data.items():
                if temp == "" or temp == " ":
                    continue
                temperature = int(temp)
                if temperature < max_temp["max_temperature"]:
                    continue
                max_temp["max_temp_day"] = day
                max_temp["max_temperature"] = temperature
                max_temp["max_temp_month"] = month_key

        # MAX_Humidity
        for month_key, days_data in MAX_HUMIDITY[year].items():
            for day, temp_humidity in days_data.items():
                if temp_humidity == "" or temp_humidity == " ":
                    continue
                humidity = int(temp_humidity)
                if humidity > max_humidity["max_humidity"]:
                    max_humidity["max_humidity"] = humidity
                    max_humidity["max_humidity_month"] = month_key
                    max_humidity["max_humidity_day"] = day

        temperatures = [min_temp, max_temp, max_humidity]
        return temperatures

    def monthly_calculation(self, year, month):
        max_temps = {"highest_temp_list": [], "avg_temp_max": 0, "sum_max_temp": 0}
        min_temps = {"lowest_temp_list": [], "avg_temp_min": 0, "sum_min_temp": 0}
        mean_humidities = {
            "mean_humidity_list": [],
            "avg_humidity_mean": 0,
            "sum_mean_humidity": 0,
        }

        # MAX Temp List
        for temp in MAX_TEMP[year][month].values():
            if temp == "" or temp == " ":
                continue
            temperature = int(temp)
            max_temps["highest_temp_list"].append(temperature)

        for val in max_temps["highest_temp_list"]:
            max_temps["sum_max_temp"] += val

        max_temps["avg_temp_max"] = max_temps["sum_max_temp"] / len(
            max_temps["highest_temp_list"]
        )

        # MIM Temp List
        for temp in MIN_TEMP[year][month].values():
            if temp == "" or temp == " ":
                continue
            temperature = int(temp)
            min_temps["lowest_temp_list"].append(temperature)

        for val in min_temps["lowest_temp_list"]:
            min_temps["sum_min_temp"] += val

        min_temps["avg_temp_min"] = min_temps["sum_min_temp"] / len(
            min_temps["lowest_temp_list"]
        )

        # Mean Humidity List
        for humidity_temp in MEAN_HUMIDITY[year][month].values():
            if humidity_temp == "" or humidity_temp == " ":
                continue
            humidity = int(humidity_temp)
            mean_humidities["mean_humidity_list"].append(humidity)

        for val in mean_humidities["mean_humidity_list"]:
            mean_humidities["sum_mean_humidity"] += val

        mean_humidities["avg_humidity_mean"] = mean_humidities[
            "sum_mean_humidity"
        ] / len(mean_humidities["mean_humidity_list"])
        avg_temperatures = [min_temps, max_temps, mean_humidities]
        return avg_temperatures

    def bar_chart_calculation(self, year, month):
        min_temperature = 65537
        max_temperature = 0

        # MIN_TEMP
        for temp in MIN_TEMP[year][month].values():
            if temp == "" or temp == " ":
                continue
            temperature = int(temp)
            if temperature > min_temperature:
                continue
            min_temperature = temperature

        # MAX_TEMP
        for temp in MAX_TEMP[year][month].values():
            if temp == "" or temp == " ":
                continue
            temperature = int(temp)
            if temperature < max_temperature:
                continue
            max_temperature = temperature

        return [min_temperature, max_temperature]

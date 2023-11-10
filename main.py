import requests
from pprint import pprint


token = "0b52a5b549b387b411cb1955969d0978"


def get_weather(city, token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        print(f"In city: {city} we see metrics in {cur_weather} gradus")

    except Exception as ex:
        print(ex)
        print("Check name of your city")


def main():
    city = input("Enter city name: ")
    get_weather(city, token)


if __name__ == "__main__":
    main()

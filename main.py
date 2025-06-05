from utils.model import research_stations
from utils.controller import get_stations_info, add_station, remove_station


def main():
    print("=========MENU========")
    print("0 - zakończ program")
    print("1 - wyświetl dane stacji badawczych")
    print("2 - dodaj stacje badawczą")
    print("3 - usuń stacje badawczą")
    print("===========================")
    while True:
        choice: str = input("wybierz opcje menu ")
        if choice == "0": break
        if choice == "1": get_stations_info(research_stations)
        if choice == "2": add_station(research_stations)
        if choice == "3": remove_station(research_stations)


if __name__ == "__main__":
    main()

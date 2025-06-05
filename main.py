from utils.model import research_stations
from utils.controller import get_stations_info


def main():
    print("=========MENU========")
    print("0 - zakończ program")
    print("1 - wyświetl dane stacji badawczych")
    print("===========================")
    while True:
        choice: str = input("wybierz opcje menu ")
        if choice == "0": break
        elif choice == "1": get_stations_info(research_stations)


main()

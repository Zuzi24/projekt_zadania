
def get_stations_info( stations_data : list ) -> None:
    for station in stations_data:
        print(f"{station['name']} : {station['location']}" )



def add_station(stations_data : list ) -> None:
    new_station: str = input("podaj nazwe nowej stacji badawczą")
    new_location: str = input("podaj lokalizacje")
    stations_data.append({"name": new_station, "location": new_location})

def get_stations_info( stations_data : list ) -> None:
    for station in stations_data:
        print(f"{station['name']} : {station['location']}" )

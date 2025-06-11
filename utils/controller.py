from folium import folium


def get_stations_info( stations_data : list ) -> None:
    for station in stations_data:
        print(f"{station['name']} : {station['location']}" )



def add_station(stations_data : list ) -> None:
    new_station: str = input("podaj nazwe nowej stacji badawczą")
    new_location: str = input("podaj lokalizacje")
    stations_data.append({"name": new_station, "location": new_location})


def remove_station(stations_data : list ) -> None:
    station_name: str = input("podaj nazwe stacji badawczej do usunięcia")
    for station in stations_data:
        if station["name"] == station_name:
            stations_data.remove(station)



def update_station(stations_data : list ) -> None:
    station_name: str = input("podaj nazwe stacji badawczej do aktualizacji")
    for station in stations_data:
        if station["name"] == station_name:
            station["name"] = input("podaj nową nazwe stacji badawczej")
            station["location"] = input("podaj nową lokalizacje")



def get_coordinates(city_name: str) -> list:
    import requests
    from bs4 import BeautifulSoup
    url = f"https://pl.wikipedia.org/wiki/{city_name}"
    response = requests.get(url).text
    response_html = BeautifulSoup(response, "html.parser")
    latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
    longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
    print(latitude, longitude)
    return [latitude, longitude]

def get_map(stations_data : list) -> None:
    import folium
    mapa = folium.Map(location=[52.21, 21.0], zoom_start=6)
    for station in stations_data:
        print(station["location"])


folium.Marker(
            location=get_coordinates(station["location"]),
            popup=f"{station["location"]} {station['name']}",
        ).add_to(mapa)
    mapa.save('mapa.html')
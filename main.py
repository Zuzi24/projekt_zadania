

research_stations : list =[

    {"name" : "Instytut_Centrum_Zdrowia_Matki_Polki" , "location": "Łódź" },
    {"name" : "Instytut_Fizjologii_i_Patologii_Słuchu" , "location": "Warszawa"},
    {"name" : "Instytut_Chemicznej_Przeróbki_Węgla" , "location": "Zabrze"},
    {"name" : "Instytut_Wymiaru_Sprawiedliwości" , "location": "Warszawa" },

]

def get_stations_info( stations_data : list ) -> None:
    for station in stations_data:
        print(f"{station['name']} : {station['location']}" )


get_stations_info( research_stations )

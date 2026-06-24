#Q1
import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=63ed8d1ff41123c3f5808b8adad286ba&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        for key, value in data["main"].items():
            print(f"{key.capitalize()}: {value}")
        #print(data["main"])
    except requests.exceptions.RequestException as e:
        print(e)


city=input("Enter the city name: ")
weather_data(city)
print("City name:",city)
print("Temperature in Celsius:", weather_data(city))

#Q2
import random
choice=["rock","paper","scissors"]
uscore=0
cscore=0


for i in range(5):
    user_choice = input("Enter your choice ( rock,  paper, scissors): ")
    cch=random.choice(choice)
    print("User choice:",user_choice)
    print("Computer choice:",cch)

    if user_choice==cch:
        print("Draw")
    elif((user_choice=='rock' and cch=='scissors') or (user_choice=='paper' and cch=='rock') or (user_choice=='scissors' and cch=='paper')):
        print("User wins!")
        uscore+=1
    else:
        print("Computer wins!")
        cscore+=1

print("User score:",uscore)
print("Computer score:",cscore)

#Q3

place=input("Enter place name:")
url=f"https://api.maptiler.com/geocoding/{place}.json?key=HAeCN24PQsIkV7XXLrLo"
res= requests.get(url)
data=res.json()
if len(data['features'])>0:

    result=data["features"][0]

    place_name=result["place_name"]
    long=result["center"][0]
    lat=result["center"][1]

    print("\nPlace found:")
    print("Place:",place_name)
    print("Latitudes:",lat)
    print("Longitudes:",long)
else:
    print("Place not found")

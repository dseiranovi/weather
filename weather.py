# e59475c2c0764771ce3e64353294fb92
# You MUST provide a valid API key


#place = input("Sheiyvanet qalaqis saxeli: ")

from pyowm import OWM

owm = OWM('e59475c2c0764771ce3e64353294fb92')

place = input("Sheiyvanet qalaqis saxeli: ")

# Search for current weather in London (Great Britain)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("\nqalaq " + place + " axla " + str(temp) + " gradusia")

if temp < 10:
    print ("\nmagrad civa arayi gadakari =D")
elif temp < 25:
    print ("\nacivda rame unda shemoicva")
else:
    print("normaluri temperatur rogorc ginda ise chaicvi")

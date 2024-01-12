# Created hotel_cost function
def hotel_cost(num_days, rate):
    return num_days * rate


# Created plane_cost function
def plane_cost(city):
    if city == "Madrid":
        price = 150
        return price
    elif city == "Krakow":
        price = 200
        return price
    elif city == "Lisbon":
        price = 220
        return price
    elif city == "Paris":
        price = 300
        return price
    elif city == "Rome":
        price = 280
        return price
    elif city == "Berlin":
        price = 270
        return price
    elif city == "Prague":
        price = 240
        return price
    else:
        print("Unable to find destination, please check your spelling")


# Created plane_cost function
def car_rental(num_days):
    return num_days * 22


# Created plane_cost function
def holiday_cost(hotel, plane, car):
    return hotel + plane + car


# Collecting input from users
print()
print("Welcome to ..::Holiday costs calculator::..\n")
print("Where would you like to go for your city break ??\n")
print("You can choose one of the fallowing destination:\n")
print("Madrid, Krakow, Lisbon, Paris, Rome, Berlin, Prague\n")
city_flight = input("Please choose your flight destination: ")
num_nights = input("How many nights would you like to stay: ")
rental_day = input("For how many days would you like hire a car: ")

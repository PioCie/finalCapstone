# Defined functions hotel_cost
def hotel_cost(num_days, rate):
    return num_days * rate


# Defined functions plane_cost
def plane_cost(city):
    if city == "madrid":
        price = 150
        return price
    elif city == "krakow":
        price = 200
        return price
    elif city == "lisbon":
        price = 220
        return price
    elif city == "paris":
        price = 300
        return price
    elif city == "rome":
        price = 280
        return price
    elif city == "berlin":
        price = 270
        return price
    elif city == "prague":
        price = 240
        return price
    else:
        print("Unable to find destination, please check your spelling")


# Defined functions car_rental
def car_rental(num_days):
    return num_days * 22


# Defined functions holiday_cost
def holiday_cost(hotel, plane, car):
    return hotel + plane + car


# Collecting input from users
print()
print("Welcome to ..::Holiday costs calculator::..\n")
print("Where would you like to go for your city break ??\n")
print("You can choose one of the fallowing destination:\n")
print("Madrid, Krakow, Lisbon, Paris, Rome, Berlin, Prague\n")
city_flight = input("Please choose your flight destination: ").lower()
num_nights = input("How many nights would you like to stay: ")
rental_day = input("For how many days would you like hire a car: ")
print()
print("Great choose, It will be great holiday")
print(f"The flight price to your destination is {plane_cost(city_flight)}£.")


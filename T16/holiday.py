# Defined functions hotel_cost
def hotel_cost(num_days, rate):
    return num_days * rate


# Defined functions plane_cost
def plane_cost(select):
        if select == 1:
            city = "Madrid"
            price = 150
            return price, city
        elif select == 2:
            city = "Krakow"
            price = 180
            return price, city
        elif select == 3:
            city = "Lisbon"
            price = 220
            return price, city
        elif select == 4:
            city = "Paris"
            price = 300
            return price, city
        elif select == 5:
            city = "Rome"
            price = 275
            return price, city
        elif select == 6:
            city = "Berlin"
            price = 160
            return price, city
        elif select == 7:
            city = "Prague"
            price = 145
            return price, city
        else:
            print("Unable to find destination, please check your spelling")



# Defined functions car_rental
def car_rental(num_days):
    return num_days * 22


# Defined functions holiday_cost
def holiday_cost(hotel, plane, car):
    return hotel + plane + car


# Defined functions create_frame
def create_frame():
    title = "Welcome to ..::Holiday costs calculator::.."
    border = "#" * 50
    frame = f"{border}\n#{' ' * 48}#\n#{title.center(48)}#\n#{' ' * 48}#\n{border}"
    print(frame, "\n")

# Defined functions get_destination_choice
def get_destination_choice():
    while True:
        try:
            select = int(input("Please choose the number enclosed to your destination: "))
            if 1 <= select <= 7:
                return select
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")



# Launching the programme logo
create_frame()
# Collecting input from users
print("Where would you like to go for your city break ??\n")
print("You can choose one of the fallowing destination:\n")
print("1. Madrid\n2. Krakow\n3. Lisbon\n4. Paris\n5. Rome\n6. Berlin\n7. Prague\n")
city_flight = input("Please choose the number enclosed to your destination: ")
num_nights = input("How many nights would you like to stay: ")
rental_day = input("For how many days would you like hire a car: ")
print()
print("Great choose, It will be great holiday")
print(f"The flight price to your destination is {plane_cost(city_flight)}£.")


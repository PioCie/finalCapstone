# Defined function to count hotel cost
def hotel_cost(num_days, rate=48):
    return num_days * rate


# Defined function to choose destination and flight cost
def plane_cost(city_flight):
    if city_flight == 1:
        price = 150
        return price
    elif city_flight == 2:
        price = 180
        return price
    elif city_flight == 3:
        price = 220
        return price
    elif city_flight == 4:
        price = 300
        return price
    elif city_flight == 5:
        price = 275
        return price
    elif city_flight == 6:
        price = 160
        return price
    elif city_flight == 7:
        price = 145
        return price


# Defined function to count car rental cost
def car_rental(num_days):
    return num_days * 22


# Defined function to count total holiday cost
def holiday_cost(hotel_price, flight_price, car_rental_price):
    return hotel_price + flight_price + car_rental_price


# Defined function to create welcome and wishful frame
def create_frame(title):
    border = "#" * 50
    frame = f"{border}\n#{' ' * 48}#\n#{title.center(48)}#\n#{' ' * 48}#\n{border}"
    print(frame, "\n")


# Defined function to get user input about destination
def get_destination_choice():
    while True:
        print("Where would you like to go for your city break ??\n")
        print("You can choose one of the fallowing destination:\n")
        print("1. Madrid\n2. Krakow\n3. Lisbon\n4. Paris\n5. Rome\n6. Berlin\n7. Prague\n")
        try:
            select = int(input("Please choose your flight destination: "))
            if 1 <= select <= 7:
                return select
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Defined function to get user input about duration of stay and hire days
def get_duration_of_stay(question):
    try:
        select = int(input(f"{question}: "))
        return select
    except ValueError:
        print("Invalid input. Please enter a number.")


# Launching the programme start logo
create_frame("Welcome to ..::Holiday costs calculator::..")
# Selecting destination and cost by user
destination = get_destination_choice()
# Display flight cost for user
flight_cost = plane_cost(destination)
print(f"Great choice, the flight cost for your destination is {flight_cost:.2f}£\n")
# Selecting duration of stay by user
length_of_holiday = get_duration_of_stay("How many nights would you like to stay")
hotel = hotel_cost(length_of_holiday)
print(f"Total price for your hotel stay will be {hotel:.2f}£\n")
# Selecting number of day for car rental by user
rental_days = get_duration_of_stay("For how many days would you like hire a car")
car_hire = car_rental(rental_days)
print(f"Total price for your car hire during your stay will be {car_hire:.2f}£\n")
# Counting total price of holiday
total_price = holiday_cost(hotel, flight_cost, car_hire)
print(f"All done. Your holiday package will be cost you {total_price:.2f}£\n")
# Launching the programme end logo
create_frame("..::Have a good holiday::..")

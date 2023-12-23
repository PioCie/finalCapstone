
user_response = input("Hello! How are you? ")

if "good" in user_response.lower():
    print("That's great! I'm glad you're having a good day.")
else:
    print("Oh no, what happened? I hope everything will be fine!")

# Logical error - changing the statement
print("Anyway, no matter how you are. Let's move on to the next question!")

user_age = input("How old are you? ")
print(f"Got it. So, you are {user_age} years old.")

# In this program, the user is greeted and asked about their well-being. Depending on their response, the program
# prints an appropriate message. However, there is a logical error where, regardless of the user's response,
# the program always proceeds to the next question without considering the user's current state.

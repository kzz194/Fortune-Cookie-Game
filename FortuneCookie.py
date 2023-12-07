# Step 1: Import the random module
import random


# Step 2: Define the fortune function
def fortune():
    # Step 3: List of fortunes
    fortunes = [
        "Don't pursue happiness – create it.",
        "All things are difficult before they are easy.",
        "The early bird gets the worm, but the second mouse gets the cheese.",
        "Someone in your life needs a letter from you.",
        "Don't just think. Act!",
        "Your heart will skip a beat.",
        "The fortune you search for is in another cookie.",
        "Help! I'm being held prisoner in a Chinese bakery!"
    ]

    # Step 4: Generate random index
    random_index = random.randint(0, len(fortunes) - 1)

    # Step 5: Print random fortune
    print(fortunes[random_index])


# Step 6: Call the fortune function three times
fortune()
fortune()
fortune()

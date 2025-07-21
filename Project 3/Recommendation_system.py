import pandas as pd

# Updated datasets with deep subcategories

# Category-wise definitions
movies_data = {
    'Sci-Fi': ['Inception', 'Interstellar', 'The Matrix', 'Blade Runner'],
    'Action': ['John Wick', 'Mad Max: Fury Road', 'Die Hard', 'Gladiator'],
    'Romantic': ['Titanic', 'The Notebook', 'Pride and Prejudice'],
    'Thriller': ['The Dark Knight', 'Se7en', 'Gone Girl'],
    'Comedy': ['The Hangover', 'Superbad', 'Step Brothers'],
    'Drama': ['The Godfather', 'Shawshank Redemption', 'Forrest Gump'],
    'Horror': ['The Conjuring', 'Get Out', 'A Quiet Place']
}

books_data = {
    'Sci-Fi': ['Dune', 'Neuromancer', 'Foundation'],
    'History': ['Sapiens', 'Guns, Germs, and Steel'],
    'Comics': ['Batman: Year One', 'Watchmen'],
    'Mystery': ['Gone Girl', 'Sherlock Holmes'],
    'Fantasy': ['Harry Potter', 'Lord of the Rings'],
    'Classic': ['1984', 'To Kill a Mockingbird'],
    'Philosophy': ['The Alchemist', "Sophie's World"]
}

games_data = {
    'Online': ['PUBG', 'Minecraft', 'Valorant', 'GTA Online', 'Fortnite'],
    'Offline': ['Chess', 'Kabaddi', 'Carrom', 'Ludo', 'Badminton']
}

pets_data = {
    'Dog': ['Labrador', 'German Shepherd', 'Golden Retriever', 'Beagle'],
    'Cat': ['Persian Cat', 'Siamese Cat', 'Maine Coon'],
    'Parrot': ['Macaw', 'African Grey'],
    'Rabbit': ['Mini Lop', 'Dutch Rabbit'],
    'Horse': ['Arabian Horse', 'Thoroughbred']
}

fruits_data = {
    'Fruit': ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange', 'Papaya', 'Watermelon']
}

food_data = {
    'Snacks': ['Samosa', 'Chips', 'Poha', 'Pakora', 'Toast', 'Biscuits', 'Pasta'],
    'Dessert': ['Ice Cream', 'Cake', 'Gulab Jamun', 'Jalebi', 'Kheer'],
    'Indian': ['Dal Tadka', 'Butter Chicken', 'Biryani', 'Dosa', 'Chole Bhature'],
    'Italian': ['Pizza', 'Pasta', 'Lasagna', 'Ravioli'],
    'Chinese': ['Noodles', 'Manchurian', 'Spring Roll', 'Dumplings'],
    'Vegan': ['Vegan Burger', 'Salad', 'Tofu Stir Fry', 'Vegan Curry'],
    'Street Food': ['Pani Puri', 'Chaat', 'Kathi Roll', 'Vada Pav']
}

# Mapping categories to their respective data
all_categories = {
    'Movie': movies_data,
    'Book': books_data,
    'Game': games_data,
    'Pet': pets_data,
    'Fruit': fruits_data,
    'Food': food_data
}

def get_user_input(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("\nYour choice: ").strip()
    return options[int(choice)-1] if choice.isdigit() and 1 <= int(choice) <= len(options) else choice.title()

print("Welcome to the Universal Recommender!")

# First input: Main category
category = get_user_input(
    "What would you like recommendations for?", list(all_categories.keys())
)

# Second input: Subcategory
if category in all_categories:
    sub_types = list(all_categories[category].keys())
    sub_category = get_user_input(
        f"Which type of {category.lower()} are you interested in?", sub_types
    )

    items = all_categories[category].get(sub_category)
    if items:
        print(f"\nHere are some {sub_category} {category.lower()}s:")
        for item in items:
            print(f"- {item}")
    else:
        print(f"\nSorry, we don't have detailed examples for {sub_category} under {category}.")
else:
    print("\nSorry, we don't support this category yet.")

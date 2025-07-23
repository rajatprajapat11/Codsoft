# Smart Recommendation System with Two-Level Input and Final Suggestions

# Predefined categories, subcategories, and item suggestions
categories = {
    1: ("Movies", {
        "Horror": ["The Conjuring", "Annabelle", "Insidious", "It", "The Nun", "Sinister", "Hereditary", "The Babadook"],
        "Romantic": ["The Notebook", "Titanic", "La La Land", "Pride & Prejudice", "Me Before You", "A Walk to Remember", "Crazy Rich Asians"],
        "Thriller": ["Shutter Island", "Gone Girl", "Seven", "The Girl with the Dragon Tattoo", "Prisoners", "Memento", "Oldboy"],
        "Comedy": ["The Hangover", "Superbad", "Step Brothers", "21 Jump Street", "Jumanji", "Bridesmaids", "The Mask"],
        "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Avatar", "Blade Runner", "Tenet", "Arrival"],
        "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Pursuit of Happyness", "Parasite", "Whiplash", "Spotlight", "Green Book"],
        "Action": ["Mad Max: Fury Road", "John Wick", "Avengers", "The Dark Knight", "Gladiator", "Inception", "Skyfall"],
        "Animated": ["Toy Story", "Finding Nemo", "Coco", "Frozen", "Zootopia", "Up", "Inside Out"]
    }),
    2: ("Books", {
        "Science": ["A Brief History of Time", "The Selfish Gene", "Cosmos", "Astrophysics for People in a Hurry", "The Gene", "Sapiens", "Homo Deus"],
        "Knowledgeable": ["Sapiens", "Thinking Fast and Slow", "Outliers", "Atomic Habits", "Factfulness", "Deep Work", "Ikigai"],
        "Time-pass": ["Diary of a Wimpy Kid", "Percy Jackson", "Goosebumps", "Geronimo Stilton", "Nancy Drew", "Harry Potter", "Twilight"],
        "Funny": ["Bossypants", "Good Omens", "Me Talk Pretty One Day", "Catch-22", "The Hitchhiker's Guide to the Galaxy"],
        "Healthcare": ["How Not to Die", "The Blue Zones", "Eat to Beat Disease", "Why We Sleep", "The Plant Paradox", "Lifespan"],
        "History": ["Guns, Germs and Steel", "The Silk Roads", "India After Gandhi", "A People's History of the United States"],
        "Biography": ["Steve Jobs", "Becoming", "Long Walk to Freedom", "Elon Musk", "The Diary of Anne Frank", "Einstein"],
        "Spiritual": ["The Power of Now", "The Alchemist", "The Secret", "Bhagavad Gita", "Autobiography of a Yogi"]
    }),
    3: ("Foods", {
        "Indian": ["Butter Chicken", "Paneer Tikka", "Biryani", "Masala Dosa", "Chole Bhature", "Dhokla", "Rogan Josh"],
        "Chinese": ["Noodles", "Manchurian", "Spring Rolls", "Fried Rice", "Dim Sum", "Kung Pao Chicken", "Szechuan Veggies"],
        "Healthy": ["Salad Bowl", "Quinoa", "Smoothies", "Oats", "Grilled Chicken", "Veggie Stir Fry", "Boiled Eggs"],
        "Fast Food": ["Burger", "Pizza", "Tacos", "Fries", "Hot Dog", "Sandwich", "Wraps"],
        "Snacks": ["Samosa", "Chips", "Popcorn", "Puffs", "Nachos", "Pakoras", "Momos"],
        "Sweets": ["Gulab Jamun", "Rasgulla", "Jalebi", "Kheer", "Ladoo", "Barfi", "Halwa"],
        "South Indian": ["Idli", "Dosa", "Vada", "Uttapam", "Sambhar Rice", "Rasam"],
        "Street Food": ["Pani Puri", "Bhel Puri", "Pav Bhaji", "Vada Pav", "Rolls", "Dabeli", "Kathi Roll"]
    }),
    4: ("Games", {
        "Online": ["Valorant", "Fortnite", "PUBG", "Apex Legends", "Call of Duty Mobile", "Clash Royale", "Minecraft", "Among Us"],
        "Offline": ["Chess", "Carrom", "Ludo", "Solitaire", "Candy Crush", "Temple Run", "Subway Surfers", "Cut the Rope"]
    }),
    5: ("Comics", {
        "Marvel": ["Spider-Man", "Iron Man", "Thor", "X-Men", "Avengers", "Black Panther", "Deadpool", "Loki"],
        "DC": ["Batman", "Superman", "Wonder Woman", "The Flash", "Aquaman", "Justice League", "Green Lantern"],
        "Manga": ["Naruto", "One Piece", "Attack on Titan", "Death Note", "Bleach", "Demon Slayer", "Tokyo Ghoul"],
        "Humor": ["Archie Comics", "Garfield", "Calvin & Hobbes", "Dilbert", "The Far Side", "Peanuts"],
        "Fantasy": ["Sandman", "Fables", "Saga", "The Wicked + The Divine", "Hellboy"],
        "Superhero": ["Invincible", "The Boys", "Kick-Ass", "Watchmen", "Young Avengers", "Ms. Marvel"],
        "Adventure": ["Tintin", "Asterix", "The Walking Dead", "Bone", "Black Hammer"],
        "Mythology": ["Ramayan 3392 AD", "Amar Chitra Katha", "Mahabharata", "Greek Gods", "Norse Myth Comics"]
    }),
    6: ("Gadgets", {
        "Mobiles": ["iPhone 14", "Samsung Galaxy S23", "OnePlus 12", "Pixel 8", "Realme GT", "Xiaomi 14", "Nothing Phone 2"],
        "Laptops": ["MacBook Air", "Dell XPS", "HP Spectre", "Asus ROG", "Lenovo ThinkPad", "MSI Stealth", "Acer Nitro"],
        "TVs": ["Samsung QLED", "LG OLED", "Sony Bravia", "OnePlus TV", "Mi TV", "TCL 4K", "Vu Premium"],
        "Smartwatches": ["Apple Watch", "Galaxy Watch", "Fitbit Versa", "Noise ColorFit", "Garmin Venu", "Fossil Gen 6"],
        "Headphones": ["AirPods Pro", "Sony XM5", "Bose QC45", "JBL Live", "Sennheiser HD", "Boat Rockerz", "Realme Buds"],
        "Cameras": ["Canon EOS", "Nikon D3500", "Sony Alpha", "GoPro Hero", "Fujifilm X", "DJI Pocket", "Panasonic Lumix"],
        "Tablets": ["iPad Pro", "Samsung Tab S9", "Lenovo Tab", "Microsoft Surface", "Xiaomi Pad 6"],
        "Gaming Consoles": ["PS5", "Xbox Series X", "Nintendo Switch", "Steam Deck", "PS4 Slim", "Meta Quest"]
    }),
    7: ("Pets", {
        "Dogs": ["German Shepherd", "Rottweiler", "Labrador Retriever", "Bulldog", "Pomeranian", "Golden Retriever", "Beagle", "Doberman"],
        "Cats": ["Persian", "Siamese", "Maine Coon", "Bengal", "Ragdoll", "Himalayan", "British Shorthair", "Sphynx"],
        "Birds": ["Parrot", "Canary", "Budgie", "Lovebird", "Cockatiel", "Macaw", "Finch", "Parakeet"],
        "Rabbits": ["Dutch Rabbit", "Lionhead", "Mini Lop", "Flemish Giant", "Rex Rabbit", "English Spot", "Netherland Dwarf"],
        "Fish": ["Goldfish", "Betta", "Guppy", "Angelfish", "Tetra", "Koi", "Molly", "Oscar"],
        "Turtles": ["Red-Eared Slider", "Box Turtle", "Painted Turtle", "Russian Tortoise", "Mud Turtle", "Map Turtle", "Snapping Turtle"],
        "Hamsters": ["Syrian Hamster", "Dwarf Hamster", "Chinese Hamster", "Campbell’s Dwarf", "Roborovski", "Teddy Bear Hamster", "Albino Hamster"],
        "Exotic Pets": ["Iguana", "Sugar Glider", "Hedgehog", "Ferret", "Chinchilla", "Tarantula", "Axolotl"]
    })
}

def show_options(options_dict):
    for num, (cat, _) in options_dict.items():
        print(f"{num}. {cat}")

def find_category(input_str):
    input_str = input_str.strip().lower()
    for num, (cat, _) in categories.items():
        if input_str == str(num) or input_str == cat.lower():
            return num, cat
    return None, None

def find_type(input_str, subtypes):
    input_str = input_str.strip().lower()
    for i, stype in enumerate(subtypes.keys(), start=1):
        if input_str == str(i) or input_str == stype.lower():
            return stype
    return None

def get_user_input(prompt):
    return input(prompt).strip()

def main():
    print("\nWelcome to the Smart Recommendation System")

    # Step 1: Category Input
    print("\nChoose a category:")
    show_options(categories)
    cat_input = get_user_input("\nEnter category number or name: ")
    cat_num, cat_name = find_category(cat_input)

    if not cat_name:
        print("\nUnknown category. Showing default categories again.")
        return main()

    # Step 2: Type Input
    subtypes = categories[cat_num][1]
    print(f"\nTypes in '{cat_name}':")
    for i, stype in enumerate(subtypes.keys(), start=1):
        print(f"{i}. {stype}")

    type_input = get_user_input("\nEnter type number or name: ")
    chosen_type = find_type(type_input, subtypes)

    if not chosen_type:
        print("\nUnknown type. Showing types again.")
        return main()

    # Step 3: Final Suggestions
    print(f"\nTop {cat_name} Recommendations in '{chosen_type}':")
    suggestions = subtypes[chosen_type]
    for i, item in enumerate(suggestions, start=1):
        print(f"{i}. {item}")

    print("\nThank you for using the recommendation system.")

if __name__ == "__main__":
    main()

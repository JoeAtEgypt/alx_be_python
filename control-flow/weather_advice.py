weaather = (
    input("What is the weather like? (sunny, rainy, snowy, windy): ").strip().lower()
)

if weaather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weaather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weaather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

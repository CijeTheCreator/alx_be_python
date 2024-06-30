
answerSunny = "Wear a t-shirt and sunglasses."
answerRainy = "Don't forget your umbrella and a raincoat."
answerCold = "Make sure to wear a warm coat and scarf."
answerUnknown = "Sorry, I don't have recommendations for this weather."

weather = input("What's the weather like today? (sunny/rainy/cold): ")
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print('Don\'t forget your umbrella and a raincoat.')
elif weather == "cold":
    print('Make sure to wear a warm coat and scarf.')
else:
    print('Sorry, I don\'t have recommendations for this weather.')
question1 = 'What\'s the weather like today? (sunny/rainy/cold):'
answerSunny = "Wear a t-shirt and sunglasses."
answerRainy = "Don't forget your umbrella and a raincoat."
answerCold = "Make sure to wear a warm coat and scarf."
answerUnknown = "Sorry, I don't have recommendations for this weather."

weather = input("What's the weather like today? (sunny/rainy/cold): ")
if weather == "sunny":
    print(answerSunny)
elif weather == "rainy":
    print(answerRainy)
elif weather == "cold":
    print(answerCold)
else:
    print(answerUnknown)
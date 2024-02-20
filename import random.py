import random

symbols = ["🍒", "🍇", "🍉", "7"]


results = symbols

results_srt = " | ".join(random.choices(symbols, k=3))

print(results_srt)

if all(symbol == '7' for symbol in results):
    print("¡Premio mayor! 💰")
else:
    print("Intente nuevamente")

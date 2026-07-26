
capitals = {
            "USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",
            "Bangladesh": "Dhaka"
}

score = 0

for country, capital in capitals.items():
    c = input(f"What's the capital of {country}: ").lower()
    if c == capital:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print(f"Your score!: {score}/{len(capitals)}")

users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])
# 2. Get Erik's hometown
print(users["Erik"]["home_town"])
# 3. Get the list of Erik's lottery numbers
erik_lottery = users["Erik"]["lottery_numbers"]
print(erik_lottery)
# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])
# 5. Get the smallest of Erik's lottery numbers
erik_lottery = users["Erik"]["lottery_numbers"]
for min_number in erik_lottery:
    min_numebr = erik_lottery[0]
    for a in erik_lottery:
        if a < min_numebr:
            min_numebr = a
print(min_numebr)


# 6. Return an list of Avril's lottery numbers that are even
avril_lottery_number = users["Avril"]["lottery_numbers"]
avril_even_lottery_number = []
for i in avril_lottery_number:
    if i % 2 == 0:
        avril_even_lottery_number.append(i)
print(avril_even_lottery_number)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
erik_lottery.append(7)
print(erik_lottery)
# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])
# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name":"fluffy","species":"dog"})
print(users["Erik"]["pets"])
# 10. Add another person to the users dictionary
users["Ying"] = {
    "twitter": "none",
    "lottery_numbers": [1,2,7,11,12,29],
    "home_town": "Tianjin",
    "pets": 
    {
      "name": "huahua",
      "species": "cat"
    }}
print(users)
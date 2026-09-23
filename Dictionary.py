#Simple dictionary example

country_capitals = {
    "Germany": "Berlin", 
    "Canada": "Ottawa",
    "France": "Paris"
}

print ("country_capitals" , country_capitals)
print (country_capitals["Germany"])

country_capitals["England"] = "London"
print (country_capitals["England"])

print("Germany" in country_capitals)  # Output: True

print("Spain" not in country_capitals)


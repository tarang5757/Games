#nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"

}
#Nesing a list in a dictionary

travel_log = {
    "France": ["paris", "Lille", "dijon"],
    "Germany": ["Berlin", "hamburg", "Stuttgart"]
}

#Nest Dictionary in a dictionary
travel_log = {
    "France": {"Cities_visited": ["Paris", "Litlle", "Dijon"], "total_visit":12},
    "Germany": {"Cities_visited": ["Berlin", "hamburg", "Stuttgart"], "total_visits":12}
}
["Paris", "Litlle", "Dijon"]

"""
[{
#Key:[list],
#Key2:{Dict},
}, 
{
    key:Value,
    key2:Value,
}]
"""

travel_log = [
    {
        "country": "France",
        "cities_visited":["Paris", "lillie", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "germany",
        "cities_visited":["Berlin", "hamburg", "stuttgart"],
        "total_visits":5

    
    }
]

#Write a program that adds to a travel_log. You can see travel_log which is a List that contains 2 dictionaries.
def add_new_country(country, visits, lis):
    new_country = {}
    new_country['country'] = country
    new_country["cities_visited"] = lis
    new_country['total_visits'] = visits
    travel_log.append(new_country)

add_new_country("russia", 2, ["Moscow", "Saint petersburg"])

print(travel_log)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order['main'][2])
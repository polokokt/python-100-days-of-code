capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in dictionary

travel_log = {
    "France": ["Paris", "Dijon", "Lille"],
    "Germany": ["Berlin", "Hamburg"],
}

print(travel_log["France"][2])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log2 = {
    "France": {"cities_visited": ["Paris", "Dijon", "Lille"], "total_visit": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_visit": 8},
}

print(travel_log2["France"]["cities_visited"][1])

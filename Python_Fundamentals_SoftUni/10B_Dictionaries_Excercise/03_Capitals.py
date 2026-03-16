countries = input().split(", ")
capitals = input().split(", ")

# countries_and_capitals = dict(zip(countries, capitals))
countries_and_capitals = {country: capital for country, capital in zip(countries, capitals)}
for key, value in countries_and_capitals.items():
    print(f"{key} -> {value}")
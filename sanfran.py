
def travel_sites(cities, str="I have visited the city of"):
  for city in cities:
    print(f'{str}{city}')


travel_sites(["San Francisco", "Denver", "Nashville"])
travel_sites(["Knoxville", "Paris", "New York"], "I have not visited this loser place: ")


# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food (q to quit): ")
    if food.lower() == "q":
          break
    else:
        price = float(input(f"Enter the price of {food} : "))
        foods.append(food)
        prices.append(price)

for food in foods:
    print(food,end=" ")
for price in prices:
    total += price

print(f"Total price is {total}")

# Movie ticket program

movies = []
prices = []
no_of_tickets = 0
total_price = 0

while True:
    movie = input("Enter the movie name (q to quit): ")
    if movie.lower() == "q":
        break
    else:
        no_of_tickets = int(input(f"Enter the number of tickets (q to quit): "))
        price = float(input(f"Enter the price of {movie} : "))
        movies.append(movie)
        prices.append(price)

for movie in movies:
    print(movie,end=" ")
for price in prices:
    total_price = no_of_tickets * price

print(f"Your total price is {total_price} : Rs")

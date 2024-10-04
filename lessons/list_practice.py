# Creating an empty list

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = [1.0, 2.0, 2.5, 3.0]  # literal

my_numbers.append(1.5)

print(my_numbers)

# String Analogy

# my_name: str = ''
# my_name: str = str()

# Multiple types of parameters
# game_points: list[int | float] = [102, 86, 94]
# using | to split them up

game_points: list[int] = [102, 86, 94]
print(game_points[2])  # [index], inside the brackets is index
game_points[1] = 72  # changing 86 to 72
print(game_points[1])
print(len(game_points))  # print the length of the list

game_points.pop(1)
print(game_points[1])

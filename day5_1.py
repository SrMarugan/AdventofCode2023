# Day 5 Part 1


def listing_numbers(list_numbers: list[str], diccionario: dict[int]) -> dict[int]:
    for index in range(0, int(list_numbers[2])):
        diccionario[int(list_numbers[1])+index] = int(list_numbers[0])+index
    return diccionario


def is_in_between(seed: str, list_numbers: list[str]) -> str:
    if int(seed) < (int(list_numbers[1])+int(list_numbers[2])) and int(seed) > int(list_numbers[1]):
        return str(int(list_numbers[1])+int(list_numbers[2])-int(seed)+int(list_numbers[0]))
    else:
        return seed


# diccionario = listing_numbers(list_numbers=[50, 98, 2], diccionario=diccionario)
# diccionario = listing_numbers(list_numbers=[52, 50, 48], diccionario=diccionario)

# print(diccionario)
# seed_list = [79, 14, 55, 13]
# seed_list_2 = []
# for seed in seed_list:
#     try:
#         number = diccionario[seed]
#     except KeyError as _error:
#         number = seed

#     print(number)
#     seed_list_2.append(number)

# print(seed_list, seed_list_2)

file = open(file="AdventCode\Day5\input.txt")

linea = file.readline()
linea = linea.split(" ")
linea.pop(0)
linea.append(linea.pop().split("\n")[0])
seed_list = linea
print(seed_list)

file = open(file="AdventCode\Day5\seed-to-soil.txt")
seeding = file.readlines()
seed_to_soil = []
for to_soil in seeding:
    seed_to_soil = to_soil.split(" ")
    seed_to_soil.append(seed_to_soil.pop().split("\n")[0])
    print(seed_to_soil)
    for index, seed in enumerate(seed_list):
        seed_list[index] = is_in_between(seed=seed, list_numbers=seed_to_soil)

print(seed_list)

file = open(file="AdventCode\Day5\soil-to-fertilizer.txt")
seeding = file.readlines()
soil_to_fertilizer = []
for to_soil in seeding:
    soil_to_fertilizer = to_soil.split(" ")
    soil_to_fertilizer.append(soil_to_fertilizer.pop().split("\n")[0])
    for index, seed in enumerate(seed_list):
        seed_list[index] = is_in_between(seed=seed, list_numbers=soil_to_fertilizer)

print(seed_list)

file = open(file="AdventCode\Day5\\fertilizer-to-water.txt")
seeding = file.readlines()
fertilizer_to_water = []
for to_soil in seeding:
    fertilizer_to_water = to_soil.split(" ")
    fertilizer_to_water.append(fertilizer_to_water.pop().split("\n")[0])
    for index, seed in enumerate(seed_list):
        seed_list[index] = is_in_between(seed=seed, list_numbers=fertilizer_to_water)

print(seed_list)

file = open(file="AdventCode\Day5\water-to-light.txt")
seeding = file.readlines()
fertilizer_to_water = []
for to_soil in seeding:
    fertilizer_to_water = to_soil.split(" ")
    fertilizer_to_water.append(fertilizer_to_water.pop().split("\n")[0])
    for index, seed in enumerate(seed_list):
        seed_list[index] = is_in_between(seed=seed, list_numbers=fertilizer_to_water)

print(seed_list)

file = open(file="AdventCode\Day5\light-to-temperature.txt")
seeding = file.readlines()
fertilizer_to_water = []
for to_soil in seeding:
    fertilizer_to_water = to_soil.split(" ")
    fertilizer_to_water.append(fertilizer_to_water.pop().split("\n")[0])
    for index, seed in enumerate(seed_list):
        seed_list[index] = is_in_between(seed=seed, list_numbers=fertilizer_to_water)

print(seed_list)

file = open(file="AdventCode\Day5\\temperature-to-humidity.txt")
seeding = file.readlines()
fertilizer_to_water = []
for to_soil in seeding:
    fertilizer_to_water = to_soil.split(" ")
    fertilizer_to_water.append(fertilizer_to_water.pop().split("\n")[0])
    for index, seed in enumerate(seed_list):
        seed_list[index] = is_in_between(seed=seed, list_numbers=fertilizer_to_water)

print(seed_list)

file = open(file="AdventCode\Day5\humidity-to-location.txt")
seeding = file.readlines()
fertilizer_to_water = []
for to_soil in seeding:
    fertilizer_to_water = to_soil.split(" ")
    fertilizer_to_water.append(fertilizer_to_water.pop().split("\n")[0])
    for index, seed in enumerate(seed_list):
        seed_list[index] = is_in_between(seed=seed, list_numbers=fertilizer_to_water)

print(seed_list)
seed_list_num = []
for seed in seed_list:
    seed_list_num.append(int(seed))
print(min(seed_list_num))

foreign_food = {}
allergens = {}
found_allergens = []

danger_list = []

input_text = open('input/day21.txt').read().split('\n')

for line in input_text:
    foods, mark = line.split('(')
    foods = foods.split()
    mark = mark[:-1].replace(',','').split()[1:]


    for m in mark:
        if m not in allergens:
            allergens[m] = set(foods)
        else:
            allergens[m] = allergens[m].intersection(set(foods))

    for f in foods:
        if f not in foreign_food:
            foreign_food[f] = 1
        else:
            foreign_food[f] += 1

number_of_allergens = len(allergens)
while len(found_allergens) < number_of_allergens:
    for key, val in allergens.items():
        if len(val) == 1:
            food = list(val)[0]

            allergens[key] = set()
            found_allergens.append(food)
            danger_list.append([key, food])
        else:
            allergens[key] = allergens[key] - set(found_allergens)



res1 = 0
for key, val in foreign_food.items():
    if key not in found_allergens:
        res1 += val
print(res1)



res2 = ','.join([df for _, df in sorted(danger_list)])
print(res2)
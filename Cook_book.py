def reading_file(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf8') as file_open:
        for line in file_open:
            dish = line.strip()
            cook_book[dish] = [] # по первой строке заполняем ключи
            number = int(file_open.readline().strip()) # количество срок с ингридиентами считаем по 2 строке
            for ingredients in range(number):
                ingredients = file_open.readline().strip().split('|')
                dict = {'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]}
                cook_book[dish].append(dict)
            file_open.readline() # смещаемся по пустой строке
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = reading_file('recipes.txt')
    shop_list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list_by_dishes:
                    shop_list_by_dishes[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
                else:
                    shop_list_by_dishes[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
    return shop_list_by_dishes


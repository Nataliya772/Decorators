import datetime
from Cook_book import reading_file

# Задание 1
def write_logs(old_function):
    def new_function(*args, **kwars):
        with open('log_file.log', 'a', encoding='utf8') as log_file:
            result = old_function(*args, **kwars)
            log_file.write(f'{datetime.datetime.utcnow()}, {old_function.__name__},\n'
                           f'аргументы вызванной функции: {args}, {kwars},\n'
                           f'результат вызванной функции: {result}\n')
        return result
    return new_function

# Задание 2
def my_logger(file_name):
    def write_logs(old_function):
        def new_function(*args, **kwars):
            with open(file_name, 'a', encoding='utf8') as log_file:
                result = old_function(*args, **kwars)
                log_file.write(f'{datetime.datetime.utcnow()}, {old_function.__name__},\n'
                               f'аргументы вызванной функции: {args}, {kwars},\n'
                               f'результат вызванной функции: {result}\n')
            return result
        return new_function
    return write_logs

# Задание 3
def logger_for_shop_list_by_dishes(file_name):
    def write_logs(old_function):
        def new_function(dishes, person_count):
            with open(file_name, 'a', encoding='utf8') as log_file:
                result = old_function(dishes, person_count)
                log_file.write(f'{datetime.datetime.utcnow()}, {old_function.__name__},\n'
                               f'аргументы вызванной функции: {dishes}, {person_count},\n'
                               f'результат вызванной функции: {result}\n')
            return result
        return new_function
    return write_logs

@logger_for_shop_list_by_dishes('mylog.txt')
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = reading_file('recipes.txt')
    shop_list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list_by_dishes:
                    shop_list_by_dishes[ingredient['ingredient_name']]['quantity'] += int(
                        ingredient['quantity']) * person_count
                else:
                    shop_list_by_dishes[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                          'quantity': int(
                                                                              ingredient['quantity']) * person_count}
    return shop_list_by_dishes

if __name__ == '__main__':
    get_shop_list_by_dishes(['Утка по-пекински'], 7)

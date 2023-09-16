import os

def directory_count(directory):
    total_size = 0
    total_count = 0

    for root, dirs, files, in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
            total_count += 1
    return total_size, total_count

directory_path = 'directory'

total_size, total_count = directory_count(directory_path)
print(f"Загальний розмір файлів: {total_size} байт")
print(f"Загальний кількість файлів {total_count}")










# -------------------------->homework 44 sice 2
# import os
# import shutil
#
# def extension(src_directory, dest_directory, file_extansion):
#     if not os.path.exists(src_directory):
#         raise FileNotFoundError(f"Деректорії {src_directory} не існує")
#
#     if not os.path.exists(dest_directory):
#         os.makedirs(dest_directory)
#
#     for filname in os.listdir(src_directory):
#         src_filepath = os.path.join(src_directory, filname)
#
#         if os.path.isfile(src_filepath) and filname.endswith(file_extansion):
#             dest_filepath = os.path.join(dest_directory, filname)
#             shutil.copy2(src_filepath, dest_filepath)
#             print(f"Скопійоано{filname} з {src_directory} до{dest_directory}")
#
# try:
#     extension('directory', 'files2', '.txt')
# except FileNotFoundError as e:
#     print(e)

















# ------------------------------------------->homework 44 sice 1
# import os
# import time
#
# def file_info(derectory):
#     if not os.path.exists(derectory):
#         raise FileNotFoundError(f"Кталогу {derectory} не існує")
#     print(f"{'Назва файлу':<30}{'Розмір(байти)':<20}{'Дата ствворення':<30}{'Дата зміни':<30}")
#     print("=" * 100)
#
#     for filname in os.listdir(derectory):
#         filpath = os.path.join(derectory, filname)
#
#         if os.path.isfile(filpath):
#             file_size = os.path.getsize(filpath)
#             create_time = time.ctime(os.path.getctime(filpath))
#             modigy_time = time.ctime(os.path.getmtime(filpath))
#             print(f"{filname:<30}{file_size:<20}{create_time:<30}{modigy_time:<30}")
#
# try:
#     file_info('files')
# except FileNotFoundError as e:
#     print(e)








# def fact_v2(n):
#     try:
#         if n < 0:
#             raise ValueError("Факторіал можна обчислити леше для цілих чисео")
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#     except ValueError as e:
#         return str(e)
# def main():
#     try:
#         num = int(input("Введіть число"))
#         result = fact_v2(num)
#         if result.isdigit():
#             print(f"{num} = {result}")
#         else:
#             print(f"Помилка {result}")
#     except ValueError:
#         print("Число не є цілим")
# if __name__ == "__main__":
#     main()






# def fact_v1(n):
#     if n < 0:
#         return None
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# def main():
#     try:
#         num = int(input("Введіть число"))
#         result = fact_v1(num)
#         if result is not None:
#             print(f"{num} = {result}")
#         else:
#             print("Факторіл можна обчислити лише для цілих чисел")
#     except ValueError:
#         print("Число не є цілим числои")
#
# if __name__ == "__main__":
#     main()






# ----------------home work 38 sicee 3
# def main():
#     num_list = []
#
#     while True:
#         print("\nМеню:")
#         print("1. Відображення списку")
#         print("2. Отримати максимальне значення")
#         print("3. Отримати мінімальне значення")
#         print("4. Відобразити значення за індексом")
#         print("5. Додати елемент до списку")
#         print("6. Видалити елемент за індексом")
#         print("7. Вихід")
#
#         choice = input("Виберіть опцію: ")
#
#         if choice == '1':
#             display_list(num_list)
#         elif choice == '2':
#             get_max(num_list)
#         elif choice == '3':
#             get_min(num_list)
#         elif choice == '4':
#             display_element(num_list)
#         elif choice == '5':
#             add_element(num_list)
#         elif choice == '6':
#             delete_element(num_list)
#         elif choice == '7':
#             break
#         else:
#             print("Неправильний вибір опції. Спробуйте ще раз.")
#
#
# def display_list(num_list):
#     if not num_list:
#         print("Список порожній")
#     else:
#         print("Список", num_list)
#
# def get_max(num_list):
#     if not num_list:
#         print("Список порожній")
#     else:
#         max_val = max(num_list)
#         print("Максимльне значення у списку", max_val)
#
# def get_min(num_list):
#     if not num_list:
#         print("Список порожній")
#     else:
#         min_val = min(num_list)
#         print("Мінімальне число у списку", num_list)
#
# def display_element(num_list):
#     if not num_list:
#         print("Список порожній")
#     else:
#         try:
#             index = int(input("Ведіть індекс елемента:"))
#             element = num_list[index]
#             print(f"Значення за індексом {index}:{element}")
#         except IndexError:
#             print("Елемента з таким індексом немає")
#
# def delete_element(num_list):
#     if not num_list:
#         print("Список порожній")
#     else:
#         try:
#             index = int(input("Вкажіть індекс елемента, який бажаєте видалити"))
#             del num_list[index]
#             print("Елемент видалино успішно")
#         except (ValueError, IndexError):
#             print("Неправельний індекс елемента")
#
# def add_element(num_list):
#     try:
#         element = float(input("Введіть новий елемент:"))
#         num_list.append(element)
#         print("Елменет успішно додано")
#     except ValueError:
#         print("Помилка Ведыть числове значення")
#
# if __name__ == "__main__":
#     main()





#----------------homework 38 sice 2
# def fact_v2(n):
#     try:
#         if n < 0:
#             raise ValueError("Error: Factorial can only be calculated for non-negative integers-1")
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#     except ValueError as e:
#         return str(e)
#
# try:
#     num = int(input("Give number"))
#     result = fact_v2(num)
#     if result.isdigit():
#         print(f"{num} = {result}")
#     else:
#         print(f"Erorr:{result}")
# except ValueError:
#     print("Error: Factorial can only be calculated for non-negative integers")






# def fact_v1(n):
#     if n < 0:
#         return None
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# try:
#     num = int(input("Give number"))
#     result = fact_v1(num)
#     if  result is not None:
#         print(f"{num} = {result}")
#     else:
#         print("Error: Factorial can only be calculated for non-negative integers")
# except ValueError:
#     print("Your text not number")





#homework 38 sice 1
# def fact(n):
#     if n < 0:
#         raise ValueError("Give positive number")
#     if n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#
# try:
#     num = int(input("Give number only positive:"))
#     result = fact(num)
#     print(f"{num} = {result}")
# except ValueError as e:
#     print(f"Error in:{e}")










#------------------------home work 37 sice 4
# print("-" * 7 + "Part 1" + "-" * 7)
# def func(lst):
#     summa = sum(lst)
#     return summa
# try:
#     lst = [1, 2, 3.4, "gfgf", 5]
#     result = func(lst)
#     print(f"Summa your list: {result}")
# except ValueError as e:
#     print(f"Error in {e}")
# except Exception as e:
#     print(f"Another mistake:{e}")
# print("-" * 7 + "Part 2" + "-" * 7)
# def function(lst):
#     try:
#         summa = sum(lst)
#         return summa
#     except Exception as e:
#         raise f"Error inn: {e}"
# lst1 = [1, 2, 3.4, "gfgf", 5]
# try:
#     result1 = function(lst1)
#     print(f"Your sum numbers = {result1}")
# except Exception as e:
#     print(f"Error in:{e}")




#home work 37 sice 3
# def added_numbers():
#     num = []
#     while True:
#         give = input("Enter positive number or Exit for termination ")
#         if give.lower() == 'exit':
#             break
#         try:
#             number = float(give)
#             if number <= 0:
#                 raise ValueError("Negative number or zero entered.")
#             num.append(number)
#         except ValueError as e:
#             print(f"Error in {e}")
#     return num
# def get_numbers(num):
#     if not num:
#         return "Your list empty"
#     summa = sum(num)
#     return f"Sum your numbers: {summa}"
# try:
#     give_num = added_numbers()
#     result = get_numbers(give_num)
#     print(result)
# except KeyboardInterrupt:
#     print("User has out")
# except Exception as e:
#     print(f"Error for {e}")










#homeewirk 37 sice 2
# print("-" * 7 + "Part 1" + "-" * 7)
# def func(name, age):
#     result = f"Hello, {name} your age {age}"
#     return result
#
# try:
#     name = input("Give toyr name$1: ")
#     age = int(input("Give your age$1: "))
#
#     if 0 <= age <= 130:
#         result = func(name, age)
#         print(result)
#     else:
#         print("Error: Age must be in the range from 0 in 130")
# except ValueError as e:
#     print("Error: Your age is incorrect")
# print("-" * 7 + "Part 2" + "-" * 7)
# def function(name, age):
#     try:
#         age = int(age)
#         if 0 <= age <= 130:
#             messeng = f"Hello, {name} your age = {age}"
#             return messeng
#         else:
#             print("Error: Age must be in the range from 0 in 130")
#     except ValueError as s:
#         print("Error: Your age is incorrect")
#         print(s)
#
# name1 = input("Give your name: ")
# age1 = input("Give your age: ")
# result1 = function(name1, age1)
# print(result1)









#--------------homework 37 sicee 1
# try:
#     name = input("Введіть ваше ім'я: ")
#     age = int(input("Введіть ваш вік: "))
#
#
#     if 0 <= age <= 130:
#         # Виводимо привітання
#         print(f"Привіт, {name}! Твій вік — {age}")
#     else:
#         print("Помилка: Вік повинен бути в діапазоні від 0 до 130.")
# except ValueError:
#     print("Помилка: Введений вік є некоректним.")







#-------------home work 36 sice 4
# import time
# def log(func):
#     def wrapper(*args, **kwargs):
#         name = func.__name__
#         arguments = ' '.join([repr(arg) for arg in args] + [f'{k}={v!r}' for k,v in kwargs.items()])
#         print(f'Executed {name}({arguments})')
#         return func(*args, **kwargs)
#     return wrapper
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         ex_time = end - start
#         print(f"Function:{func.__name__} executed by {ex_time} second")
#         return result
#     return wrapper
#
# @timer
# @log
# def nums(a, b):
#     result = [x for x in range(a, b + 1) if x % 2 == 0]
#     return result
# result = nums(1, 10)
# print(result)







#-----------homework 36 sice 3
#import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         ex_time = end - start
#         print(f"Function:{func.__name__} executed by {ex_time:.5f} second")
#         return result
#     return wrapper
# @timer
# def f1():
#     res = ''
#     for i in range(10**6):
#         res += ''
# @timer
# def f2():
#     res = ' ' * 10**6
#
# f1()
# f2()


#----------homework 36 sice 2
# def usd_convert(func):
#     def wrapper(count, price):
#         result_uah = func(count, price)
#         exchange_rate = 37.8
#         result_usd = result_uah / exchange_rate
#
#         return f"{result_uah} UAH\n{result_usd:.2f} USD"
#     return wrapper
#
# def exchanges_convertor(exchanges_rate):
#     def decorator(func):
#         def wrapper(count, price):
#             result_uah = func(count, price)
#             result_usd = result_uah / exchanges_rate
#             return f"{result_uah} UAH\n{result_usd:.2f} USD"
#         return wrapper
#     return decorator
# @usd_convert
# def check(count, price):
#     print("check=|count|price|")
#     summa = count * price
#     return summa
#
# @exchanges_convertor(40)
# def custom_exchange(count, price):
#     print("check=|count|price|")
#     summa = count * price
#     return summa
#
# #Фіксований курс
# result1 = check(2, 10)
# print(result1)
# #Змінений курс
# result2 = custom_exchange(2, 10)
# print(result2)



#-----homework 36 sice 1
# def validate_divide(func):
#     def wrapper(a, b):
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             print("Error: Both arguments must be numbers.")
#             return None
#         elif b == 0:
#             print("Error: Division by zero is not allowed.")
#             return None
#         else:
#             print("Division is performed")
#             return func(a, b)
#     return wrapper
#
# @validate_divide
# def divide(a: float, b: float) -> float:
#     return a / b
#
# result = divide(10, 2)
#
# result1 = divide(10, 0)
#
# result2 = divide("abc", 2)
#
# print(result)
# print(result1)
# print(result2)











#--------------home work 34 sice 4
# from functools import partial
# def log(date, message, important):
#     if important:
#         prefix = "Prefix:"
#     else:
#         prefix = ""
#     messege = f"[{date}] {prefix}{message}"
#     print(messege)
#
# # log("1", "Hello man", False)
# # log("2""Hello Ivan", True)
#
# # log1 = partial(log, important=True)
# # log1("25-8", "Hello men")
# # log1("25-8", "Hello Ivan")
#
#
# def log1(date):
#     def log_message(message, important):
#         if important:
#             prefix = "IMPORTANT: "
#         else:
#             prefix = ""
#
#         formatted_message = f"[{date}] {prefix}{message}"
#         print(formatted_message)
#
#     return log_message
# print()
#
# log_with_fixed_date = log1("2023-08-25")
#
#
# log_with_fixed_date("Це повідомлення не є важливим.", False)
# log_with_fixed_date("Це важливе повідомлення!", True)




#homework 35 sice 3
# from datetime import datetime
#
# films = [
#     {'title': 'The Grand Budapest Hotel', 'year': 2014, 'genre': 'comedy'},
#     {'title': 'Inception', 'year': 2010, 'genre': 'thriller'},
#     {'title': 'The Hangover', 'year': 2009, 'genre': 'comedy'},
#     {'title': 'La La Land', 'year': 2016, 'genre': 'musical'},
#     {'title': 'Terminator-2', 'year': None, 'genre': 'action'},
#     {'title': 'The Social Network', 'year': 2010, 'genre': 'drama'},
#     {'title': 'La La Land', 'year': 2016, 'genre': 'musical'},
#     {'title': 'Terminator', 'year': None, 'genre': 'action'},
#     {'title': 'Interstellar', 'year': 2014, 'genre': 'science fiction'},
#     {'title': 'Django Unchained', 'year': 2012, 'genre': 'western'},
#     {'title': 'The Dark Knight Rises', 'year': 2012, 'genre': 'action'},
#     {'title': 'The Wolf of Wall Street', 'year': 2013, 'genre': 'comedy'},
#     {'title': 'Mad Max: Fury Road', 'year': 2015, 'genre': 'action'},
# ]
#
# year = datetime.now().year
# years = list(map(lambda x: year - x ['year'] if x['year'] is not None else None, films))
# print("How many years have passed since the release of the film")
# print(years)
#
# with_know_yer = list(filter(lambda x: x['year'] is not None, films))
# print("Movies with a known release year")
# print(with_know_yer)
#
# comedy_films = list(filter(lambda x: x['genre'] == 'comedy', films))
# print("Movies comedy")
# print(comedy_films)





#homework 35 sice 2
# from functools import reduce
# #1
# numbers = list(range(1,31))
# #2
# cubed_numbers = list(map(lambda x: x**3, numbers))
# print(" ".join(map(str, cubed_numbers)))
# #3
# filtered = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))
# print(" ".join(map(str, filtered)))
# #4
# product = reduce(lambda x, y: x * y, numbers)
# print(product)
# #5
# number_degits = list(map(lambda x: len(str(x)), numbers))
# print(" ".join(map(str, number_degits)))






#--------------homework 35 sice 1
# def sum_lists(list1, list2: list) -> [int]:
#     """
#     Приймає два списки цілих чисел та повертає список, в якому кожен елемент
#     є сумою відповідних елементів вхідних списків. Якщо списки різної довжини,
#     відсутні елементи рахуються як нуль.
#
#     :param list1: Перший список цілих чисел.
#     :param list2: Другий список цілих чисел.
#     :return: Список сум відповідних елементів вхідних списків.
#     """
#     max_len = max(len(list1), len(list2))
#     result = []
#
#     for i in range(max_len):
#         element1 = list1[i] if i < len(list1) else 0
#         element2 = list2[i] if i < len(list2) else 0
#         result.append(element1 + element2)
#
#     return result
#
#
# list1 = [1, 3, 4, 2]
# list2 = [8, 3, 5, 9, 5, 4]
#
# result = sum_lists(list1, list2)
# print(result)


#-----------homework 34 sice 4
# def gen(number):
#     if number <= 1:
#         return False
#     if number <= 2:
#         return True
#     if number % 2 == 0:
#         return False
#     for i in range(3, int(number**0.5)+ 1, 2):
#             if number % i == 0:
#                 return False
#     return True
# def generator():
#     number = 2
#     while True:
#         if gen(number):
#             yield number
#         number += 1
# prime_gen = generator()
# #next
# print("First 10 prime numbers (using next)")
# for _ in range(10):
#     print(next(prime_gen), end=' ')
# print("\n")
# #for
# print("First 10 prime numbers (using for)")
# count = 0
# for i in prime_gen:
#     print(i, end=' ')
#     count += 1
#     if count == 10:
#         break







#----------homework 34 sice 3
# def gen(n):
#     curet = 1
#     while curet < n:
#         if curet % 3 == 0 or curet % 5 == 0:
#             yield curet
#         curet += 1
# n = 20
# for num in gen(n):
#     print(num, end=' ')


#-------------homework 34 sice 2
# def iter(start, end,step):
#     curet = start
#     while curet <= end:
#         if curet % 2 == 0:
#             yield curet
#         curet += step
# start, end, step = 2, 52, 1
# for num in iter(start, end, step):
#     print(num, end=' ')
# print()
# start1, end1, step1 = 2, 52, 2
# result = iter(start1, end1, step1)
# for num in result:
#     print(num, end=' ')
# print()
# start2, end2, step2 = 1, 53, 5
# for num in iter(start2, end2, step2):
#     print(num, end=' ')



#-------------homework 34 sice 1
# def gen(a, b):
#     for num in range(a, b + 1):
#         if num % 2 != 0:
#             yield num
# a = 10
# b = 20
# print(f"Odd numbers in the range {a} to {b}:")
# for odd in gen(a, b):
#     print(odd)





#homwork 33 sice 4
# def my_sort(films, key, reverse=False):
#     sorted_films = sorted(films, key=lambda x: x[key], reverse=reverse)
#     return sorted_films
# def sott(films):
#     for film in films:
#         print(f"Title:{film['title']}, Year: {film['year']}, Genre:{film['genre']}")
# films = [
#     {'title': 'The Grand Budapest Hotel', 'year': 2014, 'genre': 'comedy'},
#     {'title': 'Inception', 'year': 2010, 'genre': 'thriller'},
#     {'title': 'The Hangover', 'year': 2009, 'genre': 'comedy'},
#     {'title': 'La La Land', 'year': 2016, 'genre': 'musical'},
#     {'title': 'The Social Network', 'year': 2010, 'genre': 'drama'},
#     {'title': 'Interstellar', 'year': 2014, 'genre': 'science fiction'},
#     {'title': 'Django Unchained', 'year': 2012, 'genre': 'western'},
#     {'title': 'The Dark Knight Rises', 'year': 2012, 'genre': 'action'},
#     {'title': 'The Wolf of Wall Street', 'year': 2013, 'genre': 'comedy'},
#     {'title': 'Mad Max: Fury Road', 'year': 2015, 'genre': 'action'},
# ]
# sort_films = my_sort(films, 'year', reverse=True)
# sott(sort_films)




#------------homework 33 sice 3
# programmers = ['James Gosling', 'Bjarne Stroustrup', 'Donald Knuth', 'Larry Wall', 'Dennis Ritchie']
# programmers.sort(key=lambda x: len(x))
# print(f"Length list:{programmers}")
# programmers.sort(key=lambda x: x.split()[-1])
# print(f"Sorted for surname:{programmers}")


#homework 33 sice 2
# func = lambda x, y: x + y if x > 0 and y > 0 else (x - y if x < 0 and y < 0 else 0)
# a = 5
# b = 7
# print(func(a, b))
# a = -5
# b = -7
# print(func(a, b))
# a = 4
# b = -3
# print(func(a, b))






#homework 33 sice 1
# def even(number):
#     return number % 2 == 0
# def add(number):
#     return number % 2 != 0
# def value(values, func):
#     return func(values)
# while True:
#     lst = int(input("Give numbers fow checks:"))
#     choice = input("You want to check whether a number is even or odd (p = even /n = not even/e = exit)")
#
#     if choice == "p":
#         result = value(lst, even)
#         if result:
#             print(f"Number {lst} is even")
#         else:
#             print(f"Number {lst} is not even")
#     elif choice == "n":
#         result = value(lst, add)
#         if result:
#             print(f"Number {lst} is not even")
#         else:
#             print(f"Number {lst} is even")
#     elif choice == "e":
#         print("Good bye")
#         break
#     else:
#         print("Choose the wrong choice between p and n")








#-------------------------homework 32 sice 2
# def avg(places=2):
#     numbers = []
#     def add_number(number):
#         nonlocal numbers
#         numbers.append(round(number, places))
#     def calculate():
#         nonlocal numbers
#         if len(numbers) == 0 :
#             return None
#         return round(sum(numbers) / len(numbers), places)
#     return add_number, calculate
# add_number, calculate = avg(2)
# add_number(5.456)
# add_number(7.545)
# add_number(2.897)
# average = calculate()
# print(f"Average value:{average}")




#--------homework 32 sice 2
# def word_count(text):
#     def count_word(words):
#         norm_text = text.lower()
#         norm_word = words.lower()
#         count = norm_text.count(norm_word)
#         return count
#     return count_word, text
# counter_world, texts = word_count("Hello world is good world")
# word = "world"
# count = counter_world(word)
# print(f"Word {word} count in text {count}")



#-----------homework 32 sice 1
# def power(a):
#     def calculate(base):
#         return base ** a
#     return calculate
# power2 = power(2)
# power3 = power(3)
# result = power2(2)
# result1= power3(2)
# print(result)
# print(result1)




#----------------homework 31 sice 5
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n -2)
#
# n = int(input("Give number Fibonacci:"))
# if n < 0:
#     print("The number must be unique")
# else:
#     result = fibonacci(n)
#     print(f"Number fibonacci = {n}")
#     print(f"Result with Fibonacci:{result}")








#homework 31 sice 4
# def recursive(a, b):
#     if a > b:
#         return 0
#     return a + recursive(a + 1, b)
# a = int(input("Give number 1:"))
# b = int(input("Give number 2:"))
# result = recursive(a, b)
# print(f"The sum of numbers from {a} to {b} inclusive:{result}")



#----------------------------homework 31 sice 3
# def stars(n, count=1):
#     if n > 0:
#         print(f"{count}>*|", end='')
#         stars(n - 1, count + 1)
# n = int(input("Give number star:"))
# stars(n)
# print()

#-------------------homework 31 sice 2
#from datetime import datetime
# def date(year1, math1, day1, year2, math2, day2):
#     date1 = datetime(year1, math1, day1)
#     date2 = datetime(year2, math2, day2)
#     delta = date2 - date1
#     return abs(delta.days)
# date1 = (2023, 8, 10)
# date2 = (2023, 8, 19)
# difference = date(*date1, *date2)
# print(f"|The difference between the two dates in {difference} days |")









#-----------------------------------homework 31 sice 1
# def square(*args):
#     squares = []
#     for num in args:
#         squares.append(num ** 2)
#     return squares
# print("-" * 10, "Part 1", "-" * 10)
#
# result = square(1, 2, 3, 4, 5)
# print(f"List = {result} ")
# def arguments(**kwargs):
#     squares = []
#     for num, value in kwargs.items():
#         if isinstance(value, (int, float)): #isinstance перевіряє що аргумент це число або число з значенням пілся крапки
#             squares.append(value ** 2)
#     return squares
# print("-" * 10, "Part 2", "-" * 10)
# result1 = arguments(number1=2, number2=3.5, number3=4)
# print(result1)
# def avg(*args, **kwargs):
#     total = sum(args)
#     count = len(args)
#     for name, value in kwargs.items():
#         if isinstance(value, (int, float)):
#             total += value
#             count += 1
#     if count == 0:
#         return 0
#     else:
#         return total / count
# print("-" * 10, "Part 3", "-" * 10)
# result2 = avg(1, 2, 3, number4=4, number5=5.5)
# print(result2)
# result_with_zero = avg()
# print(f"Average no data available = {result_with_zero} ")
# print("-" * 10, "The end", "-" * 9)


#----------------------------homework 30 sice 5
# def multiple_list(lst):
#     result = 1
#     for num in lst:
#         result *= num
#     return result
# my_list = [1, 2, 3, 4, 5]
# result = multiple_list(my_list)
# print(result)
# print("-" * 20)
# def multiple_args(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
# result2 = multiple_args(2, 3, 4)
# result3 = multiple_args(5, 6, 7, 8)
# print(result2, "-" * 20, sep="\n")
# print(result3, "-" * 20, sep="\n")






#----------------------------->homework 30 sice 4
# def filter(number, add_tf):
#     num = []
#     for i in number:
#         if add_tf and i % 2 != 0:
#             num.append(i)
#         elif not add_tf and i % 2 == 0:
#             num.append(i)
#     return num
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# true_numbers = filter(my_list, True)
# false_numbers = filter(my_list, False)
# print(true_numbers)
# print(false_numbers)




#-------------------------------->homework 30 sice 3
# def values(a, b):
#     if a > 0 and b > 0:
#         return a + b
#     elif a < 0 and b < 0:
#         return a - b
#     else:
#         return 0
#
# result1 = values(3, 2)
# result2 = values(-5, -2)
# result3 = values(2, -2)
# result4 = values(0, 3)
#
# print("=" * 10 , "Version 1", f"{result1:^10}", sep="\n")
# print("=" * 10 , "Version 2", f"{result2:^9}", sep="\n")
# print("=" * 10 , "Version 3", f"{result3:^10}", sep="\n")
# print("=" * 10 , "Version 4", f"{result4:^10}", "=" * 10, sep="\n")






#--------------------->homework 30 sice 2
# def remove(lst, num):
#     count = 0
#     while num in lst:
#         lst.remove(num)
#         count += 1
#     return count
# my_list = [1, 2, 3, 4, 2, 5, 6, 2]
# print(f"Original list = {my_list}")
# num_remove = 2
# remove_count = remove(my_list, num_remove)
# print(f"Number {num_remove} in deleted items = {remove_count}")
# print(f"New list = {my_list}")








#---------------------->homework 26 sice 3
# def print_empleuess_table(employees):
#     print("\nСписок працівників")
#     print("\n{:<10} {:<30} {:<15} {:<30} {:<20} {:<10}".format(
#         "Номер",
#         "ПІБ",
#         "Телефон",
#         "Email",
#         "Посада",
#         "Кабінет"
#     ))
#     print("=" * 120)
#     for employee_id, employee_data in employees.items():
#         print("{:<10} {:<30} {:<15} {:<30} {:<20} {:<10}".format(
#         employee_id,
#         employee_data["ПІБ"],
#         employee_data["Телефон"],
#         employee_data["Email"],
#         employee_data["Посада"],
#         employee_data["Кабінет"]
#         ))
#     print("=" * 120)
#
#
# employees = {}
# while True:
#     print("\nМеню:")
#     print("1. Додати працівника")
#     print("2. Видалити працівника")
#     print("3. Знайти працівника")
#     print("4. Змінити дані працівника")
#     print("5. Вивести список працівників")
#     print("6. Вийти")
#
#     choic = input("Оберіть операцію")
#
#     if choic == "1":
#         employee_id = input("Ведіть номер працівника")
#         pib = input("ПІБ працівника")
#         phone = input("Вкажіть номер телефону працівника")
#         email = input("Вкажіть email працівника")
#         position = input("Вкажіть посаду працівника")
#         room = input("Вкажіть кабінет працівника")
#         employees[employee_id] = {
#             "ПІБ": pib,
#             "Телефон": phone,
#             "Email": email,
#             "Посада": position,
#             "Кабінет": room,
#         }
#         print("Працівника додано успішно")
#     elif choic == "2":
#         employee_id = input("Вкажіть номер працівника якого потрібно видалити")
#         if employee_id in employees:
#             del employees[employee_id]
#             print("Працівника успішно видалино")
#         else:
#             print("Працівника з таким номером не існує")
#     elif choic == "3":
#         employee_id = input("Вкажіть номер працівника")
#         if employee_id in employees:
#             print_empleuess_table({employee_id: employees[employee_id]})
#         else:
#             print("Працівника з таким номером не існує")
#     elif choic == "4":
#         employee_id = input("Вкажіть номер працівника дані якого ви хочете змінити")
#         if employee_id in employees:
#             print("Поточні дані працівника")
#             print_empleuess_table({employee_id: employees[employee_id]})
#
#             pib = input("Вкажіть нові ПІБ працівника")
#             phone = input("Вкажіть новий номер працівника")
#             email = input("Вкажіть новий Email працівника")
#             position = input("Вкажіть нову посаду працівника")
#             room = input("Вкажіть нову кімнату працівника")
#
#             employees[employee_id]["ПІБ"] = pib
#             employees[employee_id]["Телефон"] = phone
#             employees[employee_id]["Email"] = email
#             employees[employee_id]["Посада"] = position
#             employees[employee_id]["Кімната"] = room
#             print("Дані працівника зміннено успішно")
#         else:
#             print("Працівника з таким номером не існує")
#     elif choic == "5":
#         print_empleuess_table(employees)
#     elif choic == "6":
#         break
#     else:
#         print("Операцію обрано не вірно оберіть знову")





#------------------------------------homework 26 sice 4
# def roman(roman_numeral):
#     roman_numerals = {
#         'I': 1,
#         'IV': 4,
#         'V': 5,
#         'IX': 9,
#         'X': 10,
#         'XL': 40,
#         'L': 50,
#         'XC': 90,
#         'C': 100,
#         'CD': 400,
#         'D': 500,
#         'CM': 900,
#         'M': 1000
#     }
#     reslut = 0
#     i = 0
#     while i < len(roman_numeral):
#         if i + 1 < len(roman_numeral) and roman_numeral[i:i:+2] in roman_numerals:
#             reslut += roman_numerals[roman_numeral][i:i:+2]
#             i += 2
#         else:
#             reslut += roman_numerals[roman_numeral[i]]
#             i += 1
#         return reslut
#
# while True:
#     roman_input = input("Введіть римське число (або введыть 'exit' для виходу)")
#     if roman_input.lower() == 'exit':
#         break
#
#     integer_v = roman(roman_input)
#     parts = []
#
#     for symbol in roman_input:
#         parts.append(f"{symbol} = {roman(symbol)}")
#
#     explanation = ', '.join(parts)
#     print(f"Input: {roman_input}")
#     print(f"Output: {integer_v}")
#     print(f"Explanation: {explanation}\n")



#-------------------------homework 29 sice 7
# def user_name(username="Guest"):
#     print(f"Hello {username}")
# print(("-" * 10), "Part 1", ("-" * 10))
# user_name("Alex")
# user_name()
# print(("-" * 10), "Part 2", ("-" * 10))
# def user_names(*usernames):
#     for username in usernames:
#         print(f"Pople = {username}")
#
# user_names("Alex", "Emeli", "Jhon")
# print(("-" * 10), "Part 3", ("-" * 10))
# def user_info(**info):
#     print(f"User info - {info}")
#     for key, value in info.items():
#         print(f"{key}: {value}")
# user_info(name="Anton", age=28, email="Anton@gmail.com", score=12)


#---------------------------------homework 29 sice 6
# def len_number(a):
#     return len(str(a))
# result = len_number(3465)
# print(f"Len numbers = {result}")



#homework 29 sice 7
# def palindrome(numbers):
#     num_str = str(numbers)
#     revered_num = num_str[::-1]
#     return num_str == revered_num
#
# print(f"Polindrome (234432) = {palindrome(234432)}")
# print(f"Polindrome (567765) = {palindrome(567765)} ")
# print(f"Polindrome (453675) = {palindrome(453675)}")

#------------------------------home work 29 sice 5
# def calculate(a, b):
#     if a > b:
#         a, b, = b, a
#     product = 1
#     for number in range(a, b + 1):
#         product *= number
#     return product
# result = calculate(25, 5)
# print(f"Result = {result}")









#---------------------------------------------homework 29 sice 4
# def min_number(a, b, c, d, e):
#     return min(a, b, c, d, e)
#
# result = min_number(8, 4, 3 ,1, 9)
# print(f"Minimal result = {result}")

#---------------------------------------------homework 29 sice 3
# def display_square(side, symbol, filled):
#     if filled:
#         for _ in range(side):
#             print(symbol * side)
#     else:
#         print(symbol * side)
#         for _ in range(side - 2):
#             print(symbol + " " * (side - 2) + symbol)
#         print(symbol * side)
# #Заповнений
# display_square(5, "*", True)
# #Пустий
# display_square(4, "#", False)

#----------------------------------------home work 29 sice 2
# def even_numbers(start, end):
#     for number in range(start,end + 1):
#         if number % 2 == 0:
#             print(number)
#
# even_numbers(2,20)



#------------------------------------------------------------------------homework 29 sice 1
# def formatted_text():
#     text = """
#     “Don’t compare yourself with anyone in this world…
#        if you do so, you are insulting yourself.”
#                                             Bill Gates
#     """
#     print(text)
#
# formatted_text()



#----------------------------------------------------homework 28 sice 2
# world = {
#     'Germany': {'cw': 'Europe', 'ns': '154864', 'sq': '13189 KM^2'},
#     'Ukraine': {'cw': 'Europe', 'ns': '467591', 'sq': '6248 KM^2'},
#     'Egypt': {'cw': 'Africa', 'ns': '7891416', 'sq': '1488228 KM^2'},
#     'Nigeria': {'cw': 'Africa', 'ns': '77804', 'sq': '99648 KM^2'},
#     'China': {'cw': 'Asia', 'ns': '987654321', 'sq': '9137462 KM^2'},
#     'USA': {'cw': 'North America', 'ns': '193764825', 'sq': '1230540 KM^2'},
#     'Brazil': {'cw': 'South America', 'ns': '123456789', 'sq': '894484 KM^2'},
#     'Canada': {'cw': 'North America', 'ns': '456852', 'sq': '69874 KM^2'},
#     'India': {'cw': 'Asia', 'ns': '87864', 'sq': '987697 KM^2'},
#     'Finland': {'cw': 'Europe', 'ns': '28613', 'sq': '81468 KM^2'}
# }
# for country, data in world.items():
#     data['ns'] = int(data['ns'])
#     data['sq'] = int(data['sq'].split()[0])
# print("{:<15} {:.<15}".format("Country", "Continent", "Population Density", "Area(sq km)"))
# print("-" * 20)
# for country, data in world.items():
#     continent = data['cw']
#     population_density = data['ns'] / data['sq']
#     area = data['sq']
#
# #population
# total_population = sum(data['ns'] for data in world.values())
# print("\nTotal Population", total_population)
#
# #country for minimal people
# min_population_country = min(world, key=lambda country: world[country]['ns'])
# print("Country with the minimum population", min_population_country)
#
# #poplation with Asia
# asia_population = sum(data['ns'] for data in world.values() if data['cw'] == "Asia")
# print("Population living only in Asia", asia_population)
#
# #information in country terretory
# print("\n{:<15} {:<15}".format("Country", "Area (sq km)"))
# print("-" * 30)
# for country, data in world.items():
#     if data['cw'] == 'Europe':
#         print("{:<15} {:<15}".format(country, data['sq']))
# #min terry
# min_terry = min(key=lambda country: country['sq'])
# print(f"\nCountry with the minimal area: {min_terry}")





#-----------------------------------------------------------------homework 28 sice 1
# data = {
#     193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
#     209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
#     746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
#     109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
#     984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
#     765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
#     598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
#     483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
#     277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
# }
#
# filtered_data_age_above_30 = {id: person for id, person in data.items() if person["age"] > 30}
# print("People with age above 30:")
# for id, person in filtered_data_age_above_30.items():
#     print(f"ID: {id}, Name: {person['name']}, Age: {person['age']}")
# print()
#
# python_skills_people = {id: person for id, person in data.items() if "python" in person["skills"]}
# print("People with Python skills:")
# for id, person in python_skills_people.items():
#     print(f"ID: {id}, Name: {person['name']}")
# print()
#
# python_skills_above_5 = {id: person for id, person in python_skills_people.items() if person["skills"]["python"] > 5}
# average_age = sum(person["age"] for person in python_skills_above_5.values()) / len(python_skills_above_5)
# print("People with Python skills and rating above 5:")
# for id, person in python_skills_above_5.items():
#     print(f"Name: {person['name']}, Age: {person['age']}")
# print(f"\nAverage age: {average_age:.0f}")






#----------------------------------------------------------homework 27 sice 4
# students = {
#     'cartman': 10,
#     'stan': 12,
#     'kyle': 9,
#     'kenny': 10,
#     'lisa': None,
#     'jon': 12,
# }
# students_with = {k.capitalize(): v for k, v in students.items()}
# #print(students_with)
# print("{:<10} {:<10}".format("Student", "Score"))
# print("-" * 20)
# for name, score in students_with.items():
#     score_text = str(score) if score is not None else "N/A"
#     print("{:<10} {:<10}".format(name, score_text))
#
# scores = [score for score in students_with.values() if score is not None]
# avg_score = sum(scores) / len(scores)
# print("\nAverage score:", avg_score)
#
# max_score = max(scores)
# student_with_max_score = [name for name,score in students_with.items() if score == max_score]
# print("Students with the highest score:", ", ".join(student_with_max_score))
#
# student_without_scores = [name for name, score in students_with.items() if score is None]
# print("Students without scores:", ", ".join(student_without_scores))

#-----------------------------------------------------------------------homework27 sice 3
# bank = {1: 8, 2: 4, 5: 20, 10: 5, 50: 2, 100: 20}
# total_amount = sum(k * v for k, v in bank.items())
# print(f"All money = {total_amount}")
#
# max_v = max(bank.values())
# max_dict = {k: v for k, v in bank.items() if v == max_v}
# print(f"Dictionary only with denominations:{max_dict}")



#------------------------------------------------------------------------------homework 27 sice 2
# k = ["apple", "banana", "cherry", "date", "elderberry"]
# v = [5, 10, 3, 8, 15]
#
# dictionary = dict(zip(k, v))
# min_v = min(v)
# min_k = [k for k, v in dictionary.items() if v == min_v]
# print(f"Keys min value:", min_k)
# avg = sum(v) / len(v)
# avg_k = [k for k, v in dictionary.items() if v > avg]
#
# print("\nKeys values avg")
# print(avg_k)



#---------------------------------------------------------------home work 27 sice 1
# employees = [
#     {"name": "John Mckee", "age": 38, "department": "Sales"},
#     {"name": "Lisa Crawford", "age": 29, "department": "Marketing"},
#     {"name": "Sujan Patel", "age": 33, "department": "HR"}
# ]
#
# new_person = {"name": "Lari Smith", "age": 23, "department": "Logistic"}
# employees.append(new_person)
#
# for employee in employees:
#     first_name, last_name = employee["name"].split()
#     birth_year = 2023 - employee["age"]
#     department = employee["department"]
#
#     print(f"First Name: {first_name}")
#     print(f"Last Name: {last_name}")
#     print(f"Year of Birth: {birth_year}")
#     print(f"Department: {department}")
#     print("-" * 20)
#     print()











# countries = set()
#
# def add_country(country):
#     countries.add(country)
#     print(f"Країна '{country}' додана до множини.")
#
# def remove_country(country):
#     if country in countries:
#         countries.remove(country)
#         print(f"Країна '{country}' видалена з множини.")
#     else:
#         print(f"Країни '{country}' немає у множині.")
#
# def search_country(keyword):
#     matching_countries = [country for country in countries if keyword in country]
#     print("Знайдені країни:", matching_countries)
#
# def check_country_existence(country):
#     if country in countries:
#         print(f"Країна '{country}' знаходиться у множині.")
#     else:
#         print(f"Країни '{country}' немає у множині.")
#
# while True:
#     print("\nМеню:")
#     print("1. Додати країну")
#     print("2. Видалити країну")
#     print("3. Пошук країн за символами")
#     print("4. Перевірити наявність країни")
#     print("5. Вийти")
#
#     choice = input("Виберіть пункт меню: ")
#
#     if choice == '1':
#         country = input("Введіть назву країни: ")
#         add_country(country)
#     elif choice == '2':
#         country = input("Введіть назву країни: ")
#         remove_country(country)
#     elif choice == '3':
#         keyword = input("Введіть символи для пошуку: ")
#         search_country(keyword)
#     elif choice == '4':
#         country = input("Введіть назву країни: ")
#         check_country_existence(country)
#     elif choice == '5':
#         print("Дякую за використання меню!")
#         break
#     else:
#         print("Невірний вибір. Спробуйте ще раз.")






#homework 26 sice 2
# str = input("give words for space")
# words = str.split()
# word_count = {}
# letter = set()
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
#     letter.update(set(word))
# print("Different words and their number")
# for word, count in word_count.items():
#     print(f"{word}: {count}")
# unique = len(letter)
# print(f"Number of different letters = {unique}")




#homework 26 sice 1
# tuple1 = ['b', 'a', 'd', 'b', 'a', 'd', 'h', 'g']
# tuple2 = ['g', 'b', 'e', 'c', 'a', 'b', 'h', 'b']
# union_elment = set(tuple1) | set(tuple2)
# print(union_elment)
# intersection_element = set(tuple1) & set(tuple2)
# print(intersection_element)
# exclusive_element = set(tuple1) ^ set(tuple2)
# print(exclusive_element)
# element_in_tuple2_not_in_tuple1 = set(tuple1) - set(tuple2)
# uniq_element1 = [item for item in tuple1 if tuple1.count(item) == 1]
# print(uniq_element1)
# same_position = [item1 for item1, item2 in zip(tuple1, tuple2) if item1 == item2]
# print(same_position)




#homework 25 sice 3
# import random
# r_sequ = [random.randint(1,100) for _ in range(10)]
# even_number = sorted(filter(lambda x: x % 2 == 0, r_sequ))
# odd_number = sorted(filter(lambda x: x % 2 != 0, r_sequ), reverse=True)
# all_tuple = tuple(even_number + odd_number)
# print(f"Started list = {r_sequ}")
# print(f"Sorted tuple = {all_tuple}")


#homework 25 sice 2
# lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# tpl = tuple(sorted(lst))
# temp = tuple(item for item in tpl if len(item) == 5)
# print(f"Sorted tuple = {tpl}")
# print(f"Element 5 in tuple = {temp}")





#homework 25 sice 1
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6, 7, 8, 9)
#
# var1 = tuple1
# var2 = tuple2
# l1 = len(var1)
# l2 = len(var2)
# print(f"Tuple 1 = {l1}, Tuple 2 = {l2}")
# elemet = tuple1[1]
# print(f"tuple 1, two element = {elemet}")
# last_element = tuple2[3:]
# print(f"thre last elemet = {last_element}")
# all_element = tuple1 + tuple2
# print(f"All tuple = {all_element}")
# x, y, z = all_element[:3]
# print(f"x elemet = {x}, y element = {y}, z element = {z}")
# swap = x, y = y, x
# print(f"swap element x = {swap[0]}, swap element y = {swap[1]}")





# import random
#
# def heapify_desc(arr, size_heap , root):
#     lergest = root
#     left_cheld = 2 * root + 1
#     right_cheld = 2 * root + 2
#     if left_cheld < size_heap and arr[root] < arr[left_cheld]:
#         lergest = left_cheld
#     if right_cheld < size_heap and arr[lergest] < arr[right_cheld]:
#         lergest = right_cheld
#     if lergest != root:
#         arr[root], arr[lergest] = arr[lergest], arr[root]
#         heapify_desc(arr, size_heap, lergest)
#
# def heap_sort_desc(lst):
#     n = len(lst)
#
#     for i in range(n// 2 - 1, -1, -1):
#         heapify_desc(lst, n, i)
#
#     for i in range(n - 1, 0, -1):
#         lst[i], lst[0] = lst[0], lst[i]
#         heapify_desc(lst, i, 0)
#
# def heapify_asc(arr, size_heap , root):
#     smallest = root
#     left_cheld = 2 * root + 1
#     right_cheld = 2 * root + 2
#     if left_cheld < size_heap and arr[root] > arr[left_cheld]:
#         smallest = left_cheld
#     if right_cheld < size_heap and arr[smallest] < arr[right_cheld]:
#         smallest = right_cheld
#     if smallest != root:
#         arr[root], arr[smallest] = arr[smallest], arr[root]
#         heapify_asc(arr, size_heap, smallest)
#
# def heap_sort_asc(arr):
#     n = len(arr)
#
#     for i in range(n // 2 - 1, -1, -1):
#         heapify_asc(arr, n, i)
#
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify_asc(arr, i, 0)
# def generate_ident_codes(n):
#     return [random.randint(100000, 999999) for _ in range(n)]
#
# def generate_phone_numbers(n):
#     phone_numbers = []
#     for _ in range(n):
#         phone = "+380"
#         for _ in range(9):
#             phone += str(random.randint(0, 9))
#         phone_numbers.append(phone)
#     return phone_numbers
#
# def print_contacts(codes, phones):
#     for code, phone in zip(codes, phones):
#         print(f"Ідентифікаційний код: {code}, Телефонний номер: {phone}")
#
# ident_codes = generate_ident_codes(10)
# phone_numbers = generate_phone_numbers(10)
#
# while True:
#     print("\nМеню:")
#     print("1. Відсортувати за ідентифікаційними кодами за зростанням")
#     print("2. Відсортувати за номерами телефонів за спаданням")
#     print("3. Вивести список користувачів з кодами та телефонами")
#     print("4. Вихід")
#
#     choice = input("Оберіть операцію (1/2/3/4)")
#
#     if choice == "1":
#         heap_sort_asc(ident_codes)
#         print("Список відсортовано за індетифікаційним кодом у порядку зростання")
#         print_contacts(ident_codes, phone_numbers)
#     elif choice == "2":
#         heap_sort_desc(phone_numbers)
#         print("Список номерів телефону у порядку зростання")
#         print_contacts(ident_codes, phone_numbers)
#     elif choice == "3":
#         print("Cписок користувачів з кодами та телефонами")
#         print_contacts(ident_codes, phone_numbers)
#     elif choice == "4":
#         print("До побачення!")
#         break
#     else:
#         print("Оберіть коректну операці")





# home work24/2
# import random
#
#
# def heapify(arr, size_heap , root):
#     lergest = root
#     left_cheld = 2 * root + 1
#     right_cheld = 2 * root + 2
#     if left_cheld < size_heap and arr[root] < arr[left_cheld]:
#         lergest = left_cheld
#     if right_cheld < size_heap and arr[lergest] < arr[right_cheld]:
#         lergest = right_cheld
#     if lergest != root:
#         arr[root], arr[lergest] = arr[lergest], arr[root]
#         heapify(arr, size_heap, lergest)
# def heap_sort(lst):
#     n = len(lst)
#
#     for i in range(n// 2 - 1, -1, -1):
#         heapify(lst, n, i)
#
#     for i in range(n - 1, 0, -1):
#         lst[i], lst[0] = lst[0], lst[i]
#         heapify(lst, i, 0)
#
# def binar(arr, target):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return  None
# list = [random.randint(0,100) for _ in range(20)]
# print(list)
# heap_sort(list)
# print(f"Відсортований список:{list}")
# user = input("Введіть число для пошуку:")
# if not user.isdigit():
#     print("Вкажыть число для пошуку")
#     exit()
#
# number = int(user)
#
#
# if list:
#     result = binar(list, number)
#     if result is not None:
#         print(f"Елемент:{number} має індекс {result}")
#     else:
#         print(f"Елемент {number} не знайдено в списку")
# else:
#     print("Список порожній")






#home work 24/1
# import random
# def linear_search(lst, target):
#     last_index = None
#     for i in range(len(lst) - 1, -1, -1):
#         if lst[i] == target:
#             last_index = i
#             break
#     return last_index
# random_list = [random.randint(0, 9) for _ in range(20)]
# print(random_list)
# user_input = input("Ведіть число для пошуку (0/9):")
# if not user_input.isdigit():
#     print("Ведіть коректне число")
#     exit()
# number = int(user_input)
# result = linear_search(random_list, number)
# if result is not None:
#     print(f"Останнє входження числа {number} має індекс: {result}")
# else:
#     print(f"Число {number} не знайдено в списку або список порожній.")







import random

# def merge_srt_recursive(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)// 2
#     left = arr[:mid]
#     rirght = arr[mid:]
#
#     left = merge_srt_recursive(left)
#     rirght = merge_srt_recursive(rirght)
#     return merge(left, rirght)
#
# def intervetive(arr):
#     if len(arr) <= 1:
#         return arr
#     que = [[x] for x in arr]
#     while len(que) > 1:
#         fist = que.pop(0)
#         second = que.pop(0)
#         merged = merge(fist, second)
#         que.append(merged)
#     return que[0]
#
# def merge(left, right):
#     merged = []
#     left_index = 0
#     right_index = 0
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] <= right[right_index]:
#             merged.append(left[left_index])
#             left_index += 1
#         else:
#             merged.append(right[right_index])
#             right_index += 1
#
#     while left_index < len(left):
#         merged.append(left[left_index])
#         left_index += 1
#     while right_index < len(right):
#         merged.append(right[right_index])
#         right_index += 1
#     return merged
#
# N = 15
# arr = [random.randint(1,20) for _ in range(N)]
# print(f"Орігинальний рядок аrr:{arr}")
# #Рекурсине сортвування
# recursive_sort = merge_srt_recursive(arr.copy())
# print(f"Рекурсивне сортування:{recursive_sort}")
# #Інтернативне сортування
# intervetive_sort = intervetive(arr.copy())
# print(f"Інтернативне сортування:{intervetive_sort}")













# import random
#
# def sell_sort(arr):
#     exchanges = 0
#     n = len(arr)
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] < temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#                 exchanges += 1
#             arr[j] = temp
#         gap //= 2
#         print(f"Step {gap}: {arr}")
#     return exchanges
#
# def insertion(arr):
#     n = len(arr)
#     exchanges = 0
#     for i in range(1,n):
#         temp = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] < temp:
#             arr[j + 1] = arr[j]
#             j -= 1
#             exchanges += 1
#         arr[j + 1] = temp
#     return exchanges
#
# N = 13
# arr = [random.randint(0, 20) for _ in range(N)]
#
# print(f"Original lst:{arr}")
# shell_ex = sell_sort(arr.copy())
# print(f"Shell sort:{arr}")
# print(f"Number of exchanges shell sort:{shell_ex}")
# arr = [random.randint(0,20)for _ in range(N)]
# insert_ex = insertion(arr.copy())
# print(f"Sorted list insertion:{arr}")
# print(f"Number of exchanges(Insertion sort):{insert_ex}")





















# #home work 20
# import random
#
# s = [20, 100, 1000]
# def selection(num):
#     cm = 0
#     swap = 0
#     n = len(num)
#     for i in range(n - 1):
#         max_index = i
#         for j in range(i + 1, n):
#             cm += 1
#             if num[j] > num[max_index]:
#                 max_index = j
#         if max_index != i:
#             num[i], num[max_index] = num[max_index], num[i]
#             swap += 1
#     return cm, swap
#
#
# def insertion(num):
#     cm = 0
#     swap = 0
#     n = len(num)
#     for i in range(1, n):
#         key = num[i]
#         j = i - 1
#         while j >= 0 and num[j] < key:
#             cm += 1
#             num[j + 1] = num[j]
#             swap += 1
#             j -= 1
#         num[j + 1] = key
#     return cm, swap
#
#
# for i in s:
#     #Вибір
#     num = [random.randint(1, 100) for _ in range(i)]
#     n_selection = num.copy()
#     cm_selection, swap_selection = selection(n_selection)
#     print(f"\n Сортуванням вибором для N = {s}")
#     print("Відсортований список", n_selection)
#     print(f"C = {cm_selection}")
#     print(f"E = {swap_selection}")
#
#     #Вставка
#     n_insertion = num.copy()
#     cm_insertion, swap_insertion = insertion(n_insertion)
#     print(f"\nСортування вставкою для N = {s}")
#     print("Відсортований список", n_insertion)
#     print(f"C = {cm_insertion}")
#     print(f"E = {swap_insertion}")



















# num = [8, 3, 7, 4, 1, 9, 6, 2, 5]
# print(f"Рядок без сортування {num}")
# n = len(num)
# for i in range(n - 1):
#     swap = 0
#     for j in range(n - i - 1):
#         if num[j] < num[j + 1]:
#             num[j], num[j + 1] = num[j + 1], num[j]
#             swap += 1
#     if swap == 0:
#         break
# print(num)
# print(swap)












#Home work 19 numbe r1
# def sort_book_or_name(book, year):
#     #Метод сортування бульбашка
#     n = len(book)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if book[j] > book[j + 1]:
#                 book[j], book[j + 1] = book[j + 1], book[j]
#                 year[j], year[j + 1] = year[j + 1], year[j]
#     print("Список посортовано в алфавітному порядку")
#
# def sort_book_or_year(book, year):
#     n = len(year)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if year[j] > year[j + 1]:
#                 year[j], year[j + 1] = year[j + 1], year[j]
#                 book[j], book[j + 1] = book[j + 1], book[j]
#     print("Список посортовано за роком випуску за спадінням")
# def display(book, year):
#     print("Список книг")
#     for i in range(len(book)):
#         print(f"{book[i]} ({year[i]})")
#
# book = ["Book1", "Book3", "Book2", "Book4"]
# year = [2010, 2005, 2015, 2000]
# while True:
#     print("\nМеню:")
#     print("1. Відсортувати за назвою книг в алфавітному порядку")
#     print("2. Відсортувати за роками випуску за спаданням")
#     print("3. Вивести список книг з назвами та роками випуску")
#     print("4. Вихід")
#
#     ice = input("Оберіть пункт меню (1-4)")
#     if ice == "1":
#         sort_book_or_name(book, year)
#         display(book, year)
#     elif ice == "2":
#         sort_book_or_year(book, year)
#         display(book, year)
#     elif ice == "3":
#         display(book, year)
#     elif ice == "4":
#         break
#     else:
#         print("Недійсний ввибрі")





















# num = input('Give numbers').split()
# num = [int(x)for x in num]
# avg = sum(num) / len(num)
# if avg > 0:
#     sort = sorted(num[:2 * len(num) // 3])
#     rev = num[2 * len(num) // 3:][::-1]
#     r = sort + rev
# else:
#     r = sorted(num[:len(num) // 3])
# print(f'Sorted list: {r}')





# st = list(range(3, 59))
# n = [num for num in st if num % 3 == 0]
# print(n)






# st = input('').split()
# st = [int(num) for num in st]
# p = sum(1 for num in st if num > 0)
# print(f'Pizetiv number:{p}')
# minn = min(st)
# maxx = max(st)
# print(f'Minimal number = {minn}')
# print(f'Maximal number = {maxx}')
# sq = [num**2 for num in st]
# print(f'Number for append = {sq}')







#task 3 mol
# array = [4, 3, 2, 10, 12, 1, 5, 6]
# n = len(array)
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if array[j - 1] > array[j]:
#             array[j], array[j - 1] = array[j - 1], array[j]
#         else:
#             break
# print(array)


#task 2 bable
# st = [6, 9, 4, 1, 5, 3, 7]
# n = len(st)
# for i in range(0, n-1):
#     for j in range(i + 1, n):
#         if st[j] < st[i]:
#             st[j], st[i] = st[i], st[j]
# print(st)

# #task 1 sort
# st = [12, 29, 25, 8, 32, 17, 40]
# n = len(st)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1, n):
#         if st[j] < st[min_index]:
#             min_index = j
#     if min_index != i:
#         temp = st[i]
#         st[i] = st[min_index]
#         st[min_index] = temp
# print(st)







# lst = input('Give number by space').split()
# lst = [int(num) for num in lst]
# avg = sum(lst) / len(lst)
# print(avg)
# #Розмір першої тритини списку
# s = len(lst) // 3
# #Сортування в порядку зростання
# if avg > 0:
#     first = sorted(lst[:2 * s])
# else:
#     first = sorted(lst[:s])
# #У зворотньому напрямку
# b = lst[2*s][::-1]
# sort = first + b
# print(f'Sorted list:{sort}')














# from random import randint, seed
# seed(23)
# n = 10
# lst = [randint(-10,10) for x in range(n)]
# number = 1
# for num in lst:
#     if num < 0 and num % 2 == 0:
#         number *= num
# print(lst)
# print(f"Sum elements index for 2 = {number}")
# ind = sum(lst[i] for i in range(len(lst)) if i % 3 == 0)
# print(f"Sum elements index for 3 = {ind}")
# min_lst = min(lst)
# max_lst = max(lst)
# min_sum = sum(lst[lst.index(min_lst) + 1: lst.index(max_lst)])
# print(f"Minimal end maximal sum = {min_sum}")
# un = []
# for i in lst:
#     if i < 0:
#         un.append(i)
# un_first = un[0]
# un_last = un[-1]
# summa = sum(un)
# print(f"Sum elements negative elements {summa}")













# data = """ Om Bhakta male 26 Mar 1976 1707.0
# Krishnin Kakar male 18 Apr 2011 2482.33333
# Neela Tara female 27 Apr 1995 529.33333
# Ajit Pandya male 21 Aug 2001 1231.33333
# Kavita Goda female 25 Jan 1986 1281.33333
# Avinash Tata male 20 Sep 2004 2767.0
# Narinder Raval male 23 Dec 2019 2309.66667"""
#
# a = data.splitlines()
# b = ["full_name", "gender", "age", "balance"]
# table = []
# for char in a:
#     elements = char.split()
#     full_name = " ".join(elements[:2])
#     gender = elements[2]
#     birthdata = " ".join(elements[3:6])
#     balance = float(elements[6])
#     age = 2023 - int(elements[5])
#     fbalance = "{:.2f}".format(balance)
#     table.append([full_name, gender, str(age), fbalance])
# width = [max(len(char[i])for char in table) for i in range(len(b))]
# #print(f'-- {width}')
# hed = " | ".join(b)
# print(hed)
# print("-" * len(hed))
# for row in table:
#     st = " | ".join("{:<}".format(data) for data in row)
#     print(st)










# data = """ Om Bhakta male 26 Mar 1976 1707.0
# Krishnin Kakar male 18 Apr 2011 2482.33333
# Neela Tara female 27 Apr 1995 529.33333
# Ajit Pandya male 21 Aug 2001 1231.33333
# Kavita Goda female 25 Jan 1986 1281.33333
# Avinash Tata male 20 Sep 2004 2767.0
# Narinder Raval male 23 Dec 2019 2309.66667"""

# a = data.splitlines()
# print(a)
# b = ["full_name", "gender", "age", "balance"]
# table = []
# for char in a:
#     elements = char.split()
#     full_name = " ".join(elements[:2])
#     gender = elements[2]
#     birthdata = " ".join(elements[3:6])
#     balance = float(elements[6])
#     age = 2023 - int(elements[5])
#     table.append([full_name, gender, age, balance])
# width = [max(len(str(char[i])) for char in table) for i in range(len(b))]
# #print(f'-- {width}')
# hed = " | ".join("{:<}".format(b[i], width[i])for i in range(len(b)))
# print(hed)
# print("-" * len(hed))
# for row in table:
#     st = "{:<} | {:^10s} | {:+2d} | {:6.2f}".format(*row, width[0], width[1])
#     print(st, sep="")
















# from random import randint, seed
# seed(23)
# n = 10
# lst = [randint(0,9) for x in range(n)]
# lst1 = [randint(0,9) for y in range(n)]
# print(lst)
# print(lst1)
# un = []
#
# for i in lst:
#     for char in lst1:
#         if i == char:
#             un.append(i)
# print(un)
# mi_lst = max(lst)
# minn_lst = min(lst)
# print(f'Max number list 1: {mi_lst} min nuber list 1: {minn_lst}')
# mi_lst1 = max(lst1)
# minn_lst1 = min(lst1)
# print(f'Max number list 2: {mi_lst1} min nuber list 2: {minn_lst1}')
# un2 = []
# for i in lst:
#     if i not in un2:
#         un2.append(i)
# un3 = []
# for i in lst1:
#     if i not in un3:
#         un3.append(i)
# print(f'Unique list 1: {un2}')
# print(f'Unique list 2: {un3}')













#task 6
# st = 'New Delhi New York Paris Prague York York'.split()
# uniq = []
# for x in st:
#     if x not in uniq:
#         uniq.append(x)
# count = len(uniq)
# print(count)
#task 5
#from random import randint, seed
# seed(23)
# n = 10
# lst = [randint(-9,9) for i in range(n)]
# print(lst)
# lst_n = sum([x for x in lst if x < 0])
# print(lst_n)
# d = 1
# for i in range(0, n, 3):
#     print(i , lst[i])
#     d = d * lst[i]
# print(d)
# n = min(lst)
# m = max(lst)
#
# n_indx = lst.index(min(lst))
# print(n_indx)
# m_index = lst.index(max(lst))
# print(m_index)
# star = min(n_indx, m_index)
# end = max(n_indx, m_index)
# for x in lst[star:end]:
#     d = d * x
# print(d)
#
# newlst = sorted(lst[:5]) + sorted(lst[5:], reverse=True)
# print(newlst)

#task 3
# lst = input('Enter number').split()
# lst_int = [int(x) for x in lst]
#
# num = int(input('Enter number'))
#
# caunt = lst.count(num)
# print(f'count number {caunt = }')
# print(lst_int)
# print(sum(lst_int), sum(lst_int) / len(lst_int))
# lst_n = [x*num for x in lst_int]
# print(lst_n)












#Task max numbe for lst
# studScores = [['Bob',11,8,10,12], ['Jane',12,11,11,11], ['Kate',7,8,9,9]]
#
# for i in studScores:
#     s = sum(i[1:])
#     n = max(i[1:])
#     print(f'{i[0:]} max number  {n}')
#     print()
#
# score = [ [i[0], max(i[1:])] for i in studScores]












# exp = input('Enter expression (number (+,-,* ,/) number').split()
# num1 = float(exp[0])
# op = exp[1]
# num2 = float(exp[2])
#
#
#
#
# if op == '+':
#     result = num1 + num2
# elif op == '-':
#     result = num1 - num2
# elif op == '*':
#     result = num1 * num2
# elif op == '/':
#     result = num1 / num2
# print(result)








# st = 'E:/Folder/folder/ MyItems/bin'
# v = st.split('/')
# print(v)
#
# v = [fold for fold in v if fold[0].islower() or 'i' in fold]
#
# for fold in v:
#     print(fold)












# st = 'Hi*my**friend***Jack'
# count = 0
# count1 = 0
# mcount = float('inf')
# v = st.split('*')
# v = [w for w in v if w]
# print(v)
# for char in st:
#     if char == '*':
#         count += 1
#         count1 = min(count, mcount)
#     else:
#         count = 0
# print(count1)










# st = 'Hi**my****friend***Jack'
# count = 0
# countm = 0
# text = []
# word = ''
# for char in st:
#     if char == '*':
#         if word:
#             text.append(word)
#             word = ''
#     else:
#         word += char
# if word:
#     text.append(word)
# print(f"text : {text}")
# for char in st:
#     if char == '*':
#         count += 1
#         countm = max(countm, count)
#     else:
#         count = 0
#
# print(f"Min * :{countm}")









# text = input('Enter text:')
#
# v = text.split()
# v_count = len(v)
# print(f'Number word = {v_count}')
#
# v_word = max(v, key=len)
# print(f'The longes word = {v_word}')







# text = input('Enter text:')
# let = input('Enter letters')
# count = 0
# for i in text:
#     if let in let:
#         count += 1
#
# print(f'Кількість введених букв у тексті = {count}')



# stv = input('Enter text')
# text = []
# count = 0
# for i in range(len(stv)):
#     if stv[i] == 'f':
#         count += 1
#         text.append(i)
#
# if count == 0:
#     print('No f')
# elif count == 1:
#     print(f'Index f = {text[0]}')
# else:
#     print(f'Index f  = {text[0]} end {text[-1]}')








# strng = "kdjhxkjkjxxkkjjxxxxxxxxxxxkjkj"
# often_symbol = ''
# max_symbol = 0
#
# for symbol in strng:
#     symbol_count = strng.count(symbol)
# if symbol_count > max_symbol:
#     max_symbol = symbol_count
#     often_symbol = symbol
# print('Найчастіший символ: {}, перше входження: {}, осеаннє входження: {}'.format(often_symbol, strng.find(often_symbol), strng.rfind(often_symbol)))
#task4
# n = input('your full name:')
# year = int(input('your year'))
# print(f"Hello, {n}")
# balance = 120.851788
# age = 2023 - year
# print(f'You age is {age:010d}')
# print(f"{age} in hex ={age:X}, {age} in bin {age:b}.")
# print(f"balance = {balance:>+4.2f}")
# print("Welcome".center(15,'*'))
#task5
# n = 'gjgh35h3jgjhr'
# count = 0
# for char in range(len(n)):
#     if n[char].isnumeric():
#         count += 1
# print(count)
#
# n = input('Text').lower()
# b = input('Reserv text').lower()
# count = n.count(b)
# print(count)




# coe = 'U+10ffff'
# code_clear = coe.lstrip("U+")
# code_hex = int(code_clear, 16)
# char = chr(code_hex)
# print(code_hex)




# st = 'ItStep'
# string = bytes(st, "utf-8")
# print(string)
# l = len(string)
# print(l)





# import string
#
# text = input("text->:")
#
# degits = "0123456789ABCDEF"
# count = 0
# pun = 0
# for char in text:
#     if char.upper() in degits:
#         count += 1
# for char in text:
#     if char in string.punctuation:
#         pun += 1
# print(f"Кількість шіснатиціткових цифр:{count}")
# print(f"Кількість знаків понктуації:{pun}")







# x = input("Enter text").upper()
# a = input("Reserved text").upper()
#
# if a in x:
#      print(f"Текст {a} знаходиться в тексті")
# else:
#     print(f"Слово  відсутнє ")







# x = input("Enter text")
#
# string = x.replace(" ", "").lower()
#
# if string == string[::-1]:
#     print(f"Ваш текст {x} є поліндромом")
# else:
#     print(f"Ваш текст {x} не є поліндромом")



# strng = " а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ь, ю, я "
# strng_bytes = bytes(strng, 'utf-8')
# print(strng_bytes)
# strin_cl = strng.replace(",", " ").replace(" ", "")
# l = len(strin_cl)
# print(f'Довжена рядка ={l}')
# char = 'клм'
# if char in strin_cl:
#     index = strin_cl.index(char)
#     print(f'{char} знаходиться у індексі {index}')
# else:
#     print(f'{char} немає в рядку')
#
# for i, j in enumerate(strin_cl,1):
#     code = ord(j)
#     print(f'Номер ітирації {i} символ={j} Код=символу{code}')






# string = 'abcdefghijklmnopqrstuvwxyz'
# l = len(string)
# print(l)
# print(f'1:{string[:27]}')
# print(f'2:{string[:1]}')
# print(f'3:{string[1:2]}')
# print(f'4:{string[-1:]}')
# print(f'5:{string[-2:-1]}')
# print(f'6:{string[3:7]}')
# print(f'7:{string[2:27]}')
# print(f'8:{string[:27]}')
# print(f'9:{string[20:]}')
# print(f'10:{string[-3:]}')
# print(f'11:{string[18:-4]}')
# print(f'12:{string[:27:3]}')
# print(f'13:{string[3:26:3]}')
# print(f'14:{string[:-27:-1]}')



# str = "«Я зараз вивчаю Python»"
# encodestr = str.encode('utf-8')
# decodestr = encodestr.decode('utf-8')
# smile = chr(128522)
# print(str, smile, sep='')
# print(encodestr)
# print(decodestr)


# max_char = 0
# string = ""
# for char in string:
#     if string.count(char) > max_char:
#         max_char = string.count(char)
# print(max_char)
#
# unique = ""
#
# for char in string:
#     if string.count(char) == max_char and char not in unique:
#         print(char, end=' ')
#         unique = unique + char
#task 3

# st = input('Number')
# if st == st[::-1]:
#     print('Числа починаються на одну цифру')
# else:
#     print('Числа не починаються на одну цифру')



#Task 2
# st = input('')
# count = 0
# for i in st:
#     if i.lower() == 'a':
#         print(count)
#Task 1
# n = input('')
# print(n.count(''))
# st = "Python ItStep"
#
# for char in st:
#     print(f'{char=}')
#
# l = len(st)
# print(f'{l=}')
#
# for i in range(l):
#     if st[i] == 'o':
#         print(f'{i=}')







# n = 5
#
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n-1 or j == i:
#             print("*" + ' ' + ' ', end="")
#         else:
#             print(" " + ' ' + ' ', end="")
#     print()





# n = int(input('Number'))
#
#
# for i in range(1,n + 1):
#     for j in range(n - i):
#         print(' ', end='')
#
#     for j in range(i):
#         print("#", end="")
#     print()









# max = 5
#
# attempt = 0
#
# paswword = 3223
# while attempt < max:
#     x = int(input('Give password:'))
#     if x == paswword:
#         print('Done')
#         break
#     print('Invalid password')
#     attempt += 1
# if attempt == max:
#     print('You have exceeded themaximum number of attempts')



# n = int(input('Number 1'))
# x = int(input('Number 2'))
# for i in range(n,x + 1):
#     for j in range(1,11):
#         k = i * j
#         print(f"{i} x {j} = {k}", end='\t')
#     print()






# n = int(input('Number'))
#
# count = []
#
# for i in range (2, n + 1):
#     if i > 1:
#         k = 'Число просте'
#         for j in range(2, i):
#             if (i % j) == 0:
#                 k = 'Число не просте'
#                 break
#         if k:
#             count += i,
# print(k)










# count = 0
# for i in range(100,1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     if a == b or a == c or b == c:
#         count += 1
# print(count)





# x = int(input('Number 1:'))
# n = int(input('Number 2:'))
# result = 1
# for i in range(n):
#     result *= x
#     if i == n-1:
#         print(x)
#     else:
#         print(x, end='*')
#
# print('=',result, sep='')






# summ = 0
# minn = None
# maxx = None
# while True:
#     number = int(input('Number:'))
#     if number == 7:
#         print('God Bye!')
#         break
#     summ += number
#     if maxx is None or number > maxx:
#         maxx = number
#     if minn is None or number < minn:
#         minn = number
# print('Summa', summ)
# print('Min', minn)
# print('Max', maxx)








# while True:
#     number = int(input('Number'))
#     if number == 7:
#         print('Good bye!')
#         break
#     if number > 0:
#         print('Number is positive')
#     elif number < 0:
#         print('Number is negative')
#     else:
#         print('Number is equal to zero')
#     break




















# x = int(input('Number 1:'))
# a = int(input('Number 2:'))
#
# sum_ofever = 0
# number_even = 0
# sum_ofnotever = 0
# number_noteven = 0
# sum_multiples_9 = 0
# number_multiples_9 = 0
#
#
# for i in range(x, a + 1):
#     if i % 2 == 0:
#         sum_ofever += i
#         number_even += 1
#     else:
#         sum_ofnotever += i
#         number_noteven += 1
#     if i % 9 == 0:
#         sum_multiples_9 += i
#         number_multiples_9 += 1
# sum_ever = sum_ofever / number_even if number_even != 0 else 0
# avg_notever = sum_ofnotever / number_noteven if number_noteven != 0 else 0
# avg_9 = sum_multiples_9 / number_multiples_9 if number_multiples_9 != 0 else 0
#
# print('Сума парних чисел:', sum_ofever)
# print('Сума не парних чисел:', sum_ofnotever)
# print('Сума кратних 9:', sum_multiples_9)
# print('Середнє арефметичне парних чисел:', sum_ever)
# print('Середнє арефметичне непарних чисел:', avg_notever)
# print('Середнє арефметичне чисил, кратиних 9:', avg_9)



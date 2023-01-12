import re

# tel = input('введите номер телефона: ')
# reg = r'^(([+]?[7]\s(([0-9]{3})|\([0-9]{3}\))\s([0-9]{3})(\s|\-)[0-9]{2})(\s|\-)[0-9]{2})|[+]?([0-9]){11}'
# math = re.fullmatch(reg,tel)
# print('Номер корректный' if math else 'Номер не корректный')


# Найти последовательность ['1','1','2','3']
# txt = '1X Text ABC 123 A1B2C3'
# reg = r'[ABC]?[^\d](\d)'
# a = re.findall(reg, txt)
# print(a)

# Найти текст от #START# до #END#
# txt = '#START# algjhaajhapohja #END#'
# reg = r'\s(\w*)\s'
# a = re.findall(reg, txt)
# print(a)

# Найти последовательность цифр, после которой идет ровно одно подчеркивание
# txt = '12_34__86'
# reg =r'(\d+)_\d?'
# a = re.findall(reg, txt)
# print(a)

# Вычислить колличество отрицательных чисел в списке используя рекурсию.
# lst = [-2,3,8,-11,-4,6]
# count = 0
# def num(lst):
#     global count
#     if not lst:
#         return
#     else:
#         first = lst[0]
#         if first <0:
#             count +=1
#         num(lst[1:])
#     return count
# num(lst)
# print(count)

# Не рекурсивный обход вложеного списка. Найти колличество элементов в списке.
# count =0
# def cycle():
#     global count
#     for z in t:
#         count +=1
#     return count
#         
# lst = ['Adam',["Bob", ["Chet",['Fix',['Max']], "Cat", ["Bea",['Oleg'], "Bill",['Bee'], "Bill"]], "Bard",['Bill','Bob'],"Bert"], 'Alex', ["Bea", "Bill"], 'Ann',['Fox']]
# for i in lst:
#     if isinstance(i, list):
#         for j in i:
#             if isinstance(j,list):
#                 for t in j:
#                     if isinstance(t,list):
#                         cycle()
#                         continue
#                     else:
#                         count +=1
#             else:
#                 count +=1
#     else:
#         count +=1
# print(count)


# Работа с файлами

# file = open('DZ','w')
# pos1 = file.write('Hello ')
# pos2 = file.write('World')
# file.close()
# with open('DZ','r') as file:
#     s = file.read(5)
#     z =file.read(6)
#     s,z = z,s
#     print(s,z)
# file.close()
# file = open('DZ','w+')
# pos1 = file.write(s)
# pos2 = file.write(z)
# file.close()


# Объеденить 2 файла в 1. Третий файл = Первый файл.Второй файл.

# with open('file1.txt','r') as f, open('file2.txt','r') as m, open('file3.txt', 'w+') as t:
#     text = f.readlines()
#     text2 = m.readlines()
#     text3 = ''.join((text + text2))
#     t.write(text3)


# ООП


# Реализовать класс Книга.Необходимо хранить в полях класса название книги, год выпуска, издатель, жанр, автор, цену.


# class Book:
#     name = 'name'
#     year = 'year'
#     publisher = 'publisher'
#     genre = 'genre'
#     autor = 'autor'
#     price = 'price'
#     
#     def input_info(self,first_name,year,publisher,genre,autor,price):
#         self.name = first_name
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.autor = autor
#         self.price = price
#     
#     def print_info(self):
#         print()
#         print("="*40)
#         print(f'Название книги: {self.name}\nГод выпуска: {self.year}\nИздатель: {self.publisher}\nЖанр: {self.genre}\nАвтор: {self.autor}\nЦена: {self.price}')
#         print("="*40)
#         
#         
#     def set_name(self,name):
#         self.name = name
#             
#     def get_name(self):
#         return self.name
#         
#         
#     def set_year(self,year):
#         self.yaer = year
#         
#     def get_year(self):
#         return self.year
#         
#         
#     def set_publisher(self,publisher):
#         self.publisher=publisher
#             
#     def get_publisher(self):
#         return self.publisher
#         
#         
#     def set_ganre(self,genre):
#         self.ganre = genre
#             
#     def get_genre(self):
#         return self.genre
#         
#         
#     def set_autor(self,autor):
#         self.autor=autor
#             
#     def get_autor(self):
#         return self.autor
#         
#         
#     def set_price(self,price):
#         self.price = price
#             
#     def get_price(self):
#         return self.price
# h1 = Book()
# h1.input_info('Пираты','1822','Constable and Co.','History','Walter Scott','150$')
# h1.print_info()
# print(h1.get_name())
# print(h1.get_autor())
# h1.set_price('100$')
# h1.print_info()            


# # Создать класс Reсtangle, описывающий прямоугольник. В классе должны быть все необходимые методы, а так же методы вычисления
# # площади,периметра и гипотенузы и метод который рисует прямоуголник.
# 
# import math
# class Reсtangle:
#     def __init__(self,long,width):
#         self.__long = self.__width = 0
#         if Reсtangle.__check_value(long) and Reсtangle.__check_value(width):
#             self.__long = long
#             self.__width = width
#             print('Длина прямоугольника: ',long)
#             print('Ширина прямоугольника: ',width)
#         else:
#             print("Ошибка данных")
#         
#     def __check_value(z):
#         if isinstance(z,int) or isinstance(z,float):
#             return True
#         return False
# 
#     def squre(self):
#         self.s = self.__long * self. __width
#         return self.s
#         
#     def perimetr(self):
#         self.p = 2 * (self.__long + self.__width)
#         return self.p
#      
#             
#     def hypotenuse(self):
#         hyp = self.__long ** 2 + self.__width ** 2
#         self.hypoten = round(math.sqrt(hyp),2)
#         return self.hypoten
#             
#         
#     def image(self):
#         for i in range(1,self.__long+1):
#             for j in range(1,self.__width+1):
#                 print('*', end = '')
#             print()
# 
#         
#         
# a1 = Reсtangle('a',9)
# print("Площадь прямоугольника: ", a1.squre())
# print('Периметр равен: ', a1.perimetr())
# print("Гипотенуза прямоугольника: ", a1.hypotenuse())
# a1.image()

# Создайте класс для подсчета площади геометрических фигур. Класс должен предоставлять функциональность для подсчета
# площади треугольника по разным формулам, площади прямоугольника, площади квадрата. Методы класса для подсчета площади
# должны быть реализованы с помощью статических методов. Также класс должен считать количество подсчетов площади и
# возвращать это значение с помощью статического метода.


# class Area:
#     __count = 0
# 
#     @staticmethod
#     def get_count():
#         return Area.__count
# 
#     @staticmethod
#     def geron(a, b, c):
#         Area.__count += 1
#         return (a + b + c) / 2
# 
#     def base(a, b):
#         Area.__count += 1
#         return (a * b) / 2
# 
#     def squre(a):
#         Area.__count += 1
#         return a ** 2
# 
#     def rectangle(a, b):
#         Area.__count += 1
#         return a * b
# 
# 
# print("Площадь по формуле Герона: ", Area.geron(3, 4, 5))
# print('Площадь треугольника через основание на высоту:', Area.base(6, 7))
# print('Площадь квадрата:', Area.squre(7))
# print('Площадь прямоугольника:', Area.rectangle(2, 6))
# print('вызов методов: ', Area.get_count())


# Создать класс для рассчета банковского депозита

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EURO"
# 
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежайщий {self.surname} был открыт.")
#         print("*" * 50)
# 
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежайщий {self.surname} был закрыт")
# 
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
# 
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
# 
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
# 
#     def edit_owner(self, surname):
#         self.surname = surname
# 
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
# 
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у Вас нет такой {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
# 
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} успешно добавлено!")
#         self.print_balance()
# 
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
# 
#     def convert_to_euro(self):
#         euro_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {euro_val} {Account.suffix_eur}")
# 
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
# 
#     def print_info(self):
#         print("Информация о счета")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent: .0%}")
#         print("-" * 20)
# 
# 
# acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_euro()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_euro()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percents()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# acc.withdraw_money(3000)

# Написать решение с помощью методов getter and setter

# class Account:
#     __rate_usd = 0.013
#     __rate_eur = 0.011
#     __suffix = "RUB"
#     __suffix_usd = "USD"
#     __suffix_eur = "EURO"
# 
#     def __init__(self, num, surname, percent, rate_usd, rate_eur, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         self.__rate_usd = rate_usd
#         self.__rate_eur = rate_eur
#         print(f"Счет #{self.__num} принадлежайщий {self.__surname} был открыт.")
#         print("*" * 50)
# 
#     def __del__(self):
#         print("*" * 50)
#         return f"Счет #{self.__num} принадлежайщий {self.__surname} был закрыт"
# 
#     def set_convert_usd(self, __value, __rate_usd):
#         return self.__value * self.__rate_usd
# 
#     def set_convert_eur(self, __value, __rate_eur):
#         return self.__value * self.__rate_eur
# 
#     @staticmethod
#     def set_eur_rate(rate_eur):
#         __rate_eur = rate_eur
# 
#     @staticmethod
#     def set_usd_rate(rate_usd):
#         __rate_usd = rate_usd
# 
#     def set_edit_owner(self, surname):
#         self.__surname = surname
# 
#     def set_add_percents(self, __percent):
#         self.__value += self.__value * self.__percent
#         self.get_print_balance()
#         return "Проценты были успешно начислены!"
# 
#     def get_withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у Вас нет такой {val} {Account.__suffix}")
#         else:
#             self.__value -= val
#             print(self.get_print_balance())
#         return f"{val} {Account.__suffix} было успешно снято!"
# 
#     def set_add_money(self, val):
#         self.__value += val
#         self.get_print_balance()
#         return f"{val} {Account.__suffix} успешно добавлено!"
# 
#     def get_convert_to_usd(self):
#         usd_val = Account.set_convert_usd(self, self.__value, self.__rate_usd)
#         return f"Состояние счета: {usd_val} {Account.__suffix_usd}"
# 
#     def get_convert_to_euro(self):
#         euro_val = Account.set_convert_eur(self, self.__value, self.__rate_eur)
#         return f"Состояние счета: {euro_val} {Account.__suffix_eur}"
# 
#     def get_print_balance(self):
#         return f"Текущий баланс {self.__value} {Account.__suffix}"
# 
#     def get_print_info(self):
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         print(self.get_print_balance())
#         print(f"Проценты: {self.__percent: .0%}")
#         return "-" * 20
# 
# 
# acc = Account("12345", "Долгих", 0.03, 0.013, 0.011, 1000)
# print(acc.get_print_balance())
# print(acc.get_print_info())
# print(acc.get_convert_to_usd())
# print(acc.get_convert_to_euro())
# print()
# acc.set_convert_usd(1500, 2)
# print()
# acc.set_edit_owner("Дюма")
# acc.set_add_money(5000)
# print(acc.get_print_info())
# print()
# acc.set_add_percents(5)
# print(acc.get_withdraw_money(3000))
# print()
# print(acc.get_withdraw_money(100))
# print()
# acc.get_withdraw_money(3000)


# Написать програаму для расчета банковского депозита с использованием метода property

# class Account:
#     __rate_usd = 0.013
#     __rate_eur = 0.011
#     __suffix = "RUB"
#     __suffix_usd = "USD"
#     __suffix_eur = "EUR"
# 
#     def __init__(self, num, surname, percent, rate_usd, rate_eur, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         self.__rate_usd = rate_usd
#         self.__rate_eur = rate_eur
#         print(f"Счет #{self.__num} принадлежайщий {self.__surname} был открыт.")
#         print("*" * 50)
# 
#     def __del__(self):
#         print("*" * 50)
#         return f"Счет #{self.__num} принадлежайщий {self.__surname} был закрыт"
#      
# 
#     def get_convert_usd(self):
#         return self.__value * self.__rate_usd
# 
#     def get_convert_eur(self):
#         return self.__value * self.__rate_eur
# 
#     @staticmethod
#     def set_eur_rate(rate_eur):
#         __rate_eur = rate_eur
# 
#     @staticmethod
#     def set_usd_rate(rate_usd):
#         __rate_usd = rate_usd
#         
# 
#     def set_edit_owner(self, surname):
#         self.__surname = surname
#         
# 
#     def set_add_percents(self, percent):
#         self.__percent = percent / 100
#         
#                 
#         
#     def get_percent(self):
#         self.__value += self.__value * self.__percent 
#         return "Проценты были успешно начислены!"
# 
#     def get_withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у Вас нет такой {val} {Account.__suffix}")
#         else:
#             self.__value -= val
#             self.get_print_balance()
#         return f"{val} {Account.__suffix} было успешно снято!"
# 
#     def set_add_money(self, val):
#         self.__value += val
#         self.get_print_balance()
#         return f"{val} {Account.__suffix} успешно добавлено!"
# 
#     def set_convert_usd(self):
#         usd_val = Account.set_convert_usd(self.__value)
#         return f"Состояние счета: {usd_val} {Account.__suffix_usd}"
# 
#     def set_convert_euro(self):
#         euro_val = Account.set_convert_eur(self, __value)
#         return f"Состояние счета: {euro_val} {Account.__suffix_eur}"
# 
#     def get_print_balance(self):
#         return f"Текущий баланс {self.__value} {Account.__suffix}"
# 
#     def get_print_info(self):
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         print(self.get_print_balance())
#         print(f"Проценты: {self.__percent: .0%}")
#         return "-" * 20
#     
#     usd = property(get_convert_usd, set_convert_usd)
#     eur = property(get_convert_eur, set_convert_euro)
#     total = property(get_print_balance, set_add_money)
#     percent = property(get_percent, set_add_percents)
# 
# 
# 
# acc = Account("12345", "Долгих", 0.03, 0.013, 0.011, 1000)
# print(acc.get_print_balance())
# print(acc.get_print_info())
# acc.percent = 5
# acc.total = 2500
# c = acc.total
# print(acc.get_print_info())
# print(acc.get_percent())
# print(acc.get_print_info())
# acc.set_add_money(170)
# print(acc.get_print_info())


# Реализовать класс "Автомобиль". необходимо хранить в полях класса, название модели, год выпуска, производитель,
# мощность двигателя, цвет, цена машины.Реализовать методы класса для ввода даных, вывода данных. реализовать доступ к
# отдельным полям через методы класса.


# import re
#
#
# class Auto:
#     def __init__(self, name, year, manufacture, power, color, price):
#         self.name = name
#         self.year = year
#         self.manufacture = manufacture
#         self.power = power
#         self.color = color
#         self.price = price
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.verify_name(name)
#         self.__name = name
#
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self, year):
#         self.verify_year(year)
#         self.__year = year
#
#     @property
#     def manufacture(self):
#         return self.__manufacture
#
#     @manufacture.setter
#     def manufacture(self, manufacture):
#         self.verify_manufacture(manufacture)
#         self.__manufacture = manufacture
#
#     @property
#     def power(self):
#         return self.__power
#
#     @power.setter
#     def power(self, power):
#         self.verify_power(power)
#         self.__power = power
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, color):
#         self.verify_color(color)
#         self.__color = color
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, price):
#         self.verify_price(price)
#         self.__price = price
#
#     @staticmethod
#     def verify_name(name):
#         if not isinstance(name, str):
#             raise TypeError("name, Должно быть строкой")
#         f = name.split()  # [X1]
#         if len(f) != 1:
#             raise TypeError("Неверный формат имени")
#         letters = "".join(re.findall('[A-z0-9]', name))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В имени можно использовать только буквы и числа!")
#
#     @staticmethod
#     def verify_year(year):
#         if not isinstance(year, int):
#             raise TypeError("year, должен быть числом")
#
#     @staticmethod
#     def verify_manufacture(manufacture):
#         if not isinstance(manufacture, str):
#             raise TypeError("manufacture, Должно быть строкой")
#
#     @staticmethod
#     def verify_power(power):
#         if not isinstance(power, int):
#             raise TypeError("Power, должно быть числом")
#
#     @staticmethod
#     def verify_color(color):
#         if not isinstance(color, str):
#             raise TypeError("color, Должно быть строкой")
#
#     @staticmethod
#     def verify_price(price):
#         if not isinstance(price, int):
#             raise TypeError("Price, должно быть числом")
#
#
# p1 = Auto('X7', 1958, "BMW", 530, "white", 1706452)
# p1.price = 123141
# print(p1.price)


# Создать базовый класс "Стол" и дочерние классы: Прямоугольные столы, квадратные и круглые столы. Через инициализатор
# базового класса передавать размер поверхности стола: прямоугольный - ширина и длина, квадратный - ширина или длина
# круглого - радиус. В дочерних классах реализовать метод вычисления площади поверхности стола.

# class Table:  # Класс "Стол"
#
#     def __init__(self, width, length):
#         self._width = width
#         self._length = length
#
#     def perimetr(self):
#         raise NotImplementedError("В дочернем классе отсутствует метод perimetr()")
#
#
# class Square(Table):  # Дочерний класс квадратный стол
#
#     def __init__(self, width, length):
#         super().__init__(width, length)
#
#     def perimetr(self):
#         if self._width == self._length:
#             return self._width ** 2
#         else:
#              raise NotImplementedError("В дочернем классе Square() неверные данные")
#
#
# class Rectangle(Table):  # Дочерний класс прямоугольный стол
#
#     def __init__(self, width, length):
#         super().__init__(width, length)
#
#     def perimetr(self):
#         return self._width * self._length
#
#
# class Ring(Table):  # Дочерний класс круглый стол
#
#     def __init__(self, width, length=0):
#         super().__init__(width, length)
#
#     def perimetr(self):
#         return 3.14 * self._width
#
#
# l = Rectangle(20, 10)
# z = Square(20, 20)
# x = Ring(20)
#
# print(z.perimetr())
# print(l.perimetr())
# print(round(x.perimetr(), 1))

# Создать класс Student, который будет содержать имя и распечатывать информацию. А так же вложенный класс,
# который будет содержать информацию о ноутбуке с техническими характеристиками модель, процессор и память.
# Roman    => HP, i7, 16
# Vladimir => HP, i7,16
#
# class Student:
#
#     def __init__(self, name, model, cpu, memory):
#         self._name = name
#         self.laptop = self.Laptop(model, cpu, memory)
#
#     def info(self):
#         print(f"{self._name} => {lap._model} {lap._cpu} {lap._memory}")
#
#     class Laptop:
#
#         def __init__(self, model, cpu, memory):
#             self._model = model
#             self._cpu = cpu
#             self._memory = memory
#
#
# t = Student("Roman", "HP", "i7", 16)
# v = Student("Vladimir", "Honor", 10, 25)
# lap = t.laptop
# t.info()
# lap = v.laptop
# v.info()

# ****************************************************
#                   2023 год
# ****************************************************

# Написать программу разведения котов и кошек, с предполагаемым количеством котят.
# import random
#
# 
# class Cat:
#
#     def __init__(self, name: str, age: int, get: str):
#         if not isinstance(name, str):
#             raise ValueError("Имя у кошки должно быть строкой")
#         if not isinstance(age, int):
#             raise ValueError("Возраст кошки должен быть числом")
#         if not isinstance(get, str):
#             raise ValueError("Гендер у кошки должен быть строкой")
#
#         self.name = name
#         self.age = age
#         self.get = get
#
#     def get_format(self):
#         if self.kitty_age > 2:
#             sum_kits = random.randint(2, 5)
#             lst = ['Мужской', 'Женский']
#             gender = random.choice(lst)
#             print(f"У кошек родится {sum_kits} котенка, их пол будет {gender} ")
#         else:
#             raise ValueError("Возраст должен быть больше 2")
#
#     def __add__(self, other):
#         if (self.get == 'm' or self.get == 'f') and (other.get == 'm' or other.get == 'f'):
#             if self.get == other.get:
#                 raise TypeError("Одинаковый пол животного")
#             if not isinstance(other, Cat):
#                 raise ValueError("Тип данных не принадлежит к классу Cat")
#             if self.age <= 0 or other.age <= 0:
#                 raise ValueError("Возраст должен быть больше 1")
#             self.kitty_age = self.age + other.age
#             return Cat.get_format(self)
#         else:
#             raise TypeError("Пол может быть только 'm' или 'f'")
#
#
# c1 = Cat("Max", 3, 'm')
# c2 = Cat("Blue", 1, 'f')
# c3 = c1 + c2

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
        




        



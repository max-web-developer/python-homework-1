# total = int(input("введите количество квартир!: "))
# floors = int(input("введите количество этажей: "))
# apartment = int(input("номер кв вашего друга? "))
# p = (total/floors)
# if total % floors > 0 or apartment <= 0 or total < apartment:
#      print("кол-во квартир не делится на кол-во этажей!")
# if total % floors > 0 or apartment >=0 or total > apartment:
#      print('error!')
# n = apartment // (p) or (p)
# print("номер этажа вашего друга", n)

total = int(input("введите количество квартир!: "))
floors = int(input("введите количество этажей: "))
apartment = int(input("номер кв вашего друга? "))
if apartment > 12:
    print('квартира на первом этаже!')
if apartment < 12 :
    print('квартира на втором этаже!')
if apartment > 24:
    print('квартира на третьем этаже!')
if apartment > 36:
    print('квартира на 5 этаже')
if apartment > 48:
    print('квартира на 6 этаже')
if apartment > 60:
    print('квартира на 7 этаже')
if apartment > 72:
    print('квартира на 8')
if apartment > 80:
    print('квартира на 9')
if apartment > 92:
    print('квартира на 10')




from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자를 통한 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
print('oop파일')
is_on=True
# print(menu.menu[1].ingredients['coffee'])
#현재 상황에서 menu.menu를 활용하여 espresso라는 str을 추출하려면 어떡해야 하나요?
print(menu.get_items())
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까 ???  {menu.get_items()} >>>')
    if choice=='off':
        is_on=False
        print('프로그램을 종료합니다.')
    elif choice == 'report' :
        coffee_maker.report()
        print('-------')
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)








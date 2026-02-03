MENU = {
    '에스프레소' : {
        '재료' : {
            '물' : 50,
            '커피' : 18,
        },
        '가격' : 1.5,
    },
    '라떼' : {
        '재료' : {
            '물' : 200,
            '우유' : 150,
            '커피' : 24,
        },
        '가격' : 2.5,
    },
    '카푸치노' : {
        '재료' : {
            '물' : 250,
            '우유' : 100,
            '커피' : 24,
        },
        '가격' : 3.0,
    },

}
print(MENU)
resources = {
    '물' : 300,
    '우유' : 200,
    '커피' : 100,

}
profit = 0

def report() :
    print(f'물 : {resources['물']}ml \n'
          f'우유 : {resources['우유']}ml \n'
          f'커피 : {resources['커피']}g \n'
          f'돈 : {profit}$ \n')

def is_resource_enough(order_ingredients) :

    for item in order_ingredients :
        if order_ingredients[item] > resources[item] :
            print(f'죄송합니다. {item}이(가) 부족합니다.')
            return False
    return True
def process_coins():

    total = 0.0
    # quarters / dimes / nickels / pennies
    total += int(input('quarters 동전 수 >>>'))*0.25
    total += int(input('dimes 동전 수 >>>'))*0.10
    total += int(input('nickels 동전 수 >>>'))*0.05
    total += int(input('pennies 동전 수 >>>'))*0.01

    return total
def is_transaction_successful(money_received, drink_cost) :

    global profit
    change = round(money_received - drink_cost, 2)
    if change >= 0 :
        profit += drink_cost
        print(f'잔돈은 {change}다음 로직으로 진행')
        return True
    else :
        print(f'돈이 부족합니다. {money_received}를 반환합니다.')
        return False

def make_coffe(drink_name, order_ingredients) :
    for item in drink['재료']:
        resources[item] -= drink['재료'][item]

    print(f'{choice}가 완성되었습니다. ☕입 천장 다 데라')


is_on = True
while is_on:
    choice = input('어떤 음료를 드시겠습니까 ? 에스프레소 / 라떼 / 카푸치노 >>>')

    if choice == 'off':
        print('자판기가 종료되었습니다.')
        is_on = False

    elif choice == 'report':
        report()

    elif choice in ['에스프레소', '라떼' , '카푸치노'] :

        drink = MENU[choice]
        if is_resource_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink['가격']):

                make_coffe(choice,drink['재료'])

    else:
        print('오타 발생 다시 작성해라')



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
# 자판기 보유량에서 에스프레소 두 잔을 추출 했을 때 resources의 남은 물, 우유, 커피량을 딕셔너리 형태로 보여 주시오.
# 로직
# resources['물']-=MENU['에스프레소']['재료']['물']*2
# resources['커피']-=MENU['에스프레소']['재료']['커피']*2
# for key in MENU['에스프레소']['재료']:
#     resources[key]-=MENU['에스프레소']['재료']['물']*2
#
# print(resources)

# 라떼 한 잔을 뽑았을때 남는 resources를 출력 하고, 라떼 금액만큼 profit 더한 결과를 콘솔에 출력


# for stuff in MENU['라떼']['재료']:
#     resources[stuff] -= MENU['라떼']['재료'][stuff]
#
# profit += MENU['라떼']['가격']
# print(profit)
#
# resources['동전'] = profit
#
# print(resources)
# 함수 정의 영역
def report() :
    print(f'물 : {resources['물']}ml \n'
          f'우유 : {resources['우유']}ml \n'
          f'커피 : {resources['커피']}g \n'
          f'돈 : {profit}$ \n')

def is_resource_enough(order_ingredients) :
    ''' DocString : 함수/클래스/메서드가 어떤 작동을 하는지 '사람들에게' 설명하는 기능
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면 True / 아니면 False
    :param: order_ingredients
    :return: True / False
    '''
    for item in order_ingredients :
        if order_ingredients[item] > resources[item] :
            print(f'죄송합니다. {item}이(가) 부족합니다.')
            return False
    return True
def process_coins():
    '''
    동전을 입력받아 전체 금액을 반환하는 함수 call3()유형
    :return: total
    '''
    total = 0.0
    # quarters / dimes / nickels / pennies
    total += int(input('quarters 동전 수 >>>'))*0.25
    total += int(input('dimes 동전 수 >>>'))*0.10
    total += int(input('nickels 동전 수 >>>'))*0.05
    total += int(input('pennies 동전 수 >>>'))*0.01

    return total
def is_transaction_successful(money_received, drink_cost) :
    '''
    process_coins() 의 결과값과 음료 가격을 매개 변수로 받아 동전이 가격보다 높으면 true / 아니면 False를 반환하는데, 금액 부족하다고 안내해줘야 합니다. 그리고 True라면 profit에 윰료 가격만큼 추가를 해주고, 잔돈을 반환해야 합니다.
    :param money_received:
    :param drink_cost:
    :return: True/False
    '''
    global profit # 함수 내에서 전역 변수의 값을 바꾸는 것이 바람직하지 않아서 제한 걸어뒀습니다.
    change = round(money_received - drink_cost, 2)
    if change >= 0 :
        profit += drink_cost
        print(f'잔돈은 {change}다음 로직으로 진행')
        return True
    else :
        print(f'돈이 부족합니다. {money_received}를 반환합니다.')
        return False

def make_coffe(drink_name, order_ingredients) :     # call2()유형 :
    for item in drink['재료']:  # order_ingredients = drink['재료']
        resources[item] -= drink['재료'][item]
    # 커피 안내 문구
    print(f'{choice}가 완성되었습니다. ☕입 천장 다 데라')


is_on = True 
while is_on:
    choice = input('어떤 음료를 드시겠습니까 ? 에스프레소 / 라떼 / 카푸치노 >>>')
    # todo - 1 : choice가 off 라면 자판기가 종료되었습니다. 라고 출력하면서 반복 종료
    if choice == 'off':
        print('자판기가 종료되었습니다.')
        is_on = False
    # todo - 2 : choice 가 report 라면 물 : 어쩌고 커피 : 어쩌고  작성
    elif choice == 'report':
        report()
    # todo - 3 : choice가 에스프레소 / 라떼 / 카푸치노에 해당한다면 실행문으로 다음 단계 로직 이라고 콘솔에 출력할 수 있도록 코드를 작성
    elif choice in ['에스프레소', '라떼' , '카푸치노'] :

        drink = MENU[choice]
        if is_resource_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink['가격']):

                make_coffe(choice,drink['재료'])
    # todo - 4 : 오타 발생 시에 잘못 입렵하셨습니다. 를 콘솔에 출력하고 다음 반복문
    else:
        print('오타 발생 다시 작성해라')



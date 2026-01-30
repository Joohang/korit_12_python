'''
1. if 문
    - if 문은 조건이 참일 때만 해당 블록의 코드 실행
2. if-else 문
    - if 문은 조건이 True일 때 / False일때는 else 부분 실행
3. if-elif-else 문

'''
from traceback import print_tb

from ch00_starting.main import age

# age=int(input('나이를 입력하세요 >>> '))
# if age > 20:
#     print('성인입니다.')
# elif 20 >= age > 13:
#     print('청소년입니다.')
# else:
#     print('어린이입니다.')
'''
if 조건문의 전체 형식 : 

if 조건식1 : 
    실행문1
(elif 조건식2 :)
    (실행문2)
(elif 조건식3 :)
    (실행문3)
(else:)
    (실행문4)

Nested - if 문도 쓸 수 있습니다.
'''
age = 21
has_ticket = True       # boolean 자료형 처음 변수 순언해봤습니다.
print(type(has_ticket)) # <class 'bool'>
if age>=19:
    if has_ticket:
        print('영화관 입장 가능')
    else:
        print('티켓 구매')
else:
    print(' ')

'''
비교 연산자

논리연산자
    1) and " &&
    2) or : ||
    3) not : !와 같은. 근데 python에 not=이런건 없고 !=는 있어서 혼란스러울 때가 있음

'''
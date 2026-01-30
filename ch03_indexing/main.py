str_example = 'Hello Python!'
print(str_example[0])
print(str_example[1])
print(str_example[2])
print(str_example[3])
print(str_example[4])
print(str_example[5])
print(str_example[6])

print(len(str_example))     # 결과값 : 14
'''
len() 반복 가능 객체의 전체 인덱스 값을 return하는 함수
'''

# 일반 for문으로 Hello, Python!을 한 줄로 출력하시오.
for i in range(len(str_example)):
    print(str_example[i], end=' ')
print()
# 향상된 for문
for letter in str_example:
    print(letter, end=' ')

'''
마이너스 인덱스 : 문자열의 뒤에서부터 부여하는 번호. 맨 마지막 데이터의 인덱스 넘버는 -1

문자열 슬라이싱(slice) : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용하는 방법
    추출하고자 하는 단어나 문장의 시작 인덱스와 종료 인덱스를 통해 그 사이 문자들을 추출하는 것이 가능함.
    
형식 : 
변수명[ 시작인덱스 : 종료인덱스 : 증감값 ]
시작인덱스 : 생략하면 처음부터 추출
종료인덱스 : 생략하면 끝까지 추출
증감값 : 생락하면 1씩 증가함 (인덱스 넘버가 0부터 1씩 증가한다는 의미입니다.)
'''

print(str_example[:3:])
# 시작지점(0)번지 부터 뒤에서 3번째 인덱스 미만까지만 출력한다는 의미

print(str_example[-1])
print(str_example[-2])
print(str_example[-3])
print(str_example[-4])
print(str_example[-5])
print(str_example[-6])

'''
근데 잘 생각해보면 range(시작값 , 종료값 , 증감값)이랑
변수명[시작인덱스:종료인덱스:증감값]이랑 똑같아 보입니다. 근데 왜 하나는 :이고 나른 하나는 ,일까요?

기본 예제 
네 자리 숫자를 입력 받아 그자리의 맨 마지막 숫자를 출력하시오.

실행예
네 자리 숫자를 입력하세요 >>>> 
맨 마지막 숫자는
맨 마지막 숫자는 6이며 짝수
'''

number = input( "네 자리 숫자를 입력하세요 >>>> ")

last_number = number[-1]
print(f'맨마지막 숫자는 {last_number}')

# 조건문 작성 시
if int(last_number) % 2 == 0:           # 조건문 시점에는 % 연산해야하니까 형변환
    print(f'맨 마지막 숫자는 {last_number}이며 짝수입니다.')
else :
    print(f'맨 마지막 숫자는 {last_number}이며 훌수입니다.')

'''
python 삼항 연산자
if - else 구조룰 한줄로 줄여서 씁니다.
'''

result = '짝수' if int(last_number)%2==0 else '훌수'

print(f'맨 마지막 숫자는 {last_number}이며 {result}입니다.')

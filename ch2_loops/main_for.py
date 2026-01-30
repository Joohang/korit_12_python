'''
for 반복문 :
원래 python에서의 default for문의 경우 enhanced for가 기분입니다.
근데 저희는 index를 다루는 것부터 시작했었기 때문에 걔를 기준으로 먼저
강의합니다.

이때 중요한 것이 range() 함수
'''

# 1~10 까지 출력하는 for문
for i in range(10):
    print(i+1)
'''
이상에서 중요한 것은 i가 0부터 시작한다는 점입니다.
range() : 몇 번 반복할 것인가를 지정하는 함수. -> 특히 for문과 연계되어
함께 쓰이는 편입니다.

range() 함수의 응용
range((시작값) , 한계값, (증감값))

시작값 : 생략가능, 생략하면 0부터 시작
한계값 : 명시하지 않으면 끝까지 진행
증감값 : 생략가능, 생략할 경우에 1씩 증가
'''
for i in range(1,11,2):  # 먄약 홀수만 출력하고 싶다면 증감값을 2로
    print(i, end=' / ')  # 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 /
print()
print(i)        # 결곽값 : 10
'''
Java에서는 for(int i = 0 ...) 어쩌고 한 부분 있을 때
System.out.println(i); 하면 오류남
while에서와 마찬가지로 지역 변수의 범위가 다르다는 점을 알 수 있음.

이상까지 학습했을 때 시작값 / 한계값 / 증감값을 정의하게 되는 rage() 함수가 
필수적으로 여거집니다.

하지만 default 형태의 python for-loop의 경우의 형식인 : 
for 변수명(자유롭게 가능) in iterable(반복가능객체) 입니다.
'''
nums = [ 1,2,3,4,5]
for i in nums:
    print(i, end=' / ')

if 5 in nums:
    print('5가 num 리스트 내에 있습니다.')
else:
    print('5가 num 리스트 내에 없습니다.')
'''
그러면 Java를 배우는 저희는 익숙하지 않지만 in이라는 애가 생각보다 엄청
중요합니다. in이 적용된 무언가의 결과값의 자료형은 무엇일까요??
-> True / False가 나오는 '연산자'
A in B 라고 했을때 A라는 요소가 B라는 반복가능 객체 내에 존재하는지를
True / False로 뽑아주게 됩니다.
'''
print(5 in nums) # 결과값 : True
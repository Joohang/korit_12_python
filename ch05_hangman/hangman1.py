import random
numbers = [ 1,2,3,4,5 ]
chosen_number = random.choice(numbers)
# random이라는 객체같은 것에 choice라는 메서드가 있고, 내부에
# list 자료형을 넣으면 하나를 뽑아서 변수에 저장하는갑다
print(chosen_number)

word_list= ['apple' , 'banana','camel']
# todo -1 : word_list에서 하나의 단어를 임의로 선택하도록 random 모율을 사용하고, 하댕
# 단어를 chosen_word에 담으시오

# todo -2 : 사용자에게 알파벳 하나를 추측해서 입력하라고 요청하고,
# 이를 guess 변수에 담으시오. 대문자로 시작하는 경우를 방지하기 위해. lower함수를 적용하시오

# todo -3 : guess에서 입력한 문자 하나가 chosen_word의 str 문자열 중에
# 하나의 문자와 일치하는지를 확인할 수 있도록 반복 - 조건문을 작성하고
# 맞으면 정담 / 틀리면 오답

choosen_word = random.choice(word_list)

print(choosen_word)
guess =input('알파벳을 입력하세요 >>> ').lower()


for letter in choosen_word:
    if guess == letter :
        print(f'{guess} 정답')
    else :
        print('오답')

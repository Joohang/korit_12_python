import random
from hangman_arts import * # hangman_arts 파일의 전체 데이터를 가져오겠다는 의미
from hangman_word_list import word_list
# hangman_word_list 파일 내에서 word_list 변수만 가지고 오겠다는 의미
from hangman6 import *

# 이상과 같이 작성한 것을 기준으로 hangman을 완성하시오
print(logo)
chosen_word = random.choice(word_list)


print(f'테스트 단어 : {chosen_word}')

display = []

for _ in range(len(chosen_word)):
    display.append('_')
print(' '.join(display))

lives = 6

end_of_game = False

print(logo)
while not end_of_game :
    print(stages[lives])
    guess = input('알파벳을 입력하세요 >>> ').lower()
    for _ in range(len(chosen_word)):

        if guess == chosen_word[_]:
            display[_] = guess
            print(' '.join(display))

    if guess not in chosen_word :
        lives -= 1
        print(f'기회가 {lives}번 남았습니다')


        if lives == 0 :
            print('game over')
            end_of_game = True
            print(stages[lives])
            print(f'정답은 {chosen_word}입니다.')


    if '_' not in display :
        print(f'{chosen_word} 정답입니다 ~~!!' )
        end_of_game = True

    print(' '.join(display))
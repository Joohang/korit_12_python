import random
import hangman_arts
import hangman_word_list

# import 다음에 파일명을 썼다는 것에 주목. 이 파일 하나를 파이썬에서는 module(모듈)이라고 합니다.

# 외부의 hangman_word_list에 있는 word_list 변수를 참조해서 chosen_word를 만들 필요가 있습니다.


# 위에가 힌트. 그러면 chosen_word를 불러올 수 있도록
chosen_word = random.choice(hangman_word_list.word_list)
print(f'테스트 단어 : {chosen_word}')
# 나머지 부분을 잘 복사한 다음에 오류 생기는 부분을 수정

display = []

for _ in range(len(chosen_word)):
    display.append('_')
print(' '.join(display))

lives = 6

end_of_game = False

print(hangman_arts.logo)
while not end_of_game :
    print(hangman_arts.stages[lives])
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
            print(hangman_arts.stages[lives])
            print(f'정답은 {chosen_word}입니다.')


    if '_' not in display :
        print(f'{chosen_word} 정답입니다 ~~!!' )
        end_of_game = True

    print(' '.join(display))
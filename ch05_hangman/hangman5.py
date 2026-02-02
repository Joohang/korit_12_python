# ascii art generator를 통해  hangman logo

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = '''
          _____                    _____                    _____                    _____                            _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                          /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\____\                /::\    \                        /::\____\                /::\    \                /::\____\        
       /:::/    /               /::::\    \              /::::|   |               /::::\    \                      /::::|   |               /::::\    \              /::::|   |        
      /:::/    /               /::::::\    \            /:::::|   |              /::::::\    \                    /:::::|   |              /::::::\    \            /:::::|   |        
     /:::/    /               /:::/\:::\    \          /::::::|   |             /:::/\:::\    \                  /::::::|   |             /:::/\:::\    \          /::::::|   |        
    /:::/____/               /:::/__\:::\    \        /:::/|::|   |            /:::/  \:::\    \                /:::/|::|   |            /:::/__\:::\    \        /:::/|::|   |        
   /::::\    \              /::::\   \:::\    \      /:::/ |::|   |           /:::/    \:::\    \              /:::/ |::|   |           /::::\   \:::\    \      /:::/ |::|   |        
  /::::::\    \   _____    /::::::\   \:::\    \    /:::/  |::|   | _____    /:::/    / \:::\    \            /:::/  |::|___|______    /::::::\   \:::\    \    /:::/  |::|   | _____  
 /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\          /:::/   |::::::::\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \ 
/:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\/:::/____/  ___\:::|    |        /:::/    |:::::::::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\
\::/    \:::\  /:::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /\:::\    \ /\  /:::|____|        \::/    / ~~~~~/:::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /
 \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    /  \:::\    /::\ \::/    /          \/____/      /:::/    /  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    / 
          \::::::/    /            \::::::/    /           |::|/:::/    /    \:::\   \:::\ \/____/                       /:::/    /            \::::::/    /           |::|/:::/    /  
           \::::/    /              \::::/    /            |::::::/    /      \:::\   \:::\____\                        /:::/    /              \::::/    /            |::::::/    /   
           /:::/    /               /:::/    /             |:::::/    /        \:::\  /:::/    /                       /:::/    /               /:::/    /             |:::::/    /    
          /:::/    /               /:::/    /              |::::/    /          \:::\/:::/    /                       /:::/    /               /:::/    /              |::::/    /     
         /:::/    /               /:::/    /               /:::/    /            \::::::/    /                       /:::/    /               /:::/    /               /:::/    /      
        /:::/    /               /:::/    /               /:::/    /              \::::/    /                       /:::/    /               /:::/    /               /:::/    /       
        \::/    /                \::/    /                \::/    /                \::/____/                        \::/    /                \::/    /                \::/    /        
         \/____/                  \/____/                  \/____/                                                   \/____/                  \/____/                  \/____/         
                                                                                                                                                                                       
'''
word_list = [
    'apple', 'banana', 'camel', 'dragon', 'elephant', 'flower', 'guitar', 'house', 'island', 'jungle',
    'kite', 'lemon', 'mountain', 'notebook', 'ocean', 'piano', 'queen', 'river', 'stone', 'tiger',
    'umbrella', 'violin', 'whale', 'xylophone', 'yacht', 'zebra', 'airplane', 'bicycle', 'camera', 'desert',
    'engine', 'forest', 'garden', 'hammer', 'irony', 'jacket', 'keyboard', 'laptop', 'mirror', 'needle',
    'orange', 'planet', 'quartz', 'rocket', 'silver', 'tunnel', 'unique', 'valley', 'window', 'yellow',
    'ability', 'balance', 'calendar', 'danger', 'effort', 'factor', 'galaxy', 'habit', 'impact', 'jacket',
    'knight', 'labor', 'machine', 'native', 'object', 'package', 'quality', 'rabbit', 'safety', 'tablet',
    'update', 'vessel', 'wealth', 'yield', 'anchor', 'bottle', 'castle', 'dinner', 'energy', 'finger',
    'glory', 'health', 'inside', 'junior', 'kitchen', 'ladder', 'memory', 'number', 'office', 'pocket',
    'record', 'season', 'ticket', 'urgent', 'visual', 'winter', 'active', 'bright', 'center', 'direct',
    'effect', 'future', 'global', 'height', 'island', 'journey', 'kindly', 'letter', 'market', 'nature',
    'online', 'player', 'report', 'school', 'target', 'useful', 'voice', 'worker', 'yield', 'action',
    'beauty', 'common', 'degree', 'expert', 'ground', 'honest', 'income', 'junior', 'legend', 'modern',
    'notice', 'output', 'period', 'reason', 'simple', 'theory', 'upload', 'volume', 'winner', 'accept',
    'beyond', 'charge', 'design', 'escape', 'format', 'guilt', 'handle', 'import', 'judge', 'knight',
    'liquid', 'manage', 'notion', 'option', 'permit', 'relief', 'select', 'travel', 'unique', 'verify',
    'weight', 'across', 'border', 'client', 'detail', 'entire', 'figure', 'gather', 'happen', 'ignore',
    'junior', 'knowledge', 'locate', 'method', 'nearly', 'obtain', 'proper', 'rely', 'source', 'though',
    'unless', 'victim', 'within', 'yearly', 'access', 'bottom', 'column', 'device', 'extent', 'follow',
    'growth', 'health', 'intend', 'justice', 'killer', 'launch', 'matter', 'narrow', 'origin', 'policy',
    'repair', 'system', 'toward', 'unable', 'vastly', 'weekly', 'against', 'budget', 'course', 'driver',
    'export', 'famous', 'guilty', 'highly', 'indeed', 'joined', 'killed', 'lesson', 'mostly', 'nation',
    'others', 'prison', 'rather', 'speech', 'thanks', 'useful', 'values', 'wanted', 'youth', 'agency',
    'button', 'choice', 'during', 'easily', 'finish', 'guilty', 'honest', 'island', 'judgment', 'knight',
    'living', 'mental', 'nearby', 'others', 'public', 'result', 'silent', 'theory', 'united', 'voters',
    'winter', 'writer', 'yields', 'advice', 'branch', 'caught', 'damage', 'editor', 'failed', 'gentle',
    'hidden', 'impact', 'joined', 'killed', 'living', 'mainly', 'notice', 'object', 'palace', 'quiet',
    'rhythm', 'senior', 'timing', 'urgent', 'volume', 'wealth', 'yearly', 'around', 'broken', 'called',
    'decide', 'enough', 'faster', 'groups', 'health', 'inside', 'judged', 'known', 'likely', 'making',
    'needed', 'office', 'player', 'really', 'simple', 'thanks', 'unless', 'voices', 'within', 'yellow',
    'almost', 'became', 'camera', 'degree', 'events', 'fields', 'ground', 'higher', 'income', 'jumped',
    'keep', 'longer', 'moving', 'number', 'others', 'points', 'raised', 'second', 'things', 'useful',
    'values', 'wanted', 'winter', 'amount', 'behind', 'center', 'direct', 'expect', 'friend', 'garden',
    'having', 'itself', 'justly', 'kindly', 'lights', 'mostly', 'nearly', 'opened', 'passed', 'reason',
    'single', 'though', 'under', 'vision', 'worker', 'across', 'better', 'church', 'double', 'either',
    'father', 'giving', 'health', 'island', 'joined', 'knows', 'listen', 'middle', 'night', 'others',
    'please', 'return', 'school', 'toward', 'united', 'voices', 'within', 'yearly', 'active', 'beyond',
    'common', 'during', 'entire', 'figure', 'gather', 'higher', 'inside', 'jungle', 'kindly', 'longer',
    'memory', 'nature', 'others', 'period', 'public', 'rather', 'sounds', 'things', 'urgent', 'values',
    'writer', 'yellow', 'animal', 'bright', 'closed', 'dreams', 'escape', 'forest', 'ground', 'houses',
    'images', 'junior', 'knives', 'lights', 'moment', 'number', 'object', 'pieces', 'really', 'simple',
    'thanks', 'united', 'visual', 'wanted', 'winter', 'across', 'broken', 'choose', 'direct', 'engine'
]
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
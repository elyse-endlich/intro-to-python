from random import randrange

# numbers, letters, and special characters
letters = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"


randrange(27)

lst = (letters, caps, numbers)

password = ""

for _ in range(8):
    temp = lst[randrange(len(lst))]
    password = password + temp[randrange(len(temp))]
print(password)

# four random words
nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology', 'funeral', 'engine', 'isolation',
         'perception', 'hat', 'mountain', 'session', 'case', 'legislature', 'consent', 'spread', 'shot', 'direction',
         'data', 'tragedy', 'illness', 'serving', 'mess', 'resistance', 'basis', 'kitchen', 'mine', 'temple', 'mass',
         'dot', 'final', 'chair', 'picture', 'wish', 'transfer', 'profession', 'suggestion', 'purse', 'rabbit',
         'disaster', 'evil', 'shorts', 'tip', 'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition',
         'origin', 'lesson', 'Bible', 'act', 'constitution', 'standard', 'status', 'burden', 'language', 'voice',
         'border', 'statement', 'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler', 'merit', 'puzzle',
         'poll', 'wind', 'shelter', 'limit', 'talent']
verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim', 'fill', 'present', 'complain', 'offer',
         'provoke', 'yield', 'shock', 'purchase', 'seek', 'operate', 'persist', 'inspire', 'conclude', 'transform',
         'add', 'boast', 'gather', 'manage', 'escape', 'handle', 'transfer', 'tune', 'born', 'decrease', 'impose',
         'adopt', 'suppose', 'sell', 'disappear', 'join', 'rock', 'appreciate', 'express', 'finish', 'modify', 'keep',
         'invest', 'weaken', 'speed', 'discuss', 'facilitate', 'question', 'date', 'coordinate', 'repeat', 'relate',
         'advise', 'arrest', 'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend', 'owe', 'wait', 'unfold', 'back',
         'waste', 'delay', 'store', 'balance', 'compete', 'bake', 'employ', 'dip', 'frown', 'insert']
adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical', 'extreme', 'cruel', 'expensive',
        'comfortable', 'steady', 'necessary', 'isolated', 'deep', 'bad', 'free', 'voluntary', 'informal', 'loud', 'key',
        'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 'OK', 'gray', 'little', 'religious', 'municipal',
        'just', 'psychological', 'essential', 'perfect', 'intense', 'blue', 'following', 'Asian', 'shared', 'rare',
        'developmental', 'uncomfortable', 'interesting', 'environmental', 'amazing', 'unhappy', 'horrible',
        'philosophical', 'American']

# Make a four word password by combining words from the list of nouns, verbs and adjs
print(len(nouns))  # 75
print(len(verbs))  # 75
print(len(adjs))  # 50


print(
    adjs[randrange(50)] + adjs[randrange(50)] + nouns[randrange(75)] + verbs[randrange(75)])

lst = (nouns, verbs, adjs)

password = ""
temp = ""

for _ in range(4):
    temp = lst[randrange(len(lst))]
    password = password + temp[randrange(len(temp))]
print(password)

# leetspeak password
word = "pool"
word = word.replace('o', 'e')
# print(word)
word = word.capitalize()
# print(word)

###

nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology', 'funeral', 'engine', 'isolation',
         'perception', 'hat', 'mountain', 'session', 'case', 'legislature', 'consent', 'spread', 'shot', 'direction',
         'data', 'tragedy', 'illness', 'serving', 'mess', 'resistance', 'basis', 'kitchen', 'mine', 'temple', 'mass',
         'dot', 'final', 'chair', 'picture', 'wish', 'transfer', 'profession', 'suggestion', 'purse', 'rabbit',
         'disaster', 'evil', 'shorts', 'tip', 'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition',
         'origin', 'lesson', 'Bible', 'act', 'constitution', 'standard', 'status', 'burden', 'language', 'voice',
         'border', 'statement', 'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler', 'merit', 'puzzle',
         'poll', 'wind', 'shelter', 'limit', 'talent']
verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim', 'fill', 'present', 'complain', 'offer',
         'provoke', 'yield', 'shock', 'purchase', 'seek', 'operate', 'persist', 'inspire', 'conclude', 'transform',
         'add', 'boast', 'gather', 'manage', 'escape', 'handle', 'transfer', 'tune', 'born', 'decrease', 'impose',
         'adopt', 'suppose', 'sell', 'disappear', 'join', 'rock', 'appreciate', 'express', 'finish', 'modify', 'keep',
         'invest', 'weaken', 'speed', 'discuss', 'facilitate', 'question', 'date', 'coordinate', 'repeat', 'relate',
         'advise', 'arrest', 'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend', 'owe', 'wait', 'unfold', 'back',
         'waste', 'delay', 'store', 'balance', 'compete', 'bake', 'employ', 'dip', 'frown', 'insert']
adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical', 'extreme', 'cruel', 'expensive',
        'comfortable', 'steady', 'necessary', 'isolated', 'deep', 'bad', 'free', 'voluntary', 'informal', 'loud', 'key',
        'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 'OK', 'gray', 'little', 'religious', 'municipal',
        'just', 'psychological', 'essential', 'perfect', 'intense', 'blue', 'following', 'Asian', 'shared', 'rare',
        'developmental', 'uncomfortable', 'interesting', 'environmental', 'amazing', 'unhappy', 'horrible',
        'philosophical', 'American']

# Make a four word password by combining words from the list of nouns, verbs and adjs
# print(len(nouns)) # 75
# print(len(verbs)) # 75
# print(len(adjs)) # 50

lst = (nouns, verbs, adjs)

password = ""
temp1 = ""
temp2 = ""

for _ in range(4):
    temp1 = lst[randrange(len(lst))]
    temp2 = temp1[randrange(len(temp1))]
    password = password + temp2.capitalize()
if "i" in password:
    password = password.replace('i', '1')
if "e" in password:
    password = password.replace('e', '3')
if "o" in password:
    password = password.replace('o', '0')
if "B" in password:
    password = password.replace('B', '8')
if "S" in password:
    password = password.replace('S', '$')
if "a" in password:
    password = password.replace('a', '@')
print(password)

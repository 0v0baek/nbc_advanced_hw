# 문자열 메소드


# count : 문자열 내에 특정 문자가 몇 개나 있는지 세줌
jihyeon = 'I am happy'
count = jihyeon.count(' ')
print(f'count : {count}')

# find : 특정 문자열이 처음 나오는 위치를 찾아줌. 없을 경우 -1 return
jihyeon = 'I am happy'
position = jihyeon.find('happy')
print(f'find : {position}')

# index : 특정 문자열이 처음 나오는 위치를 찾아줌. 없을 경우 ValueError
jihyeon = 'I am happy'
try:
    position = jihyeon.index('are')
    print(f'index : {position}')
except ValueError:
    print('찾는 문자열이 없습니다!')

# join : 특정 문자열을 기준으로 다른 문자열을 합쳐줌
jihyeon = ['i','am','happy']
jihyeon_join = ' '.join(jihyeon)
print(f'join : {jihyeon_join}')

# upper / lower : 문자열 내의 모든 문자를 대문자/소문자로 바꿔줌
jihyeon = 'I am happy'
upper_jihyeon = jihyeon.upper()
print(f'upper : {upper_jihyeon}')

lower_jihyeon = upper_jihyeon.lower()
print(f'lower : {lower_jihyeon}')

# replace : 특정 문자열을 다른 문자열로 바꿔줌
jihyeon = 'I am happy'
replace_jihyeon = jihyeon.replace('happy', 'sad')
print(f'replace : {replace_jihyeon}')

# split : 문자열을 특정 문자를 기준으로 나눠줌
jihyeon = 'I am happy'
list_jihyeon = jihyeon.split(' ')
print(f'split : {list_jihyeon}')

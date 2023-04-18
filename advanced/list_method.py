# 리스트 메소드


# len : 리스트의 길이 반환
jihyeon = ['i','am','happy']
print(f'len : {len(jihyeon)}')

# del : 리스트에서 특정 요소를 삭제
jihyeon = ['i','am','happy']
del jihyeon[2]
print(f'del : {jihyeon}')

# append : 리스트에 새로운 요소를 추가함(리스트 맨 뒤)
jihyeon = ['i','am','happy']
jihyeon.append('^^')
print(f'append : {jihyeon}')

# sort : 리스트를 오름차순으로 정렬
jihyeon = [2, 3, 1, 5, 4]
jihyeon.sort()
print(f'sort : {jihyeon}')

# reverse : 리스트를 반대로 뒤집음
jihyeon = [1, 2, 3, 4, 5]
jihyeon.reverse()
print(f'reverse : {jihyeon}')

# index : 리스트에서 특정 요소의 인덱스를 반환
jihyeon = ['i','am','happy']
print('index :', jihyeon.index('i'))

# insert : 리스트의 특정 위치에 요소 삽입
jihyeon = ['i','am','happy']
jihyeon.insert(2, 'not')
print(f'insert : {jihyeon}')

# remove : 리스트에서 특정 요소 제거
jihyeon = ['i','am','happy']
jihyeon.remove('happy')
print(f'remove : {jihyeon}')

# pop : 리스트에서 마지막 요소를 빼낸 뒤 그 요소를 삭제
jihyeon = ['i','am','happy']
jihyeon.pop(2)
print(f'pop : {jihyeon}')

# count : 리스트에서 특정 요소의 개수를 셈
jihyeon = ['i','am','happy']
count = jihyeon.count('i')

# extend : 리스트를 확장해 새로운 요소들을 추가
jihyeon = ['i','am','happy']
jihyeon.extend(['you','are','happy'])
print(f'extend : {jihyeon}')

# += : extend와 비슷한 기능
jihyeon = ['i','am','happy']
jihyeon += ['you','are','happy']
print(f'+= : {jihyeon}')
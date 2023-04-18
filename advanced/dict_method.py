# 딕셔너리 메소드


# 딕셔너리 초기화
empty_dict = {}
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
print(f'딕셔너리 초기화 : {jihyeon}')

# 딕셔너리 쌍 추가
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
jihyeon['four'] = 4
print(f'딕셔너리 쌍 추가 : {jihyeon}')

# del : 딕셔너리에서 특정 요소 삭제
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
del jihyeon['one']
print(f'del : {jihyeon}')

# 딕셔너리에서 특정 key의 value를 얻는 방법
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
print(jihyeon['one'])

# keys : 딕셔너리의 모든 key값을 리스트로 만들기
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
key_list = list(jihyeon.keys())
print(f'keys : {key_list}')

# values : 딕셔너리의 모든 value를 리스트로 만들기
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
value_list = list(jihyeon.values())
print(f'values : {value_list}')

# items : 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
items = jihyeon.items()
print(f'items : {items}')

# clear : 딕셔너리의 모든 요소를 삭제
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
jihyeon.clear()
print(f'clear : {jihyeon}')

# get : 딕셔너리에 지정한 키에 대응하는 value 반환. 없을 경우 None return
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
one = jihyeon.get('one')
four = jihyeon.get('four')
print(f'get : {one}, {four}')

# in : 해당 키가 딕셔너리 안에 있는지 확인
jihyeon = {'one' : 1, 'two' : 2, 'three' : 3}
print('one' in jihyeon)
print('four' in jihyeon)
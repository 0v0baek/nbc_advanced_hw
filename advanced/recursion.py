# 풀어써서 이해하려고 해보기
def pascal(n):
    if n <= 2:
        return [1]
    if 3 <= n <= 4:
        return [1] + [n-1]*(n-2) + [1]
    if 5 <= n <= 6:
        return [1] + [n-1] + [pascal(n-1)[1]+pascal(n-1)[2]]*(n-4) + [n-1] +[1]
    ...


# 구조를 한번 짜보기
def pascal(n):
    if n <= 2:
        return [1] * 2
    else:
        return [1] + [pascal(n-1)[0] + pascal(n-1)[1]] + ... + [pascal(n-1)[n-1] + pascal(n-1)[n]] + [1]

# for문으로 돌려 써보기
# list index out of range (이전 줄의 pascal은 n-1이 마지막 이라는 것을 유의...)
def pascal(n):
    if n <= 2:
        return [1] * 2
    else:
        pascal_list = []
        for i in range(1, n):
            pascal_list.append(pascal(n-1)[i-1] + pascal(n-1)[i])
        return [1] + pascal_list + [1]

'''
여기서부터 작동 잘되는 코드
'''

# 작동은 잘 되는데 시간이 너무 오래 걸림
def pascal(n):
    if n <= 2:
        return [1] * 2
    else:
        pascal_list = []
        for i in range(2, n):
            pascal_list.append(pascal(n-1)[i-2] + pascal(n-1)[i-1]) 
        return [1] + pascal_list + [1]

# 위와 시간은 같은데 한 줄로 줄인 코드
def pascal(n):
    if n == 1:
        return [1]
    return [1] + [pascal(n-1)[i-2] + pascal(n-1)[i-1] for i in range(2,n)] + [1]

# 딕셔너리에 파스칼 값을 저장해서 매번 연산하지 않아도 되게 속도를 줄여줌
def pascal(n):
    pascal_dict = {}
    for i in range(1, n+1):
        # 파스칼 줄의 길이와 맞게 리스트 원소 갯수를 생성(1로 통일)
        pascals = [1] * i
        for j in range(1, i-1):
            # 파스칼 삼각형의 각 행의 값은 자기 위의 두 숫자를 더한 값이다
            pascals[j] = pascal_dict[i-1][j-1] + pascal_dict[i-1][j]
        # for문으로 변경되어 나온 pascals를 pascal_dict의 i번째에 저장해줌
        pascal_dict[i] = pascals
    # 원하는 행을 출력
    return pascal_dict[n]


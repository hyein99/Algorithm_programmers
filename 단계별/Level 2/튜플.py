def solution(s):
    # step 1.문자열 s를 이중리스트로 재구성
    slist = s[2:-2].split('},{')
    slist.sort(key=lambda x: len(x))
    arr = []
    for st in slist:
        arr.append(set(map(int, st.split(','))))

    # step 2. result에 하나씩 추가
    result = [list(arr[0])[0]]
    for i in range(1, len(arr)):
        result.append(list(arr[i] - arr[i - 1])[0])

    return result

def solution(m, n, board):
    # 블록을 삭제할 수 있는지 판단하는 함수
    def can_delete(x, y):
        # 조건1) 4개블록이 존재할 경우
        #       [x][y+1]과 [x+1][y]는 앞 조건문에서 확인했으므로 [x+1][y+1]만 확인
        # 조건2) 4개 블록이 같을 경우
        if y + 1 < len(blist[x+1]):
            if blist[x][y] == blist[x][y + 1] == blist[x + 1][y] == blist[x + 1][y + 1]:
                return True
        return False

    # step 1) 사용할 변수 선언
    cnt = 0  # 삭제한 블록 수
    blist = [[''] * m for _ in range(n)]  # board의 원소를 리스트로 변환(m,n 반대)
    for i in range(m):
        for j in range(n):
            # blist[i][j] = i번째 세로줄 밑에서 j번째 있는 캐릭터
            blist[j][m - i - 1] = board[i][j]  # 거꾸로(리스트 정렬 사용 위해)

    while True:
        # step 2) 삭제할 블록 탐색, 삭제할 블록 set에 추가
        deleted = set()
        for i in range(len(blist)-1):        # 마지막 행또는 열은 사각형 형성x
            for j in range(len(blist[i])-1):
                if can_delete(i, j):
                    # 4개 블록 set에 add
                    deleted = deleted | {(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)}

        # step 4) 2,3 반복, 삭제할 블록 set이 empty이면 종료
        if not deleted:
            break

        # step 3) 정렬 후 삭제
        # 제일 위에 있는 블록(blist[i][j]에서 j가 큰 블록)부터 삭제
        # cnt(삭제한 블록 개수) 추가
        deleted = list(deleted)
        deleted.sort(key=lambda x: (-x[1], x[0]))
        cnt += len(deleted)
        for dx, dy in deleted:
            del blist[dx][dy]

    return cnt


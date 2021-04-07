from collections import defaultdict

def solution(genres, plays):
    # step 1) dict 2개 생성
    # genre_dict: key(genre), value(재생횟수 합)
    # play_dict: key(genre), value(id, 재생횟수)
    genre_dict = defaultdict(int)
    play_dict = defaultdict(list)
    for i in range(len(genres)):
        genre_dict[genres[i]] += plays[i]
        play_dict[genres[i]].append((plays[i], i))

    # step 2) genre 정렬
    sorted_genre_dict = sorted(genre_dict.items(), key=lambda x: -x[1])

    # step 3) genre별 노래 추가
    result = []
    for genre in sorted_genre_dict:
        if len(play_dict[genre[0]]) == 1:  # 장르에 속한 곡이 하나일 경우
            result.append(play_dict[genre[0]][0][1])
        else:
            play_dict[genre[0]].sort(key=lambda x: (-x[0], x[1]))
            for i in range(2):
                result.append(play_dict[genre[0]][i][1])

    return result
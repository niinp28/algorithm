# 영단어 암기는 괴로워
# 문자열 연습하기 위함
N, M = map(int, input().split())
word_dict = {}

for _ in range(N):
    word = input()
    if len(word) >= M: # 단어의 길이가 M보다 큰 것만!
        if word in word_dict: # 이미 있으면 숫자 증가
            word_dict[word] += 1
        else: # 없으면 새로 등록
            word_dict[word] = 1

# 빈도순, 길이 긴 순, 알파벳순
ordered_word = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in ordered_word:
    print(word[0])
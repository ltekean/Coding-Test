# 1. 단어를 먼저 띄어쓰기 기준으로 나누기
# 2. 나눈 단어들을 인덱스에 넣기
# 3. 스택을 사용해 마지막 단어부터 빼내서 놓기

n = int(input())
for i in range(n):
	n_list = list(input().split()) # 띄어쓰기 기준으로 나누기
	n_list = n_list[::-1] # 나눈 단어들을 인덱스에 넣기
	s = ' '.join(n_list) # n_list에 있는 단어들을 띄어쓰기로 다시 합치기
	print("Case #%d: %s" %(i+1, s))
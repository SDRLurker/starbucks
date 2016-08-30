words = []

for N in range(int(input())):
	words.append(input())
words.sort()

for Q in range(int(input())):
	word = input()
	rank = words.index(word) + 1
	score = 0
	for c in word:
		score += ord(c) - ord('A') + 1
	score *= rank
	print(score)

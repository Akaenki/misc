import random
import matplotlib.pyplot as plt

def is_limited():
	if random.random() < 0.35:
		return True
	return False

def is_ssr(count):
	bonus = (count - 50) * 0.02 if count > 50 else 0
	if random.random() < (0.02 + bonus):
		return True
	return False
	
def draw():
	count_total = count_cur = 0
	while True:
		count_total += 1
		count_cur += 1
		ssr = is_ssr(count_cur) 
		if ssr and is_limited():
			return count_total
		elif ssr:
			count_cur = 0


if __name__ == '__main__':
	total = 100000
	counts = []
	a = []
	for i in range(total):
		counts.append(draw())
	african = len([i for i in counts if i >= 300])/total
	print("三百抽没限定的非洲人概率", african)
	plt.hist(counts, bins=range(0,500,50))
	plt.show()
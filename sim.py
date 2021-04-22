import random
import matplotlib.pyplot as plt

def get_sim_result():
	# 33非限定 + w五倍权重下的普通6星歪率
	psngr_rate = 1./38 * .3
	w_rate = 5./38 * .3
	rand = random.random()
	if rand < 0.35:
		return 'limited'
	elif rand < 0.35 + w_rate:
		return 'w'
	elif rand < 0.35 + w_rate + psngr_rate:
		return 'psngr'
	return 'others'

def is_ssr(count):
	bonus = (count - 50) * 0.02 if count > 50 else 0
	return random.random() < (0.02 + bonus)

def draw():
	count_total = count_cur = 0
	num_psngr = num_w = 0
	while True:
		count_total += 1
		count_cur += 1
		ssr = is_ssr(count_cur) 
		if ssr:
			result = get_sim_result()
			if result == 'limited':
				return count_total, num_psngr, num_w
			elif result == 'w':
				num_w += 1
			elif result == 'psngr':
				num_psngr += 1
			count_cur = 0


if __name__ == '__main__':
	total = 100000
	counts = []
	w = []
	psngr = []
	a = []
	for i in range(total):
		count_total, num_psngr, num_w = draw()
		counts.append(count_total)
		w.append(num_w)
		psngr.append(num_psngr)
	african = len([i for i in counts if i >= 300])/total
	print("三百抽没限定的非洲人概率", african)
	print("抽到限定前平均歪了 %f 个w和 %f 个异客" % (sum(w)/total, sum(psngr)/total))
	print("本届非洲酋长：共 %d 抽，喜迎 %d 个w和 %d 个异客" % (max(counts), w[counts.index(max(counts))], psngr[counts.index(max(counts))]))
	#plt.hist(counts, bins=range(0,500,50))
	#plt.show()
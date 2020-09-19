'''
author : Runfeng Xu, Date: 09/19-2020
'''


import random
def MOM(n,L):
	x = [random.uniform(0,L) for _ in range(n)]
	estimation = sum(x)/n*2
	mse = (estimation-L)**2
	return mse

def MLE(n,L):
	x = [random.uniform(0,L) for _ in range(n)]
	estimation = max(x)
	mse = (estimation-L)**2
	return mse

if __name__ =='__main__':
	n=100
	L=10
	E_MOM=0
	E_MLE=0
	for i in range(1000):
		E_MOM+=MOM(n,L)
		E_MLE+=MLE(n,L)
	print('MOM:',E_MOM/1000)
	print('MLE:',E_MLE/1000)

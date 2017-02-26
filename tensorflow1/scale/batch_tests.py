'''Batch tests'''

import os
import time
import sys

import numpy as np

import sgd_equivariance as se

from matplotlib import pyplot as plt


def main():
	opt = {}
	opt['equivariant_weight'] = 1e-6
	accs = []
	N_trials = 10
	
	for i in xrange(N_trials):
		acc = se.main(opt)
		accs.append(acc)
		np.save('./batch_tests/equi_{:.0e}.npy'.format(opt['equivariant_weight']), accs)
	'''
	plt.figure(1)
	names = ['1e-1.npy','1e-2.npy','1e-3.npy','0.npy',]
	equi = [1e-1, 1e-2, 1e-3, 0.]
	
	means = []
	for i, name in enumerate(['1e_n1.npy','1e_n2.npy','1e_n3.npy','0.npy',]):
		fname = './batch_tests/equi_' + name
		data = np.load(fname)
		means.append(np.mean(data))
		print data
		print('{:s}: {:04f}, {:04f}'.format(fname, means[-1], np.std(data)))
	print equi, means
	plt.plot(equi, means)
	plt.show()
	'''

if __name__ == '__main__':
	main()
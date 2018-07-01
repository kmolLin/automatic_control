# draw root-locus

import numpy as np
import matplotlib.pyplot as plt

def compute_roots(tf, gains):
	"""
	Compute the roots of the characteristic equation of the closed-loop system
	of a given transfer function for a list of gain parameters.
	Concretely, given TF = zeros/poles, and a gain value K, we solve for the 
	characteristic equation roots, that is the roots of poles + (K * zeros).
	Parameters:
	-----------
	- tf: DialogBlock mode
	- gains: list of gains
	Returns:
	--------
	- roots: numpy array containing the roots for each gain in gains.
	"""
	num, denum = tf.num, tf.den
	num_roots = len(np.roots(denum))
	roots = []

	for gain in gains:
		ch_eq = list(denum +  gain*num)
		ch_roots = np.roots(ch_eq)
		ch_roots.sort()
		roots.append(ch_roots)

	# convert final roots list into array
	roots = np.vstack(roots)

	return roots

def plot_root_locus(gains, roots):
	"""
	Plots the root locus of the closed loop system given the provided gains.
	To be filled out later - too lazy
	Parameters:
	-----------
	- gains
	- roots
	Returns:
	--------
	- fig
	- ax
	"""
	# get real and imaginary values
	real_vals = np.real(roots)
	imag_vals = np.imag(roots)

	# possible colors
	colors = ['b', 'm', 'c', 'r', 'g']

	# create figure and axis labels
	fig, ax = plt.subplots()
	ax.set_xlabel('Re')
	ax.set_ylabel('Im')
	ax.axvline(x=0, color='k', lw=1)
	ax.grid(True, which='both')

	# plots a blue "x" for the first roots
	ax.scatter(real_vals[0, :], imag_vals[0, :], 
					marker='x', 
					color='blue')

	# plots a red "o" for the last roots
	ax.scatter(real_vals[-1, :], imag_vals[-1, :],
					marker='o',
					color='red')

	gain_text = ['k = {:1.2f}'.format(k) for k in gains]

	temp_real_vals = real_vals[1:-1, :]
	temp_imag_vals = imag_vals[1:-1, :]
	color_range = range(temp_real_vals.shape[1])

	# plot the rest of the roots in different colors with respect to the regions
	for r, i, j in zip(temp_real_vals.T, temp_imag_vals.T, color_range):
		ax.plot(r, i, color=colors[j])
		
	return fig, ax

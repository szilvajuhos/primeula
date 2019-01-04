# 1. read primes from file and store diffs in data frame
# 2. generator for to make pairs for any delay in the Lamerey-diagram. I.e. for the
# series of primes:
#      3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61
# diff is:
#      2 2 4 2  4  2  4  6  2  6  4  2  4  6  6  2
# N=1
#   2,2
#   2,4
#   4,2
#   2,4
#   4,2
#   2,4
#   4,6
#   6,2
# N=2
#   2,4
#   4,4
#   4,4
#   4,2
#   2,4
#   4,4
#   4,6
# N=3
#   2,2
#   2,4
#   4,6
#   6,4
#   4,2
# N=7
#   2,6
#   6,6

# read primes and store in a list
primes = []
with open('5M_primes.dat') as f:
#with open('test.dat') as f:
    for line in f:
        primes.append(int(line.rstrip()) )

# make subsets
data_length = len(primes)
xs = primes[0:data_length-1]
ys = primes[1:data_length]

diff = []
for dpair in list(zip(xs,ys)):
    diff.append( dpair[1]-dpair[0] )
dxs = diff[0:data_length-2]
dys = diff[1:data_length-1]

# make a third column by the frequency of pairs
# to get frequencies make a dict
freq = {}
diffs = list(zip(dxs,dys))
for pair in diffs:
    try:
        freq[pair] = freq[pair]+1
    except KeyError:
        freq[pair] = 1

# now we have the frequencies, make the colors
# get the list of key tuples first:
coords = freq.keys()
# unzip lo get list of coords:
[pxs,pys] = zip(*coords)
# the third column is going to be the frequency: note, the dict is not ordered, so 
# we are re-creating a list to get the same order

import math
pfreq = []
for ppair in list(zip(pxs,pys)):
    pfreq.append(math.log(freq[ppair]))
    #pfreq.append(freq[ppair])

import matplotlib.pyplot as plt
plt.grid(True)
plt.scatter(pxs, pys, c=pfreq, marker=".", cmap='seismic',s=10)
plt.show()


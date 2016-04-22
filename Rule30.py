from pylab import *
import sys

def rule30(x, y, z):
    if x and y and z:
        return 0
    if x and y and not z:
        return 0
    if x and not y and z:
        return 0
    if x and not y and not z:
        return 1
    if not x and y and z:
        return 1
    if not x and y and not z:
        return 1
    if not x and not y and z:
        return 1
    if not x and not y and not z:
    	return 0
        
#Size of the automaton, specify before running
#Best size is 35      

try:
	num = int(sys.argv[1])
except Exception:
	print "Supply a size for the automaton"
	sys.exit()


graph = zeros((num, num*2), dtype=int)
graph[0, num] = 1
    
for i in arange(num-1)+1:
    for j in arange (num*2-1):
        graph[i,j] = rule30(graph[i-1, j-1], graph[i-1, j], graph[i-1, j+1])
            
for row in graph:
	print ''.join([str(x) for x in row.tolist()])

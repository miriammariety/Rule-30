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
#Best size is 35 (Depending how big the console is)     
try:
	num = int(sys.argv[1])
except Exception:
	print "Supply a size for the automaton"
	sys.exit()

#Create graph of zeros
graph = zeros((num, num*2), dtype=int)
#Set middle to one
graph[0, num] = 1
    
#Assign values for row and column
for i in arange(num-1)+1:
    for j in arange (num*2-1):
    	#Check the three cells above the current cell
        graph[i,j] = rule30(graph[i-1, j-1], graph[i-1, j], graph[i-1, j+1])
            
#Print graph
for row in graph:
	print ''.join([str(x) for x in row.tolist()])

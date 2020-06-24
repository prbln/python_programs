n =7
n=9
for i in range(1,n):
    print('- '*(n-i+1),end="")
    for j in range(i):
    	print('.|.',end=" ")
    	
    print('- '*(n-i+1),end=" ")
    print("")
    if n-i == 2:
    	break
    

nums = [1,2,3,4,5,6,7,8,9,10]
'''
my_list = []
for n in nums:
	my_list.append(n)
print (my_list)

#my_list = [n*n for n in nums]

my_list = [n for n in nums if n%2==0]
'''	
#print (my_list)

'''
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]

print (my_list)

# dictionary comprehension

names = ['bruce','clarck','peter','logan','wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']


my_dict =  {name: hero for name, hero in zip(names,heros) if name != 'peter'}

print (my_dict)


'''

nums = [1,2,3,4,32,1,2,4,4,3,2,2,65,7,9,9,7]

my_set = {n for n in nums}
print(my_set) 





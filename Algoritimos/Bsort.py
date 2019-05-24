#http://www.pythontutor.com/visualize.html#code=from%20random%20import%20randint%0Anums%3D%5B%5D%0An%3Dint%28input%28'contidade%20de%20elementos'%29%29%0A%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%0Afor%20k%20in%20range%20%280,n%29%3A%0A%20%20%20%20nums.append%28randint%280,5000%29%29%0A%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%23%0A%23Buble%20sort.%0A%0Afor%20i%20in%20range%20%280,len%28nums%29-1%29%3A%0A%20%20%20%20for%20j%20in%20range%20%28i%2B1,len%28nums%29%29%3A%0A%20%20%20%20%20%20%20%20if%20nums%5Bi%5D%3Enums%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nums%5Bi%5D,nums%5Bj%5D%3Dnums%5Bj%5D,nums%5Bi%5D%0A%20%20%20%20%20%20%20%20&cumulative=false&curInstr=559&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%2220%22%5D&textReferences=false


from random import randint
nums=[]
n=int(input('contidade de elementos'))
###################################
for k in range (0,n):
    nums.append(randint(0,5000))
###################################
#Bubble sort.

for i in range (0,len(nums)-1):
    for j in range (i+1,len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        
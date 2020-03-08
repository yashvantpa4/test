# Write your code here
index = int(input()) #this represents the nemuber of testcases
for i in range(index):
    N=int(input()) #Number of persons to travel
    a = list(map(int,input().split())) #this list shows the cost of each persons to travel
    b=sorted(a) #last program i didnt sort well there was little flaw so i sortedd the array and copied to b
    cost1=0 #intiali cost will be zero
    while N>3:
            op1 = b[0]+(2*b[1])+b[N-1] #this is shows the constraint to travel n people in the list this path is safest anyone can travel in this path more than 3 people
            op2 = (2*b[0])+b[N-1]+b[N - 2]
            cost1 = cost1 + min(op1,op2)
            N = N -2
    if N==3:
        cost1 = cost1 + sum(b[0:3]) #three person travel including driver and passsengers
    elif N==2:
        cost1 = cost1 +b[1] #two person
    else:
        cost1=cost1+b[0] #if one person
    print(cost1)
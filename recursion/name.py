def fun(n : int , i : int =0) -> str:
    if i==n:
        return "Printed"
    print('Name')
    fun(n,i+1)
    
# fun(10)

def sum_of_n(num,s=0):
    if num ==0:
        return s
    return sum_of_n(num-1,s + num)

# print(sum_of_n(3))

def sum_(n):
    if n ==1:
        return 1
    return n+sum_(n-1)

# print(sum_(3))

def swap_arr(i,arr):
    if i>len(arr)/2:
        return
    arr[i] , arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
    swap_arr(i+1,arr)
arr=[1,2,3,4,5]
swap_arr(0,arr)
print(arr)


def fun1(a,b):

    a = a+5
    b= b-2

a=10
b=12
fun1(a,b)
print(a,b)
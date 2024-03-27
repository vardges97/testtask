def primenums(n):
    if n=="":
        return ('variable cant be empty')
    elif not isinstance(n,int):
        return ("var must be a number")
    elif n<0:
        return ('variable cant be negative')
    else:
        return [num for num in range(2,n+1) if num>1 and all(num%i!=0 for i in range(2,num))]
x =primenums("hello")
# print(x)

x = [[i+j*2 for i in range(1,4)]for j in range(0,3)]
# print(x)

fib =lambda n: 1 if n == 1 or n==2 else fib(n-1)+fib(n-2)
# print(fib(9))

def sumofdigits(n):
    if n=="":
        return ('variable cant be empty')
    elif not isinstance(n,int):
        return ("var must be a number")
    elif n<0:
        return ('variable cant be negative')
    else :
        return 0 if n == 0 else int(n%10) + sumofdigits(int(n/10))
# print(sumofdigits())

def letnum(word):
    if word=="":
        return ('variable cant be empty')
    elif not isinstance(word,str):
        return ("var must be a string")
    # else:
    #     res={}
    #     for i in word:
    #         if res.get(i):
    #             res[i]+=1
    #         else:
    #             res[i]=1
    #     return res
    else:
        res = {i: word.count(i) for i in set(word)}
        return res
# print(letnum(223))


def sqroftwo(n):
    if n=="":
        return ('variable cant be empty')
    elif not isinstance(n,int):
        return ("var must be a number")
    elif n<0:
        return ('variable cant be negative')
    if n&(n-1)==0:
        return True
    else:
        return False
print(sqroftwo(-10))
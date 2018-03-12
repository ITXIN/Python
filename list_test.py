def f(x):
    return x*x

r = map(f,[1,2,4,5,6])
print(list(r))

print(list(map(str,[1,4,5,6,7])))

from functools import reduce
def add(x,y):
    return x + y
print(reduce(add,[1,2,4,5,]))

# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield b
#         a,b = b,a+b
#         n = n + 1
#     return 'done'
#
# g = fib(6)
# print(f)
# for n  in fib(6):
#     print(n)

# while True:
#     try:
#         x = next(g)
#         print('g',x)
#     except Exception as e:
#         print('generator return value',e.value)
#         break





# l = [x*x for x  in range(10)]
# print(l)
# g = (x*x for x  in range(10))
# print(g)
# for n  in g:
#     print(n)


# l = ['hello','world','IBM','Apple']
# [s.lover() for s in l]



# l = [x*x for x  in range(1,11) if x % 2 == 0]
# print(l)

# def person(name,age,**kw):
    # print('name',name,'age',age,'other',kw)

# def person(name,age,*,city,job):
#     print('name:',name,'age:',age,'city:',city,'job:',job)

# person('michael',30)
#
# person('ok',2,city='shanghai')
# extra = {'city':'shanghai','job':'worker'}
# person('jack',1,**extra)
# print(person)


#
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# print(power(5),power(5,2))

# def calc(*numbers):
#     sum = 0
#     for n  in numbers:
#         sum = sum + n*n
#     return sum
#
# c = calc(1,4,5)
# nums = [1,3,5]
# d = (1,6,7)
# print(calc(*nums))
# print(calc(*d))





# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('End')
#     return L
#
# add_end()
# print(add_end([2,45,5]))
# print(add_end())






# def power(x,n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# print(power(5,2))


# def my_abs(x):
#     print(x+1)
#
# my_abs(10)
# s1 = set([1,3,5])
# s1.add(6)
# s2 = set([2,4,6])
# print(s1&s2)





# d = {'m':95,'b':78,}
# print(d.get('c',-100))
# d.pop('b')
# print(d.get('b',-1))



# arr = ['1','3','5']
# arr.insert(2,'10')
# print(arr)

# tuple_test = ('m',['2','5'])
# tuple_test[1][0] = 'x'
# tuple_test[1][1] = 'y'
# print(tuple_test)
# for nam in arr:
#     print(nam)
# sum = 0
# for x in range(100):
#     sum += x
#     print(sum)

# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# 在 for i in range中i每次会被重新赋值   0，1，2，3，n-1     无论在for循环体中做了任何事
# 同时for i in range 相当于定义了变量 i 可以在后续的程序中被使用




for i in range(10):
    i = i+1
    print(i)

for i in range(5):
    print(i)



print(i)

#p为奇数, 编程实现方程x*x + y*y = p的  变量有x, y, u, v
p = 100069
x = pow(2, int((p-1)/4)) % p
y = 1
m = int((x*x + y*y) / p)
u = int(x % m)
v = 1
while(m!=1):
    xtmp = x
    ytmp = y
    x = int((u*xtmp + v*ytmp) / m)
    y = int((u*ytmp - v*xtmp) / m)
    m = int((x*x + y*y) / p)
    u = int(x % m)
    v = int(y % m)
	rpint(x, y)
	w(2, int((p-1)/4)) % p
	y = 1
	m = int((x*x + y*y) / p)
	u = int(x % m)
	v = 1
	while(m!=1):
	    xtmp = x
	    ytmp = y
 	    x = int((u*xtmp + v*ytmp) / m)
	    y = int((u*ytmp - v*xtmp) / m)
	    m = int((x*x + y*y) / p)
            u = int(x % m)
            v = int(y % m)
	    print(x, y)


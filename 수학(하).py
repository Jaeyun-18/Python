def dec_period(p,q,n):
    for i in range(n+1):
        m = p // q
        r = p % q
        print("%3d %3d %3d" %(i,m,r))
        p = 10 * r

    return

dec_period(19, 62, 20)

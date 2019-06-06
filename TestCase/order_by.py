def order_by():
    alist = [12,8,21,43,2,12,3]
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j]>=alist[j+1]:
                item= alist[j]
                alist[j]=alist[j + 1]
                alist[j+1]=item


    print(alist)


def jiujiu():
    for i in range (1,10):
        for j in range (1,i+1):
            print('%s * %s = %s'%(j,i,j*i),end='  ')

        print('')


def he():
    A = 0
    for i in range (1,51):
        if i % 2 == 1 :
            A = A +i
    print(A)






if __name__ == '__main__':
    order_by()
    jiujiu()
    he()
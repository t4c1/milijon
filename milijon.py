import numpy
#print help(numpy.linalg.norm)
def gen(n=10000):
    data=numpy.zeros(shape=(n,3*2+1))
    data[:,0]=numpy.random.rand(n)  ##masa
    data[:,1:3]=numpy.random.rand(n,2)  ## x in y      porazdelitev
    data[:,3]=numpy.sqrt(2-data[:,0]**2-data[:,1]**2)  ## z
    data[:,4:7]=numpy.cross(data[:,0:3],(0,0,1))  ##smer hitrosti
    #print numpy.linalg.norm(data[:,3:6],axis=1)
    nrm=numpy.linalg.norm(data[:,3:6],axis=1)**2
    data[:,3:6]/=numpy.vstack((nrm,nrm,nrm)).T  ##velikost hitrosti
    data[:,4:7]+=numpy.random.rand(n,3)-0.5 #nakljucnost hitrosti
    return data

G=1
def update(data,korak=0.1):
    n=data.shape[0]
    a=numpy.zeros(shape=(n,3))
    for i in range(1,n):
        data2=numpy.roll(data[:,0:4],n)  ##zamik
        dx=data2[:,1:4]-data[:,1:4]  ##vektor razdalje
        d = data2[:, 0]/ numpy.linalg.norm(dx, axis=1) ** 3
        a=+numpy.vstack((d, d, d)).T * dx
    data[:,4:7]+=G*korak*a
    data[:,1:4]+=korak*data[:,4:7]




if __name__=="__main__":
    data= gen()
    import time
    t=time.clock()
    update(data,0.1)
    print time.clock()-t
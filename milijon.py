import numpy
numpy.set_printoptions(linewidth=300,precision=2)

def gen(n=100):
    data=numpy.zeros(shape=(n,3*2+1))
    data[:,0]=1#numpy.random.rand(n)  ##masa
    data[:,1:3]=numpy.random.rand(n,2)  ## x in y      porazdelitev
    data[:,3]=numpy.sqrt(2-data[:,0]**2-data[:,1]**2)*0.3  ## z
    data[:,1:4]*=numpy.random.choice([1,-1],size=(n,3))*5
    data[:,4:7]=numpy.cross(data[:,1:4],(0,0,1))  ##smer hitrosti
    nrm=numpy.linalg.norm(data[:,3:6],axis=1)**2
    #data[:,4:7]/=numpy.vstack((nrm,nrm,nrm)).T  ##velikost hitrosti
    #data[:,4:7]+=numpy.random.rand(n,3)-0.5 #nakljucnost hitrosti
    data[:,4:7]*=15
    return data

G=1
def update_py(data,korak=0.1):
    for i in range(data.shape[0]):
        for j in range(data.shape[0]):
            if i!=j:
                dx=data[j,1:4]-data[i,1:4]
                data[i,4:7]+=G*korak*data[j,0]*dx /(dx[0]**2+dx[1]**2+dx[2]**2)**0.5 **3
    data[:,1:4]+=korak*data[:,4:7]

def update_np(data,korak=0.1): #ne dela pravilno!
    n=data.shape[0]
    a=numpy.zeros(shape=(n,3))
    for i in range(1,n):
        data2=numpy.roll(data[:,0:4],i)  # zamik
        dx=data2[:,1:4]- data[:,1:4]  # vektor razdalje
        d = data2[:, 0]/ numpy.linalg.norm(dx, axis=1) ** 3  # skalarni del formule
        a=+numpy.vstack((d, d, d)).T * dx
    data[:,4:7]+=G*korak*a
    data[:,1:4]+=korak*data[:,4:7]


if __name__=="__main__":
    data= gen()
    d2=data.copy()
    import time
    t=time.clock()
    update_np(data,0.1)
    print time.clock()-t
    t=time.clock()
    update_py(d2,0.1)
    print time.clock()-t
    print data-d2
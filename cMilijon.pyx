from libcpp.vector cimport vector

cdef extern from "milijon.cpp":
    cdef cppclass cZvezda "zvezda":
        float m,x,y,z,vx,vy,vz;
    cdef vector[cZvezda] cGen "gen"(int n)
    cdef void cUpdate "update"(vector[cZvezda] &data, float step)

from pandac.PandaModules import UnalignedLVecBase4f, PTA_LVecBase4f

cdef class wrapper:
    cdef vector[cZvezda] *ptr
    def __cinit__(self):
        self.ptr=new vector[cZvezda]()
    cdef cinit(self,vector[cZvezda]* obj):
        self.ptr=obj
        return self
    #def ___dealloc__(self):
     #   del self.ptr

cpdef wrapper gen(int n=1000):
    cdef vector[cZvezda]* r=new vector[cZvezda]()
    r[0]=cGen(100)
    return wrapper().cinit(r)

cpdef update(wrapper data,float step=0.1):
    cUpdate(data.ptr[0],step)

cpdef copy(dest, wrapper data,int n):
    cdef int i
    cdef cZvezda zv
    cdef vector[cZvezda]* ptr=data.ptr
    for i in range(n):
        #,y,z=self.data[i,1:4]*5
        zv=data.ptr[0][i]
        dest[i]=UnalignedLVecBase4f(zv.x,zv.y,zv.z,1)






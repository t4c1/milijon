
from panda3d.core import loadPrcFileData
# loadPrcFileData('', 'basic-shaders-only 0')
# loadPrcFileData("", "want-directtools #t")
# loadPrcFileData("", "want-tk #t")
loadPrcFileData("", "framebuffer-multisample 1")
loadPrcFileData('', 'multisamples 16')
# loadPrcFileData("", "threading-model App/Cull/Draw")
# loadPrcFileData("", "fullscreen #t")

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import PStatClient,CardMaker
from pandac.PandaModules import Point3, UnalignedLVecBase4f, PTA_LVecBase4f, Shader

from milijon import *

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        cm=CardMaker("cm")
        cm.setFrame(Point3(-1,-1,-1),Point3(1,-1,-1),Point3(1,1,-1),Point3(-1,1,-1))
        model = self.hidden.attachNewNode(cm.generate())
        model.setScale(0.1)
        #self.disableMouse()
        base.setFrameRateMeter(True)
        self.n=100
        self.data=gen(self.n)
        self.zvezde= self.render.attachNewNode("zvezde")
        model.reparentTo(self.zvezde)
        self.zvezde.setPosHpr(0,70,0,0,90,0)
        self.zvezde.setInstanceCount(self.n)
        myShader = Shader.load(Shader.SLGLSL, "vertex.glsl", "fragment.glsl" )
        self.zvezde.setShader(myShader)#Shader.load('instance.cg'))
        self.render.setShaderAuto()
        self.offsets = PTA_LVecBase4f.emptyArray(self.n);

        self.zvezde.setShaderInput('shader_data', self.offsets)
        self.zvezde.setShaderInput('shader_data[0]', self.offsets)
        #self.taskMgr.setupTaskChain('threaded chain', numThreads = 0, frameBudget = -1,frameSync = 1)
        self.taskMgr.add(self.update, "update")#,taskChain = 'threaded chain')

    def update(self,dt):
        #self.zvezde.forceRecomputeBounds()
        update_py(self.data,0.02)
        for i in range(self.n):
            x,y,z=self.data[i,1:4]*5
            self.offsets[i]=UnalignedLVecBase4f(x,y,z,1)
        return Task.cont




if __name__=="__main__":
    a=App()
    PStatClient.connect()
    a.run()
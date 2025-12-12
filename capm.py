import math
#我在分支上修改了这个文件
def getReturn(rm,beita):
    return rm*beita
def getCov(bx,qx,by,qy,qm):
    qxy=bx*by*qm*qm/(qx*qy)
    wx=math.sqrt(qx*qx-bx*bx*qm*qm)
    wy=math.sqrt(qy*qy-by*by*qm*qm)
    return(qxy,wx,wy)

if __name__=="__main__":
    print(getReturn(-0.05,1.05))
    print(getReturn(0.07,1.05))

    print(getCov(1.15,0.35,0.95,0.33,0.2))

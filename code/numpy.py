import  numpy as np





' '.join([str(i) for i in np.random.randint(10, size=100)])
#============================================

np.random()#between 0-1  size one elment 

np.randint(0,10)#between a,b  size one elment  int 

np.uniform(1,20)#between a,b  size one elment float 

np.randrange(start=2,stop=150,step=1)  #between start =2,stop=150,step=1  size one elment int  
np.randrange(150)#between start =0,stop=150,step=1 (defolt )  size one elment int

np.choice(['f','df','fe']) #between size list ,  size one elment  from list 

np.choice('sweet home alabama')

np.sample(range (10,50),10)#   range  (10,50)   shape 1d =10

a=list(range(10,50))

items = [1,2,3,4,5,6] # out put  [6, 2, 1, 5, 4, 3]
d=np.shuffle(items)          
#============================================
np.random.rand()#between 0-1  size shape
np.random.randn()#between -1-1  size shape  (normal destrputation )


np.random.rand(4,5)

s=np.random.randn(4,5)
np.round(s,2)
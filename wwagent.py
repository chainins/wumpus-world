# -*- coding: utf-8 -*-

###############################################
#                                             #
#             Mon Nov 30 20:10:12 2020        #
#                                             #
###############################################

"""

This is an agent could find the gold in a wumpus world.
The basic method is truth-table enumeration-based entailment
(model checking).
In this code, enumerates all possible model by truth-table
and calculate the probability  of alpha is true.
If the probability  is 1, means alpha is True.
If the probability  is 0, means alpha is False.

If the agent finds the wumpus, it would shoot the wumpus.

All of the perceptions could contribute to the KB(Knowledge-Base) at the 
earliest time.

To accelerate this process( reduce both space complexity and time complexity),
this code also takes several measures:
    1) all of the perceptions would append corresponding elements to KB and 
    dicKB (which records the truth-table already determined, and checked in the 
    beginning of the method of model check) AMAP.
    2) symbol list only includes w(i,j) and p(i,j) since breeze and stench are 
    perceptions and would not be influenced by logic calculations.
    3) Only the grids in KB,dicKB and adjacent ones are added to symbol list.

All of the demands are satisfied. The agent could:
    1) find all of the 100% guguaranteed safe grids around current position.
    2) calculate probabilities of the grids around not 100% guaranteed safe.
    3) identify whether a location is safe at the earliest time possible 
    given percepts.
    4) not get killed because of step 2 above, and eventually find gold 
    and win the game if it is reachable.
    
The performance of the code: less than 1 second each round mostly.
    
According to the demands, this code could work well with the original wwsim.py.

In order to observe the result, a modified wwsim.py is also supplied 
though it isn't necessary.
(in the modified wwsim.py, a timer is added in nonGUI, and step counter and "autoRun" 
button are also added in GUI mode)

--------------------------------------------------------------------
Modified from wwagent.py written by Greg Scott

Modified to only do random motions so that this can be the base
for building various kinds of agent that work with the wwsim.py 
wumpus world simulation -----  dml Fordham 2019

# FACING KEY:
#    0 = up
#    1 = right
#    2 = down
#    3 = left

# Actions
# 'move' 'grab' 'shoot' 'left' right'

"""


from random import randint
from random import shuffle

# This is the class that represents a rational agent

class WWAgent:

    def __init__(self):
        self.max=4 # number of cells in one side of square world
        self.stopTheAgent=False # set to true to stop th agent at end of episode
        self.position = (0, self.max-1) # top is (0,0)  
        self.directions=['up','right','down','left']
        self.facing = 'right'
        self.arrow = 1
        self.percepts = (None, None, None, None, None)
        ########################## Chengpi modified below #####################
        # add some new attributes
        self.rowSize = self.max
        self.colSize = self.max
        self.KB = []
        self.dicKB = []
        self.dicKB.append(('w03',False))
        self.dicKB.append(('p03',False))
        self.nextfacing = 'right' # next facing 
        self.nextpos =() # next position
        self.numTrueKB = 0 # model check, to calculate prob
        self.numTrueAlpha = 0 # model check, to calculate prob
        self.symbolsList = [] # for model check
        self.wumpusGrid = () # the position of wumpus
        self.wumpusAlive = True # check whether wumpus died
        self.visitedGrids = [] # record grids already visited
        self.step = 0
        print("\n\nNew rational(smart) agent created ------------------")
        
    '''Check whether prop is true in model'''        
    def isTrue(self,prop,model):
        # assumes prop and model use the list/logic notation
        if isinstance(prop,str):
            return (prop,True) in model
        elif len(prop)==1:
            return self.isTrue(prop[0],model)
        elif prop[0]=='not':
            return not self.isTrue(prop[1],model)
        elif prop[1]=='and':
            return self.isTrue(prop[0],model) and self.isTrue(prop[2],model)
        elif prop[1]=='or':
            return self.isTrue(prop[0],model) or self.isTrue(prop[2],model)
        elif prop[1]=='implies':
            return (not self.isTrue(prop[0],model)) or self.isTrue(prop[2],model)
        elif prop[1]=='iff':
            left = (not self.isTrue(prop[0],model)) or self.isTrue(prop[2],model)
            right= (not self.isTrue(prop[2],model)) or self.isTrue(prop[0],model)
            return (left and right)
        return False


#
# Enumerate all possible models
# and check if the models that satisfy
# KB are a subset of those that satisfy alpha
# KB entails alpha implies M(KB) subset M(alpha)


    def checkDicKB(self,alpha,dicKB):
        if (alpha[0],True) in dicKB:
            return True
        if (alpha[0],False) in dicKB:
            return False
    
        
    # emulate the true-value table, check whether alpha is True when KB is True
    # based on model. Count the number of the True-value of alpha and KB for
    # the calculation of probabilities later.
    def modelCheck(self,symbols,model,KB,alpha,dicKB):
        if len(symbols)==0:
            if self.isTrue(self.KB,model): 
                self.numTrueKB = self.numTrueKB + 1   # count how many KB == True.
                checkAlpha = self.isTrue(alpha,model)
                if checkAlpha:
                    self.numTrueAlpha = self.numTrueAlpha + 1    # count how many Alpha == True.
            else:   # KB=False
                return True 
        else:
            p = symbols[0]
            rest = list(symbols[1:len(symbols)])
            if (p,True) in self.dicKB: 
                return self.modelCheck(rest,model+[(p,True)],self.KB,alpha,self.dicKB) 
            elif (p,False) in self.dicKB:
                return self.modelCheck(rest,model+[(p,False)],self.KB,alpha,self.dicKB)
            else:
                firstPart = self.modelCheck(rest,model+[(p,True)],self.KB,alpha,self.dicKB) 
                secondPart = self.modelCheck(rest,model+[(p,False)],self.KB,alpha,self.dicKB)
                # code modified to emulate all true-value table
                return firstPart and secondPart

    # collect Grids from (KB) as symbols
    def collectGrids(self,complexList):
        for elem in complexList:
            if isinstance(elem,str): 
                if (elem[0]=='w' or elem[0]=='p'):
                    if (not (elem in self.symbolsList)):
                        self.symbolsList.append(elem)
            else:
                self.collectGrids(elem)
  
    # extract Grids from (dicKB) as symbols
    def extractGrids(self,complexList):
        for elem in complexList:
                if not (elem[0] in self.symbolsList):
                    self.symbolsList.append(elem[0])
 
    
    # original code modified. 
    # According to the latest perceptions, the agent updates KB & dicKB.
    
    def update(self, percept):
        self.percepts=percept
        ###############      chengpi modified      #######################
        print("Current Position ",self.position)
        r = self.position[0]
        c = self.position[1]
        if 'scream' in self.percepts and self.wumpusAlive == True: # shoot successful.
            for j in range(self.rowSize):
                for k in range(self.colSize):
                    if j!=r and k!=c:
                        gridx = 'w'+str(j)+str(k)
                        if not ( (gridx,False) in self.dicKB):
                            self.dicKB.append((gridx,False))
                    # if ( (r,c) in self.dicKB):
                    #     self.dicKB.append((gridx,False))
            print("\nWumpus died ! ",'w'+str(r)+str(c))
            self.wumpusGrid = ()
            self.wumpusAlive = False
        if not ((r,c) in self.visitedGrids): # if visited, already added. don't repeat
            wList = []
            pList = []
            if 'stench' in self.percepts and self.wumpusAlive == True: # after wumpus died don't change dicKB
                if ((r - 1) >= 0):
                    gridx = 'w'+str(r-1)+str(c)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)
                    if len(wList)==0:
                        wList =  [gridx]
                    else:
                        wList = [wList] + ['or',gridx]
                if ((r + 1) < 4):
                    gridx = 'w'+str(r+1)+str(c)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)
                    if len(wList)==0:
                        wList =  [gridx]
                    else:
                        wList = [wList] + ['or',gridx]
                if ((c - 1) >= 0):
                    gridx = 'w'+str(r)+str(c-1)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)
                    if len(wList)==0:
                        wList =  [gridx]
                    else:
                        wList = [wList] + ['or',gridx]
                if ((c + 1) < 4):
                    gridx = 'w'+str(r)+str(c+1)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)
                    if len(wList)==0:
                        wList =  [gridx]
                    else:
                        wList = [wList] + ['or',gridx]
                if not (len(wList) == 0):
                    if len(self.KB) == 0:
                        self.KB = wList
                    else:
                        self.KB = [self.KB] + ['and',wList]
            else:
                if ((r - 1) >= 0):
                    gridx = 'w'+str(r-1)+str(c)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if not ( (gridx,False) in self.dicKB):
                        self.dicKB.append((gridx,False))
                if ((r + 1) < 4):
                    gridx = 'w'+str(r+1)+str(c)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if not ( (gridx,False) in self.dicKB):
                        self.dicKB.append((gridx,False))
                if ((c - 1) >= 0):
                    gridx = 'w'+str(r)+str(c-1)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if not ( (gridx,False) in self.dicKB):
                        self.dicKB.append((gridx,False))
                if ((c + 1) < 4):
                    gridx = 'w'+str(r)+str(c+1)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if not ( (gridx,False) in self.dicKB):
                        self.dicKB.append((gridx,False))
            if 'breeze' in self.percepts:
                if ((r - 1) >= 0):
                    gridx = 'p'+str(r-1)+str(c)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if len(pList)==0:
                        pList =  [gridx]
                    else:
                        pList = [pList] + ['or',gridx]
                if ((r + 1) < 4):
                    gridx = 'p'+str(r+1)+str(c)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if len(pList)==0:
                        pList =  [gridx]
                    else:
                        pList = [pList] + ['or',gridx]
                if ((c - 1) >= 0):
                    gridx = 'p'+str(r)+str(c-1)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if len(pList)==0:
                        pList =  [gridx]
                    else:
                        pList = [pList] + ['or',gridx]
                if ((c + 1) < 4):
                    gridx = 'p'+str(r)+str(c+1)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if len(pList)==0:
                        pList =  [gridx]
                    else:
                        pList = [pList] + ['or',gridx]
                if not (len(pList) == 0):
                    if len(self.KB) == 0:
                        self.KB = pList
                    else:
                        self.KB = [self.KB] + ['and',pList]
            else:
                if ((r - 1) >= 0):
                    gridx = 'p'+str(r-1)+str(c)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if not ( (gridx,False) in self.dicKB):
                        self.dicKB.append((gridx,False))
                if ((r + 1) < 4):
                    gridx = 'p'+str(r+1)+str(c)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if not ( (gridx,False) in self.dicKB):
                        self.dicKB.append((gridx,False))
                if ((c - 1) >= 0):
                    gridx = 'p'+str(r)+str(c-1)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if not ( (gridx,False) in self.dicKB):
                        self.dicKB.append((gridx,False))
                if ((c + 1) < 4):
                    gridx = 'p'+str(r)+str(c+1)
                    if not(gridx in self.symbolsList):
                        self.symbolsList.append(gridx)                
                    if not ( (gridx,False) in self.dicKB):
                        self.dicKB.append((gridx,False))
            self.visitedGrids.append((r,c))
            gridx = 'p'+str(r)+str(c)
            if not(gridx in self.symbolsList):
                self.symbolsList.append(gridx)                
            if not ( (gridx,False) in self.dicKB):
                self.dicKB.append((gridx,False))
            gridx = 'w'+str(r)+str(c)
            if not(gridx in self.symbolsList):
                self.symbolsList.append(gridx)                
            if not ( (gridx,False) in self.dicKB):
                self.dicKB.append((gridx,False))
    

    # Since there is no percept for location, the agent has to predict
    # what location it is in based on the direction it was facing
    # when it moved

    def calculateNextPosition(self):
        if self.nextfacing =='up':
            nextPosition = (self.position[0],max(0,self.position[1]-1))
        elif self.nextfacing =='down':
            nextPosition = (self.position[0],min(self.max-1,self.position[1]+1))
        elif self.nextfacing =='right':
            nextPosition = (min(self.max-1,self.position[0]+1),self.position[1])
        elif self.nextfacing =='left':
            nextPosition = (max(0,self.position[0]-1),self.position[1])
        return nextPosition

    # and the same is true for the direction the agent is facing, it also
    # needs to be calculated based on whether the agent turned left/right
    # and what direction it was facing when it did
    
    def calculateNextDirection(self,action):
        if self.facing=='up':
            if action=='left':
                self.facing = 'left'
            else:
                self.facing = 'right'
        elif self.facing=='down':
            if action=='left':
                self.facing = 'right'
            else:
                self.facing = 'left'
        elif self.facing=='right':
            if action=='left':
                self.facing = 'up'
            else:
                self.facing = 'down'
        elif self.facing=='left':
            if action=='left':
                self.facing = 'down'
            else:
                self.facing = 'up'


    # generate probability of alpha
    def calculateProb(self,r,c,alpha):
        self.symbolsList = []
        self.collectGrids(self.KB)
        self.extractGrids(self.dicKB)       
        inDicKB = self.checkDicKB(alpha,self.dicKB) # True / False
        if inDicKB is None:
            self.numTrueKB = 0
            self.numTrueAlpha = 0
            if not self.KB:
                self.KB = [['not','w03'],'and',['not','p03']]  # in case KB is null at beginning. changes when row and col changes
            Result = self.modelCheck(self.symbolsList,[],self.KB,alpha,self.dicKB)
            if(self.numTrueKB==0):
                prob = 1
            else:
                prob = self.numTrueAlpha/self.numTrueKB
            return alpha+[prob]
        elif inDicKB: # alpha, True 
            return alpha+[1]
        elif not inDicKB:   # alpha, False, append to dicKB!
            return alpha+[0]

                 
            
    # check whether a grid is safe,return to safeList,failList,probList 
    # if not sure it's safe or pit or wumpus, calculate sum of prob(w & p).
    def trygrid(self,r,c):
        porbWList = self.calculateProb(r,c,['w'+str(r)+str(c)])
        porbPList = self.calculateProb(r,c,['p'+str(r)+str(c)])
        if ((porbWList[1]==1  and self.wumpusAlive == True) or porbPList[1] == 1):
            if porbWList[1]==1 and self.wumpusAlive == True:
                if not (('w'+str(r)+str(c),True) in self.dicKB):
                    self.dicKB.append(('w'+str(r)+str(c),True)) # append to dicKB! 
                    self.wumpusGrid = (r,c)
            if porbPList[1]==1:
                if not (('p'+str(r)+str(c),True) in self.dicKB):
                    self.dicKB.append(('p'+str(r)+str(c),True)) # append to dicKB!
            return None,(r,c),None # safe grid list, fail grid list, prob list
        elif ((porbWList[1]==0 or self.wumpusAlive == False)  and porbPList[1] == 0):
            if porbWList[1]==0:
                if not (('w'+str(r)+str(c),False) in self.dicKB):
                    self.dicKB.append(('w'+str(r)+str(c),False)) # append to dicKB!
            if porbPList[1]==0:
                if not (('p'+str(r)+str(c),False) in self.dicKB):
                    self.dicKB.append(('p'+str(r)+str(c),False)) # append to dicKB!
            return (r,c),None,None            
        else:
            return None,None,(r,c,porbPList[1] + porbWList[1]) 


    # create local symbols
    def symbolCreateList(self,r,c): 
        # current grid don't need to check, but symbols needed!.
        # smybols don't includes b,s. just w,p
        self.symbolsList = []
        self.symbolsList.append('w' + str(r) + str(c))
        self.symbolsList.append('p' + str(r) + str(c))
        if ((r - 1) >= 0):
            self.symbolsList.append('w' + str(r-1) + str(c))
            self.symbolsList.append('p' + str(r-1) + str(c))
        if ((r + 1) < 4):
            self.symbolsList.append('w' + str(r+1) + str(c))
            self.symbolsList.append('p' + str(r+1) + str(c))
        if ((c - 1) >= 0):
            self.symbolsList.append('w' + str(r) + str(c-1))
            self.symbolsList.append('p' + str(r) + str(c-1))
        if ((c + 1) < 4):
            self.symbolsList.append('w' + str(r) + str(c+1))
            self.symbolsList.append('p' + str(r) + str(c+1))

        
    # Check whether the 4 adjacent grids are safe.
    def try4grids(self,r,c):
        safeGrids = []
        failGrids = []
        probGrids = []
        if ((r - 1) >= 0):
            self.symbolCreateList(r-1,c)
            safeResult,failResult,probResult = self.trygrid(r-1,c)
            if safeResult is not None: safeGrids.append(safeResult)
            if failResult is not None: failGrids.append(failResult)
            if probResult is not None: probGrids.append(probResult)
        if ((r + 1) < 4):
            self.symbolCreateList(r+1,c)
            safeResult,failResult,probResult = self.trygrid(r+1,c)
            if safeResult is not None: safeGrids.append(safeResult)
            if failResult is not None: failGrids.append(failResult)
            if probResult is not None: probGrids.append(probResult)
        if ((c - 1) >= 0):
            self.symbolCreateList(r,c-1)
            safeResult,failResult,probResult = self.trygrid(r,c-1)
            if safeResult is not None: safeGrids.append(safeResult)
            if failResult is not None: failGrids.append(failResult)
            if probResult is not None: probGrids.append(probResult)
        if ((c + 1) < 4):
            self.symbolCreateList(r,c+1)
            safeResult,failResult,probResult = self.trygrid(r,c+1)
            if safeResult is not None: safeGrids.append(safeResult)
            if failResult is not None: failGrids.append(failResult)
            if probResult is not None: probGrids.append(probResult)
        return safeGrids,failGrids,probGrids

    # calculate the turn action according to current and next facing
    def calculateAction(self):
        if self.nextfacing=='up':
            if self.facing == 'up':
                action ='move'
            elif self.facing == 'left':
                action='right'
            else:   # right or down
                action='left'
        if self.nextfacing=='down':
            if self.facing == 'down':
                action ='move'
            elif self.facing == 'left':
                action ='left'
            else:   # right or up
                action ='right'
        if self.nextfacing =='right':
            if self.facing == 'right':
                action ='move'
            elif self.facing == 'up':
                action ='right'
            else:   # left or down
                action ='left'
        if self.nextfacing =='left':
            if self.facing == 'left':
                action ='move'
            elif self.facing == 'up':
                action ='left'
            else:   # right or down
                action ='right'
        return action
                
    # this is the function that will pick the next action of
    # the agent. 
    
    def action(self):
        self.step +=1
        print("\nStep:", self.step,end="\n")
        action =''
        # check whether last action is turn direction and reaches nextfacing
        if (self.facing != self.nextfacing) or len(self.nextpos)==2:
            if self.facing != self.nextfacing: # turn at most twice
                action = self.calculateAction() 
                self.calculateNextDirection(action)
            elif len(self.nextpos)==2:
                if len(self.wumpusGrid)==2:
                    action = 'shoot' # don't need to change self.position
                else:
                    action = 'move'
                    self.position = self.nextpos # got to new position to percept
                self.nextpos = ()
            print ("Continuously turning :",action, "-->",self.position[1],
                   self.position[0], self.facing)
            return action

        # test for controlled exit at end of successful gui episode
        if self.stopTheAgent:
            print("Agent has won this episode.")
            return 'exit' # will cause the episide to end
            
        #reflect action -- get the gold!
        if 'glitter' in self.percepts:
            print("Agent will grab the gold!")
            self.stopTheAgent=True
            return 'grab'

        # check grid around current grid
        safeList,failList,probList = self.try4grids(self.position[0],self.position[1])

        # double check, put all visited grids in safe grids list
        for probgrid in probList:
            if (probgrid[0],probgrid[1]) in self.visitedGrids:
                probList.remove(probgrid)
                safeList.append((probgrid[0],probgrid[1]))
        
        coin = 100 # sometimes agent loops in safe grids, jump out ramdonly
        if len(self.wumpusGrid)==2:
            action = 'shoot'
            selectedGrid = self.wumpusGrid
        else:
            if len(safeList)>0: # safe grids list not null, choose randomly
                i=0
                shuffle(safeList)
                while True: # find the first new grid
                    selectedGrid = safeList[i]
                    if  (not (selectedGrid in self.visitedGrids)): # find one
                        break
                    else: # next
                        i = i+1 # next
                    if i==len(safeList): # visited all, redo from first
                        selectedGrid = safeList[0]
                        coin = randint(0,4) # 20% chance of jump out, probList
                        break
            if ((not len(safeList)>0) and len(probList)>0) or (len(safeList)>0 and coin==0 and len(probList)>0):
                # if there are no safe grid, or jumpu out loop of safe grids
                # rank possibility list: probList
                probList = sorted(probList, key=lambda x: x[2], reverse=False) # Ascending Prob of Risk
                i = 0
                selectedGridOptions = []
                leastProb = 2 # ( it's sum of two prob. of w & p)
                while True: # find the first new grid
                    if  leastProb >= probList[i][2]: # find one or more grids least risy
                        selectedGrid = probList[i]
                        if (not ((selectedGrid[0],selectedGrid[1]) in self.visitedGrids)):
                            leastProb = probList[i][2]
                            selectedGridOptions.append(selectedGrid)
                        i = i+1 # next
                    else:
                        break
                    if i==len(probList): # visited All, redo first gird
                        selectedGrid = probList[0]
                        probRisk = probList[0][2]
                        selectedGridOptions.append(selectedGrid)
                        break
                if len(selectedGridOptions)>1:
                    i = randint(0,len(selectedGridOptions)-1)
                    selectedGrid = (selectedGridOptions[i][0],selectedGridOptions[i][1])
                    probRisk = selectedGridOptions[i][2]
                else:
                    selectedGrid = (selectedGridOptions[0][0],selectedGridOptions[0][1])
                    probRisk = probList[0][2]
            
        if (self.position[0],self.position[1]-1) == selectedGrid:
            self.nextfacing = 'up'
        if (self.position[0],self.position[1]+1) == selectedGrid:
            self.nextfacing = 'down'
        if (self.position[0]+1,self.position[1]) == selectedGrid:
            self.nextfacing = 'right'
        if (self.position[0]-1,self.position[1]) == selectedGrid:
            self.nextfacing = 'left'
        

        self.nextpos = selectedGrid
        if self.facing == self.nextfacing:
            if len(self.wumpusGrid)==2:
                action = 'shoot'
            else:
                action = 'move'
                self.position = (selectedGrid[0],selectedGrid[1])
                self.nextpos = ()
        else: # still not faces nextfacing
            action = self.calculateAction() # turn
            self.calculateNextDirection(action) # nextfacing

            

       # choose a direction, and move          
        print ("Rational Agent(smart):",action, "-->",self.position[0],
               self.position[1], self.facing)
        return action

# This is the class that represents an agent of random

class WWAgent_random:

    def __init__(self):
        self.max=4 # number of cells in one side of square world
        self.stopTheAgent=False # set to true to stop th agent at end of episode
        self.position = (0, 3) # top is (0,0)
        self.directions=['up','right','down','left']
        self.facing = 'right'
        self.arrow = 1
        self.percepts = (None, None, None, None, None)
        self.map = [[ self.percepts for i in range(self.max) ] for j in range(self.max)]
        self.step=0
        print("\n\nNew random agent created ------------------")

    # Add the latest percepts to list of percepts received so far
    # This function is called by the wumpus simulation and will
    # update the sensory data. The sensor data is placed into a
    # map structured KB for later use
    
    def update(self, percept):
        self.percepts=percept
        #[stench, breeze, glitter, bump, scream]
        if self.position[0] in range(self.max) and self.position[1] in range(self.max):
            self.map[ self.position[0]][self.position[1]]=self.percepts
        # puts the percept at the spot in the map where sensed

    # Since there is no percept for location, the agent has to predict
    # what location it is in based on the direction it was facing
    # when it moved

    def calculateNextPosition(self,action):
        if self.facing=='up':
            self.position = (self.position[0],max(0,self.position[1]-1))
        elif self.facing =='down':
            self.position = (self.position[0],min(self.max-1,self.position[1]+1))
        elif self.facing =='right':
            self.position = (min(self.max-1,self.position[0]+1),self.position[1])
        elif self.facing =='left':
            self.position = (max(0,self.position[0]-1),self.position[1])
        return self.position

    # and the same is true for the direction the agent is facing, it also
    # needs to be calculated based on whether the agent turned left/right
    # and what direction it was facing when it did
    
    def calculateNextDirection(self,action):
        if self.facing=='up':
            if action=='left':
                self.facing = 'left'
            else:
                self.facing = 'right'
        elif self.facing=='down':
            if action=='left':
                self.facing = 'right'
            else:
                self.facing = 'left'
        elif self.facing=='right':
            if action=='left':
                self.facing = 'up'
            else:
                self.facing = 'down'
        elif self.facing=='left':
            if action=='left':
                self.facing = 'down'
            else:
                self.facing = 'up'


    # this is the function that will pick the next action of
    # the agent. This is the main function that needs to be
    # modified when you design your new intelligent agent
    # right now it is just a random choice agent
    
    def action(self):
        self.step +=1
        print("\nStep:", self.step,end="\n")

        # test for controlled exit at end of successful gui episode
        if self.stopTheAgent:
            print("Agent has won this episode.")
            return 'exit' # will cause the episide to end
            
        #reflect action -- get the gold!
        if 'glitter' in self.percepts:
            print("Agent will grab the gold!")
            self.stopTheAgent=True
            return 'grab'
        
        # choose a random direction, and move          
        actionSelection = randint(0,1)
        if actionSelection>0: # there is an 50% chance of moving forward 
            action = 'move'
            # predict the effect of this
            self.calculateNextPosition(action)
        else: # pick left or right 50%
            actionSelection=randint(0,1)
            if actionSelection>0:
                action = 'left'
            else:
                action='right'
            # predict the effect of this
            self.calculateNextDirection(action)
        print ("Random agent:",action, "-->",self.position[0],
               self.position[1], self.facing)
        return action

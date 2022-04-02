import random

class card():
    
    def __init__(self, number_of_colors, depth):
        self.unshuffled_beads= []
        self.number_of_colors = number_of_colors
        self.depth = depth
        
        for i in range(0,number_of_colors):       #generating unshuffled beads
            t = []
            for k in range(0,depth):
                t.append(char(65+i))
            t= tuple(t)
            self.unshuffled_beads.append(t)
        self.user_unshuffled_beads = []
        for_shuffled = []
        for i in self.unshuffled_beads:
            for_shuffled.append(list(i))
            self.user_unshuffled_beads.append(list(i))
        self.shuffled_beads =self.shuffle(for_shuffled)
        
        
    def shuffle(self, unshuffledBeads):
        list1= [ x for x in range(0,self.number_of_colors)]
        list2= [ x for x in range(0,self.depth)]
        for j in range(0,random.randrange(3, self.depth+ self.number_of_colors)):
            x1= random.choice(list1)
            y1= random.choice(list2)
            x2= random.choice(list1)
            y2= random.choice(list2)
            
            unshuffledBeads[x2][y2], unshuffledBeads[x1][y1]= unshuffledBeads[x1][y1], unshuffledBeads[x2][y2]
        return unshuffledBeads
    
    
    def reset(self):
        pass
    
    def show(self):
        for i in range(len(self.unshuffled_beads[0])):
            print("|",end=' ')
            for j in range(0,len(self.unshuffled_beads)):
                print(self.unshuffled_beads[j][i], end=' ')
            print("|")
        print("+", end= ' ')
        for k in range(len(self.unshuffled_beads[0])):
            print("-", end=' ')
        print("+")
        
    def stack(self,number):
        return self.shuffled_beads[number-1]
    
    def __str__(self) -> str:                      #this function returns a str
        string=" "
        for i in range(0, self.number_of_colors):
            string += '|'
            for k in range(0,self.depth):
                string += self.shuffled_beads[i][k]
            string += '|'
        return string
    
    def replace(self, filename,n):
        pass
        
        
class BStack:
    
    def __init__(self, maximum_capacity) -> None:       #this function returns None
        self.maximum_capacity = maximum_capacity
        self.stacks = []
        
    def push(self,item):
        if len(self.stacks)>self.maximum_capacity:
            print("The stack isFull ")
        else:
            self.stacks.append(item)
            
    def pop(self):
        if len(self.stack)==0:
            print("The stack isUnderflow")
        else:
            return self.stacks.pop()
        
    def isFull(self):
        return len(self.stacks)>= self.maximum_capacity
    
    def index(self):
        last_index = len(self.stacks)-1
        
        return self.stacks[last_index]
    
    
class AbacoStack(card):
    
    def __init__(self, color, depth):
        card.__init(self,color,depth)
        self.rows_length= color+1
        self.movement = 0
        
    def moveBead(self,move):
        if move == 'r':
            print("The moves are reseted")
            self.reset()
            
            
        
            
                 
        
            
            
    
            
        
        
        
        
    
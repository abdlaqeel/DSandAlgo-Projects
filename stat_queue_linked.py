#Submitted by Abdullah Aqeel Student ID: 202043030
from linked_queue import LinkedQueue #importing class from notes
class node:
   def __init__(self,number):
       self.number=number
       self.next=None
#queue class       
class StatQueue(LinkedQueue):
    def _init_(self):
        super()._init_()
        self._max=None
        self._min=None
        self._mean=0
        self.totalsum=0   
#accesor methods for min, max and mean       
    def min(self):
        return self._min

    def max(self):
        return self._max
 
    def mean(self):
        return self._mean
#enqueue mthod       
    def EnQueue(self,number):
        temp=node(number)
        if(self.rear==None):
            self.size=self.size+1
            self.front=self.rear=temp
            self._max=number
            self._min=number
            self.totalsum=self.totalsum+number
            self._mean=(self.totalsum)/(self.size)
            return
        self.size=self.size+1
        if(number>self._max):
            self._max=number
        if(number<self._min):
            self._min=number
            self.totalsum=self.totalsum+number
            self._mean=(self.totalsum)/(self.size)
            self.rear.next=temp
            self.rear=temp
#dequeue     
    def DeQueue(self):
        if self.isEmpty():
               return ' ' 
        temp = self.front
        self.front = temp.next
     
        if(self.front == None):
            self.rear = None
        self.size=self.size-1

  

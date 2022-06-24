#Submitted by Abdullah Aqeel Student ID: 202043030
from linked_queue import LinkedQueue
from array_queue import ArrayQueue

class RoundRobinScheduler:
  """Round Robin Scheduler Simulation.
  Implement the scheduler
  Print each time slice or changes
  Print final reults: table of completion time, turnaround waiting time
  ?Experiment effect of slice time to performane
  """
  
  """
  Nested class for task definition
  """
  class _Task:
    def __init__(self, id = None):
      super()._init_() #inherits the class
      self._PID = id            #the task id, could be string
      self._arrivalTime = 0     #the arrival time, in ms
      self._taskTime = 0        #the task time required to finish the job, in ms
      self._taskTimeLeft = self._taskTime   #task time left to be finished. It is initialized using the task time
      self._completeTime = 0    #task completed at clock time
    def print(self):
      print("Task ID: " + self._PID +
            "\t Arrival time: " + str(self._arrivalTime) +
            "\t Task time: " + str(self._taskTime) +
            "\t Complete at: " + str(self._completeTime) +
            "\t Completion time: " + str(self._completeTime - self._arrivalTime) +
            "\t Waiting time: " + str(self._completeTime - self._arrivalTime - self._taskTime))
  def __init__(self):
    """Create an empty queue."""
    self._tasksInQueue = ArrayQueue()   #This is the Robin Queue
    self._clock = 0             #this clock keeps increase by timeslice (quantum time) or task remaining time when it <= timeslice
    self._timeSlice = 100       #Here we set the quantum time as 100 ms
    
    self._tasksList = ArrayQueue() #tasks list to be send into the round robin queue
    self._setUpTaskList() #method that set up some test data

  def _setUpTaskList(self):
    """Initialize the waittime tasks list
    """
    newTask = self._Task("P0")
    newTask._arrivalTime = 0
    newTask._taskTimeLeft = newTask._taskTime = 250
    self._tasksList.enqueue(newTask)
    newTask = self._Task("P1")
    newTask._arrivalTime = 50
    newTask._taskTimeLeft = newTask._taskTime = 170
    self._tasksList.enqueue(newTask)
    newTask = self._Task("P2")
    newTask._arrivalTime = 130
    newTask._taskTimeLeft = newTask._taskTime = 75
    
    self._tasksList.enqueue(newTask)
  
  def scheduling(self): #incomplete
    start_time = []
        exit_time = []
        start_time = 0
        ready_queue = []
        executed_process = []
        process_data.sort(key=lambda x: x[1])
        while 1:
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= start_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3]])
                        ready_queue.append(temp)
                        temp = []
        while tasksList and tasksInQueue != 0:
    
        if self._taskTimeLeft <= self._timeSlice :
            self._clock += self._taskTimeLeft
            self._task__str__()
        else:
            self._clock += self._timeslice
            self._taskTimeLeft -= self._timeslice

            print(f"Sequence of Processes: {executed_process}")

    
    
    """Scheduling algorithm"""
   
    """Some suggested notes might help your implementation, BUT YOU CAN ALWAYS DO YOUR OWN WAY!
    1 keep running while both tasks list and robin queue is not empty
    2 keep enqueue into Robin queue for those arrival time before next time slot
    3 process the first task in the Robin Queue
        3.1 if the task can be finished with next time slot (_taskTimeLeft <= self._timeSlice), clock increases by the task time left, task finished, record the complete time and print the finished task
        3.2 else clock increases by time slice, _taskTimeLeft decreases by time slice, put back to the queue
    """
    """
        YOUR CODE GOES HERE


    
      """

    def calculateWaitingTime(self, process_data):#returns average waiting times
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_wait_time = total_wait_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_wait_time / len(process_data) #calculates the average
        return average_waiting_time
      
    #prints the data in required format"
    def printData(self, process_data, average_turnaround_time, average_waiting_time, executed_process):
        process_data.sort(key=lambda x: x[0])
      
        print("Process_ID  Arrival_Time  Rem_Burst_Time   Completed  Original_Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j], end="                         ")
            print()

        print(f"Average Turnaround Time: {average_turnaround_time}")

        print(f"Average Waiting Time: {average_waiting_time}")

    


          
if __name__ == '__main__':
  Q = RoundRobinScheduler()
  Q.scheduling()
  no_of_processes = int(input("Enter number of processes: "))

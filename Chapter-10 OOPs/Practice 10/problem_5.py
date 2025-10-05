from random import randint

class train:

    def __init__(self, trainNo):
         self.trainNo = trainNo


    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
         print(f"Train no: {self.trainNo} is running on time")
        

    def getfare(self, fro, to):
          print(f"Ticket is fare in train no: {self.trainNo} from {fro} to {to} is {randint(1, 5666)}")


t = train(12939)
t.book("karachi", "lahore")
t.getfare("karachi", "lahore")
t.getstatus()
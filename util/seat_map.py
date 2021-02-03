import numpy as np


class MyException(Exception):
    pass

class Seats(object):
    
    def __init__(self):
        self.map = np.zeros([10,20])
        self.shape = [10,20]
        self.row = {
            0: "A",
            1: "B",
            2: "C",
            3: "D",
            4: "E",
            5: "F",
            6: "G",
            7: "H",
            8: "I",
            9: "J"
        }
        self.col = {}
        for c in np.arange(1,21):
            self.col[c-1] = str(c)
                        
    # check if the seat is occupied
    def empty(self,row,col):
        return self.map[row,col] == 0
    
    # give number of reservation and assign seats
    # simple method. start from top left corner and put customers in by sequence
    def assign_seats_simple(self, num):
        neighbors = 2
        cur_reservation = []
        if num ==0:
            return cur_reservation
        for i in np.arange(0,self.shape[0],2):
            for j in np.arange(self.shape[1]):
                if self.empty(i,j) :
                    if num < 1 and (neighbors == 0 or j == 0):
                        return cur_reservation
                    elif num < 0:
                        neighbors -= 1
                    self.map[i,j] = 1
                    seat = self.row[i] + str(self.col[j])
                    if num > 0:
                        cur_reservation.append(seat)
                    num -= 1
        if num < 1:
            return cur_reservation
        else:
            raise MyException("Exceeded seating capacity.")  
     
    # give number of reservation and assign seats
    def assign_seats(self, num):
        cur_reservation = []
        ######### wait for implementation #########
        pass
        return cur_reservation
    
    
    
if __name__ == '__main__':
    seats = Seats()
    seats.assign_seats_simple(100)
    print(seats.map)
    
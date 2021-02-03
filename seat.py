#########################
# author: Yi Zhou
# laste edit: 2/2/2021
#########################
import sys
import numpy as np
from util.seat_map import *
import tests


# read entire reservation file and
# parse into lists of reservation indexes and size
def read_file(data):
    with open(data) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    f.close
    index, size = [], []
    for c in content:
        i_s = c.split()
        index.append(i_s[0])
        size.append(i_s[1])
    return index , size

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele + ","
    str1 = str1[:-1]
    return str1

class Cases(object):
    def __init__(self,case, size):
        print('Calculating scenario: ', case)
        if case == 1:
            self.val = self.case1(size)
        if case ==2:
            self.val = self.case2(size)
                
    def case1(self,size):
        reservation = []
        seats = Seats()
        for num in size:
            num = int(num)
            reservation.append(seats.assign_seats_simple(num)) 
        return reservation
    
    def case2(self,size):
        reservation = []
        pass
        ######## Wait for implementation ############
    


def __main__(data, case):
    index , size = read_file(data)
    reservation = Cases(case,size)
    for i,res in enumerate(reservation.val): 
        index[i] += " " + listToString(res)
    outfile = open("out.txt","w")
    for i in index:
        outfile.write("{} \n".format(i))
    outfile.close
    return index
    
    
if __name__ == '__main__':
    try:
        arg = sys.argv[1:]
        __main__(arg[0],int(arg[1]))
    except IndexError:
        print ('Incorrect input arguments')
        sys.exit()
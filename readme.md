# Description

This is a quick project of the movie theater challenge. In this scenario, the question asks to implement an algorithm that fulfils reservation requests and places customers in a theater with 10 by 20 seats. Every reserved group should be separated by 3 seats and/or a row.

Please unzip 'test.zip' for prebuilt test cases.


# Usage

"seat.py" outputs seating assignment.
`python seat.py <case> <num>` 

"seat_test.py" is used to test if the implementation is correct.
`python seat_test.py` 

## Parameters

case: A .txt file. It contains a list of reservation numbers and number of group members.

num: A number. It represents algorithms and implementation methods. 

**For example:** `python seat.py case0.txt 1`  

## Assumption and Implementation

**Assumption**:
	1. First come first serve.
	2. Assuming customers like to sit besides people within the same reservation.
	3. Customers are happy if they are assigned a seat.
	4. Customers don't care where they seat if social distancing is ensured.

**Implementation**: (Using queue)
	1. Start from A1, assign seat A2, A3 ... until seats are assigned to all members in the reservation group.
	2. Space three seats, and assign seats to the next group.
	3. Till the end of the row A, skip one row and assign seats for the next group from C1, to C2, C3 ...
	4. Repeat till all seats are assigned.
	
## Miscellaneous

With different customer satisfaction metric, different algorithm should be implemented.

## Note

Currently, only one algorithm is implemented, i.e. `num = 1`. However, the files are programmed in a flexible way that a novel algorithm can be added easily. 

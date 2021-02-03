import unittest
import sys
import seat 

def read_file(data):
    with open(data) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    f.close
    return content
    
    
class Seat_test(unittest.TestCase):
    
    def test1(self):
        for i in range(5):
            o = "tests/case" + str(i) + ".txt"
            out = seat.__main__(o,1)
            test = "tests/test" + str(i) + ".txt"
            comp = read_file(test)
            self.assertEqual(out,comp)
            
    def test2(self):
        ########## Wait for implementation ########
        pass
        
        
if __name__ == '__main__':
    unittest.main()
import sys

def yeah(list):
    counter_1 = 0
    counter_2 = 1
    while counter_1 < len(list):
        while counter_2 < len(list):
            if list[counter_1] != list[counter_2]:
                counter_2 += 1
            else:
                return True
                # print('True') #little test
                sys.exit(0) #if True, then stop the whole fxn
        counter_1 += 1
        counter_2 = counter_1 + 1
    return False
    # print('False') #little test
    sys.exit(0)

if __name__ == '__main__':
    yeah([1,2,3]) #returns False
    yeah([1,2,3,1,0,10]) #returns True
import util

def record() :
    print("\nTRANSACTION HISTORY : \n")
    if not util.history :
        print("NO TRANSACTIONS DONE YET !!")
    else :
        for _ in util.history :
            print("->", _)
marks = input("enter you marks between 0.0 and 1.0")
marks = float(marks)
if marks >= 0.1 and marks <= 1.0 :
    if marks >= 0.9 :
        print ("A")
    elif marks >= 0.8 :
        print ("B")
    elif marks >= 0.7 :
        print ("C")
    elif marks >= 0.6 :
        print ("D")
    elif marks < 0.6 :
        print ("F")
else :
    print("error")

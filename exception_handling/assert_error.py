try:
    num=int(input("Enter the number:")) 
    assert num > 0 ,"The number is not greater the zero"
except AssertionError:
    print("The number should be greater then Zero")


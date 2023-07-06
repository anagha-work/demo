# filter(function,sequence)
# function checks (True,False)
# return-->retruns in the filter forms(eg.list,set,tuple)
# filter & map not use loops

def check_num(number):
    if(number%2==0):
        return True
    return False

def main():
    print("Enter the element :")
    size = int(input())

    Data_Input=[]
    print("Enter the value :")
    for i in range(0,size):
        value = int(input())
        Data_Input.append(value)
    print("Given list :",Data_Input)

    even_num=filter(check_num,Data_Input)
    #print(even_num)
    #print(type(even_num))
    output=list(even_num)
    print(output)
    output=set(even_num)
    print(output)

if __name__=="__main__":
    main()





def main():
    print("Enter the element :")
    size=int(input())

    lst=[]
    print("Enter the data :")
    
    for i in range(0,size):
        value=int(input())
        lst.append(value)
    print("Given list :",lst)
    even_num=filter(lambda num:num%2==0,lst)
    output=list(even_num)
    print(output)


if __name__=="__main__":
    main()
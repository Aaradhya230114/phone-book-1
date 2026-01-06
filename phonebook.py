import sys
def initial_phonebook():
    rows,cols=int(input("please enter intial number of contacts")),5
    phone_book=[]
    print(phone_book)
    for i in range(rows):
        print("enter contact %d details in the following order only"%(i+1))
        print("note:*indicates mandatory fiels")
        print(".......................................................")
        temp=[]
        for j in range(cols):
            if j==0:
                temp.append(str(input("enter name*:")))
                if temp[j]=="" or temp[j]==" ":
                    sys.exit("name is a mandatory field process exiting due to blank field")
            if j==1:
                 temp.append(int(input("enter number*:")))
            if j==2:
                 temp.append(str(input("enter email address:")))
                 if temp[j]=="" or temp[j]==" ":
                     temp[j]=None
            if j==3:
                 temp.append(str(input("enter Date of birth(dd/mm/yy):")))
                 if temp[j]=="" or temp[j]==" ":
                     temp[j]=None
            if j==4:
                 temp.append(str(input("enter catagory(family/friends/work/others):")))
                 if temp[j]=="" or temp[j]==" ":
                     temp[j]=None
        phone_book.append(temp)
    print(phone_book)
    return phone_book
def menu():
    print("******************************************************")
    print("\t\t\t smart phone directory",flush=False)
    print("\t you can perfforn the following operations on this phone book ")
    print("1.add a new contact")
    print("2.remove an existing contact")
    print("3.delete all contacts")
    print("4.search for  a  contact")
    print("5.diaplay all contacts")
    print("6.exit phone book")
    choice=int(input("please enter your choice:"))
    return choice
def add_contact(pb):
    dip=[]
    for i in range(len(pb[0])):
        if i==0:
            dip.append(str(input("enter name")))
        if i==1:
            dip.append(str(input("enter number")))
        if i==2:
            dip.append(str(input("enter email address")))
        if i==3:
            dip.append(str(input("enter Date of birth(dd/mm/yy): ")))
        if i==4:
            dip.append(str(input("enter catagory(family/friends/work/others) ")))
    pb.append(dip)

    return pb
        
        


                
                     




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
def remove_existing(pb):
    query=str(input("please enter the name of the contact you wish to remove"))
    temp=0
    for i in range(len(pb)):
        if query==pb[i][0]:
            temp+=1
            print(pb.pop(i))
            print("this query has now been removed")
            return pb
    if temp==0:
        print("sorry You have entered an invalid query")
        return pb
def delete_all(pb):
    return pb.clear()
def search_existing(pb):
    choice=int(input("enter search criteria\n\n\n 1.name\n2.number\n3.email id\n4.dob\n5.catagory(Family/friends/work/others)\nplease enter:"))
    temp=[]
    check=-1
    if choice==1:
         query=str(input("please enter the name of the contact you wish to search"))
         for i in range(len(pb)):
             if query==pb[i][0]:
                 check=i
                 temp.append(pb[i])
    elif choice==2:
         query=int(input("please enter the number of the contact you wish to search"))
         for i in range(len(pb)):
             if query==pb[i][1]:
                 check=i
                 temp.append(pb[i])
    elif choice==3:
         query=str(input("please enter the email of the contact you wish to search"))
         for i in range(len(pb)):
             if query==pb[i][2]:
                 check=i
                 temp.append(pb[i])
    elif choice==4:
         query=str(input("please enter the dob (dd/mm//yy) of the contact you wish to search"))
         for i in range(len(pb)):
             if query==pb[i][3]:
                 check=i
                 temp.append(pb[i])
    elif choice==5:
         query=str(input("please enter the catagory of the contact you wish to search"))
         for i in range(len(pb)):
             if query==pb[i][4]:
                 check=i
                 temp.append(pb[i])
    else:
        print(" invalid search")
        return -1
    if check==-1:
        return -1
    else:
        display_all(temp)  
        return check
def display_all(pb):
    if not pb:
        print("list is empty[]") 
    else:
        for i in range(len(pb)):
            print(pb[i])
def thanks():
    print("*****************************************")
    print("thank you for using smart phone directry system > Please visit again")
    print("*****************************************")
    sys.exit("goodbye")
print("................................................")
print("Hello dear ! Welcome to smartphone directry system")
ch=1
pb=initial_phonebook()
while ch in(1,2,3,4,5):
    ch=menu()
    if ch==1:
        pb=add_contact(pb)
    elif ch==2:
        pb=remove_existing(pb)
    elif ch==3:
        pb=delete_all(pb)
    elif ch==4:
        d=search_existing(pb)
        if d==-1:
            print("please try again")
    elif ch==5:
        display_all(pb)
    else:
         thanks()

   

        


    
    


        
        


                
                     




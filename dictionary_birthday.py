birthday={"New Year":"01.01.2016","Fedorifhin":"09.06.2016"}
#print (geek['404'],'\n',geek['Link Rot'])
#print(geek.get('Dancing Baloney','Error'))
choice=None
while choice!="0":
    print (
    """
    0-Exit
    1-Find person
    2-Add person
    3-Edit date or person
    4-Delete person
    5-View all person in list
    """
    )
    choice=input('Your choice: ')
    print()
    #exit
    if choice=="0":
        print("Goodbay!!!")
    #find word
    elif choice=='1':
        term=input("Choise the person for finding in ditionary: ")
        if term in birthday:
            print(birthday[term])
        else:
            print("Sorry,but",term,'is absent in your list')
    elif choice=="2":
        term=input("Enter person for adding to yor list: ")
        if term not in birthday:
            dictionary=input("Enter the birthday date: ")
            birthday[term]=dictionary
        else:
            print("This person is already present in our list, please enter new person or edit date birthday")
    elif choice=="3":
        term=input("Enter person for edit: ")
        if term in birthday:
            dictionary=input("Enter the date of person: ")
            birthday[term]=dictionary
        else:
            print ("Sorry you are wrong! The person",term,"absent in list")
    elif choice=="4":
        term=input("Enter person for delete in list: ")
        if term in birthday:
            del birthday[term]
            print ("The person",term,"delete in list")
        else:
            print ("Sorry you are wrong! The person",term,"absent in list")
    elif choice=="5":
        for key,values in birthday.items():
            print ("*)",key,"-",values)
    else:
        print("Sorry you wrong! Please repeat your choise")

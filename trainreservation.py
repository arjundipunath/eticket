import mysql.connector as c
conc=c.connect(host='localhost',user='root',passwd='8547',database='train_reservation_system')
cr=conc.cursor()

#-------------------------------------------------Functions---------------------------------------------#

#---------------------to add trains------------------------#
def add_train():
        n=int(input("enter the number of trains you want to add: "))
        for i in range(n):
            trainno=int(input("enter the train no: "))
            trainname=input("enter the train name: ")
            departure=input("enter the departure: ")
            intersection=input("enter the intersection: ")
            arrival=input("enter the arrival: ")
            fare=int(input("enter the fare: "))
            t=(trainno,trainname,departure,intersection,arrival,fare)
            q='insert into train_details values(%s,%s,%s,%s,%s,%s)'
            cr.execute(q,t)
            conc.commit()
            print("-----------TRAIN ADDED SUCCESSFULLY---------")


#------------------To display trains--------------------#
            
def display():
        d="select*from train_details"
        cr.execute(d)
        f=cr.fetchall()
        for i in f:
                  print("Trainno:   ", '\t' ,i[0],'\n',"Trainname: ",'\t',i[1] ,'\n',"Departure:  ",'\t',i[2],'\n',"Intersetion:  ",'\t',i[3],'\n',"Arrival: ",'\t\t',i[4],'\n',"Fare",'\t\t',i[5],'\n')
        print("**************************************")



#------------------function to search-------------------#
def search_train():
        trainno1=int(input("enter the train number to be searched: "))
        p='select*from train_details where trainno=%s'
        y=(trainno1,)
        cr.execute(p,y)
        q=cr.fetchall()
        if cr.rowcount==0:
                print("Incorrect Train No")

        else:
                for i in q:
                        print("Trainno:  ", '\t',i[0],'\n',"Trainname:  ", '\t' ,i[1] ,'\n',"Departure:  ", '\t', i[2],'\n',"Intersetion:  ",'\t',i[3],'\n',"Arrival:  ",'\t\t',i[4],'\n',"Fare:",'\t\t',i[5],'\n')
                print("**************************************")
#----------------function to update trian details----------#
def update_train():
        trainno2=int(input("enter the train no to be updated: "))
        d=('Select * from train_details where trainno =%s')
        y=(trainno2,)
        cr.execute(d,y)
        t=cr.fetchall()
        if cr.rowcount==0:
                print("no such train")
        else:
                for i in t:
                        while True:
                                print("1.To change departure")
                                print("2.To change intersection")
                                print("3.To change arrival")
                                print("4.To change Fare")
                                print("5.To show the updated table")
                                print("6. Nothing more to update")
                                ch=int(input("enter your choice: "))
                                if ch==1:
                                        dep=input("enter the new departure: ")
                                        q='update train_details set Departure=%s where trainno=%s'
                                        t=(dep,trainno2)
                                        cr.execute(q,t)
                                        conc.commit()
                                elif ch==2:
                                        inter=input("Enter the new interesection: ")
                                        q='update train_details set Intersection=%s where trainno=%s'
                                        t=(inter,trainno2)
                                        cr.execute(q,t)
                                        conc.commit()
                                elif ch==3:
                                        arr=input("Enter the new arrival: ")
                                        q='update train_details set arrival=%s where trainno=%s'
                                        t=(arr,trainno2)
                                        cr.execute(q,t)
                                        conc.commit()
                                elif ch==4:
                                        fare=input("Enter the new Fare: ")
                                        q='update train_details set fare=%s where trainno=%s'
                                        t=(fare,trainno2)
                                        cr.execute(q,t)
                                        conc.commit()
                                elif ch==5:
                                       s='select * from train_details'
                                       c=cr.execute(s,)
                                       d=cr.fetchall()
                                       for i in d:
                                               print("Trainno:   ",'\t',i[0],'\n',"Trainname: ",'\t',i[1] ,'\n',"Departure: ",'\t',i[2],'\n',"Intersetion: ",'\t',i[3],'\n',"Arrival: ",'\t\t',i[4],'\n',"Fare: ",'\t\t',i[5],'\n')
                                                
                                     
                                elif ch==6:
                                        break
                                        print('*********UPDATED**********')
                                        
                                else:
                                        print("wrong choice")

          


def delete_trains():
        trainno3=int(input("Enter the train no to be deleted:"))
        q='delete from train_details where trainno=%s'
        t=(trainno3,)
        cr.execute(q,t)
        conc.commit()
        print("*****deleted*****")


#**************************************************************************#

#-----------------------------------USER PORTAL----------------------------------------#

#def user_portal:


def booking_ticket():
#---------to enter user details-----------#
        n=int(input("enter the number of tickets you want to book: "))
        print('!!!!!!NOTE you should enter trainno from above listed only!!!!!!!!!')
        for i in range(n):
                import random
                user_id=random.randrange(500,1000)
                user_name=input("enter the username: ")
                Trainno=int(input("enter the trainNo: "))
                Dat_of_jour=input("enter the date of journey:  ")
                Departure=input("enter the place of departure: ")
                Arrival=input("enter the place of arrival: ")
                t=(user_id,user_name,Trainno,Dat_of_jour,Departure,Arrival)
                q='insert into user_details values(%s,%s,%s,%s,%s,%s)'
                cr.execute(q,t)
                q1=('select fare from train_details where trainno=%s')
                t1=(Trainno,)
                cr.execute(q1,t1)
                f=cr.fetchone()
                conc.commit()
                summ=n*f[0]
                print('--------------============================------------------------------')
                print('-------------****** INDIAN RAILWAY ******----------')
                print('------------------------------------------------------------------------------------')
                print("Train Number: ",Trainno)
                print("User Id: ",user_id)
                print("------------------------------------")
                print("username",'\t',"Date of Journey",'\t\t','Departure','\t','Arrival')
                print('-----------------------------------------------------------------------------------------------------')
                print(user_name,'\t\t',Dat_of_jour,'\t\t',Departure,'\t',Arrival)
                print('-----------------------------------------------------------------------------------------------------')
                print('Amount ₹',f[0])
                print('-----------------------------------------------------------------------------------------------------')
        print('Total amount is ===  ₹    ',summ)
        print('-----------------------================================--------------------------')
                


#-----------------------------------------------------------------------------------#
def search_details():
        t=int(input("enter the user id: "))
        p=('select * from user_details where user_id=%s')
        y=(t,)
        cr.execute(p,y)
        m=cr.fetchall()
        if cr.rowcount==0:
                       print("!!!!!  incorrect user id  !!!!!!")
                
        
        else:
                for i in m:
                        print("user_id: ",i[0],'\n',"user_name: ",i[1],"\n","train_no: ",i[2],"\n","dat_of_jour: ",i[3],"\n","departure: ",i[4],"\n","arrival: ",i[5])
                       


#--------------------------------------------------------------------------#
def delete_ticket():
    tno1=(input('Enter User id To Cancel The Ticket'))
    q=('delete from user_details where user_id=%s')
    t=(tno1,)
    cr.execute(q,t)
    conc.commit()
    if cr.rowcount==0:
            print("!!!!!  incorrect user id  !!!!!!")
    else:
            print('*****DELETED SUCESSFULLY*****')



 #=======================================================================================#   
#---------------ADMIN PORTAL---------------#
def admin_portal():
           while True:
            print('1:To add train')
            print('2:To display train details')
            print('3:To Search for a Particular Train')
            print('4:To update Train details')
            print('5:To delete train details')
            print('6:To Exit from admin Portal')
            ch=int(input('Enter Your Choice:    '))
            if ch==1:
                    add_train()
            elif ch==2:
                    display()
            elif ch==3:
                    search_train()
            elif ch==4:
                     update_train()
            elif ch==5:
                     delete_trains()
            elif ch==6:
                     print("---------------THANKYOU VISIT AGAIN----------------")
                     break
            else:
                    print("INVALID CHOICE")

def usr_func():
    while True:
            print('1:To Book Ticket')
            print('2:To Search for a Particular Ticket')
            print('3:To Cancel a Ticket Record')
            print('4:To Exit from User Portal')
            ch=int(input('Enter Your Choice:   '))
            if ch==1:
                s='select * from train_details'
                c=cr.execute(s,)
                d=cr.fetchall()
                for i in d:
                      print("Trainno:   ",'\t',i[0],'\n',"Trainname:   ",'\t' ,i[1] ,'\n',"Departure:  ",'\t',i[2],'\n',"Intersetion",'\t',i[3],'\n',"Arrival:  ",'\t\t',i[4],'\n',"Fare",'\t\t',i[5],'\n')
                booking_ticket()
            elif ch==2:
                search_details()
            elif ch==3:
                    delete_ticket()
            elif ch==4:
                print('**********THANKYOU VISIT AGAIN**********')
                break
            else:
                print('Invalid Choice')


#---------------------------------------------MAIN PROGRAM---------------------------------------------------#
while True:
    print('***********WELCOME TO ETICKETS***********')
    print('1:Admin Portal')
    print('2:User Portal')
    print('3:Exit the appilcation')
    ch = int(input('enter your choice:   '))
    if ch == 1:
        n = input('enter Admin id:  ')
        pa= int(input('enter pin:  '))
        if pa == 1234:
                admin_portal()
            
        else:
            print('incorrect pin')
    elif ch == 2:
        usr_func()
    elif ch == 3:
        print('***********THANK YOU FOR VISITING************')
        break
    else:
        print('invalid choice')



class to_dolist:
    list=[]    
    def add_list(self,task):
        print(task)
        self.list.append(task)

    def display_list(self):
        print(self.list)
        
        
    def remove_list(self, task):
        self.list.remove(task)

    
to_dolist=to_dolist()



while True:
    print("********************************")
    print ("1.add to_do")
    print("2.display to_do")
    print("3.delete to_do")
    print("4.exit to_do")
    print("********************************")

    a=int(input("ENTER THE CHOICE  "))
    if a==1:
      task=input("ENTER THE TASK  :")
      to_dolist.add_list(task)

      
    elif a==2:
     to_dolist.display_list()


    elif a==3:
       c=input("ENTER THE TASK TO DELETE   :")
       to_dolist.remove_list(c)

       
    elif a==4:
     print("THANK YOU")
     break
    
    else:
       print("WRONG CHOICE  ,ENTER THE ABOVE CHOICES:  ")

       







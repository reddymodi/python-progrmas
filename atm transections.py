username = "kesava"
password = "reddy123"
enter_user = input("enter your user name:")
enter_pass= input("enter your password:")
if enter_user == username and enter_pass==password:
    print('''
1.deposite
2.withdraw
3.ministatement
4.exit
''')
             
    option = int(input("enter your option:"))
    amount = 20000
    if option == 1:
        dep = int(input("enter yor depositeamount:"))
        amount += dep
        print("your amount is ",amount)
    elif option == 2:
        withd = int(input("enter your withdraw amount:"))
        amount -= withd
        print("your cuurrent balance is:",amount)
    elif option == 3:
        print("+++++ATAM++++")
        print("username:",username)
        print("last deposite:",dep)
        print("last withdraw:",withd)
        print("cuurent balance:",amount)
        print("thank you for visisting")
        print("========ATM==========")
    elif option == 4:
        print("exit")
else:
    print("enter your correct loginns")
    
        

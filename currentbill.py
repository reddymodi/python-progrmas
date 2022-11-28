bill_no = input("enter your bill no:")
un1= int(input("enter the units first no:"))
un2 = int(input("enter the units ending no:"))
cu = un2-un1
total = 0
if cu <= 300:
    total = cu * 3.50
elif 301 >= cu <= 500:
    total = cu * 4.50
else:
    total = cu * 5.50
print(bill_no,"is total used units is",cu,"total bill is",total)
    
    
    

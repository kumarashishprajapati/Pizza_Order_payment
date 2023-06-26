print('''
---- Pizza Shop Request Order ----

1.Small Pizza  - 200 RS 
2.Medium Pizza  - 300 RS
3.Large Pizza  - 400 RS

''')

order=int(input("Enter Your Pizza Order No. [1,2,3] - "))

print('''---  Additive Ingridents ---
           1. pepprion pizza (50 Rs) + your order no. 
           2. paneer pizza (100 Rs) + your order no.
           3. extra cheeze(150 Rs) + your order no.
''')
add=int(input("Enter Your Additive Item No. [1,2,3] - "))
img=('static/paytm.png')

bill=0
if order ==1:
    if add==1:
        bill+=200 + 50
        print(f"YOur Total is {bill} Scan QR-Code for Payment {img}")
    elif add==2:
        bill+=200 + 100
        print(f"Your Total is  {bill}  Scan QR-Code for Payment {img}")    
    elif add==3:
        bill+=200 +150
        print(f" Your Total Order is  {bill}  Scan QR-Code for Payment {img}")
elif order == 2:
    if add==1:
        bill+=300 + 50
        print(f"YOur Total is {bill}  Scan QR-Code for Payment {img}")
    elif add==2:
        bill+=300 + 100
        print(f"YOur Total is {bill}  Scan QR-Code for Payment {img}")
    elif add==3:
        bill+=300 + 150
        print(f"YOur Total is {bill}  Scan QR-Code for Payment {img}")

elif order ==3:
    if add==1:
        bill+=400 + 50
        print(f"YOur Total is {bill}  Scan QR-Code for Payment {img}")
    elif add==2:
        bill+=400 + 100
        print(f"YOur Total is {bill}  Scan QR-Code for Payment {img}")
    elif add==3:
        bill+=400 + 150
        print(f"YOur Total is {bill}  Scan QR-Code for Payment {img}")
else:
    print("--Invalid Detail--!")
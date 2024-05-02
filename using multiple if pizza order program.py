# pizza order program
size = input("enter size of pizza S/M/L:")
bill =0
if size =='S' or size =='s':
    bill = bill +100
    print("small size pizza is 100 rs")
elif size =='M' or size =='m':
    bill = bill +200
    print("medium size pizza is 200 rs")
else:
    bill = bill + 300
    print("large size pizza is 300 rs")

pepporoni = input("you want pepporoni yes/no:")
if pepporoni =='yes' or pepporoni =='YES':
   if size =='s' or size =='S':
      bill = bill + 30
   elif size =='M' or size =='m':
       bill = bill + 40
   else:
       bill= bill + 50
cheese = input("you want cheese y/n:")
if cheese == 'yes' or cheese == 'YES':
    bill = bill +20
print(f"total bill is {bill}")

      

    


  
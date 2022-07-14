height = int(input("enter your height: "))
if height>120:
  print("you can ride")
  age=int(input("enter your age plz: "))
  wantPhoto=input("whould you like to take a photo? Y or N : ")
  if age<=12:
    pill=5
    if(wantPhoto=='Y'):
      pill+=3
    print(f"child have to pay ${pill} ")
  elif age<=18:
    pill=7
    if(wantPhoto=='Y'):
      pill+=3
    print(f"teenagers have to pay ${pill}")
  elif age>=44 and age<=45 :
    pill=0
    if(wantPhoto=='Y'):
      pill+=3
      print(f" you get a free ticket your bill: ${pill}")
    
  else:
    pill=12
    if(wantPhoto=='Y'):
      pill+=3
    print(f"adults have to pay ${pill}")
else:
  print("you can't ride")


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# name1_lower=name1.lower()
# name2_lower=name2.lower()
# countT=name1_lower.count('t')+name2_lower.count('t')
# countR=name1_lower.count('r')+name2_lower.count('r')
# countU=name1_lower.count('u')+name2_lower.count('u')
# countE=name1_lower.count('e')+name2_lower.count('e')
# countTrue=countT+countR+countU+countE
# countL=name1_lower.count('l')+name2_lower.count('l')
# countO=name1_lower.count('o')+name2_lower.count('o')
# countV=name1_lower.count('v')+name2_lower.count('v')
# countLove=countL+countO+countV+countE
# loveScore=countTrue*10+countLove
name=name1+name2
nameLowerCase=name.lower()
t=nameLowerCase.count('t')
r=nameLowerCase.count('r')
u=nameLowerCase.count('u')
e=nameLowerCase.count('e')
l=nameLowerCase.count('l')
o=nameLowerCase.count('o')
v=nameLowerCase.count('v')
true=t+r+u+e
love=l+o+v+e
loveScore=int(str(true)+str(love))

if loveScore<10 or loveScore>90:
  print(f"Your score is %{loveScore}, you go together like coke and mentos.")
elif loveScore>=40 and loveScore<=50 :
  print(f"Your score is %{loveScore}, you are alright together.")
else:
  print(f"Your score is %{loveScore}")
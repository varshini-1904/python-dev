import re as Regex
username=input("Enter your user name")
print(Regex.fullmatch('[\w_-]*',username))


name=input("Enter your name")
print(Regex.fullmatch('[\w ]*',name))

email=input("Enter your email")
print(Regex.fullmatch('[\w_-]*@{1}(gmail|yahoo|outlook).com{1}',email))

password=input("Enter your password")
print(Regex.fullmatch('[\d@#_-]{9,15}',password))

mobilenumber=input("Enter your mobile no")
print(Regex.fullmatch('[\d{10}]*',mobilenumber))

gender=input("Enter your gender ")
print(Regex.fullmatch('Female|Male|Others',gender))



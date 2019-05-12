import random

s = "abcdefghiklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
len_password = int(input("enter number of letters in password:"))

password ="".join(random.sample(s,len_password))
print(password)

#answer =input("like to keep pasword: ")
#if("yes" in answer):
 #   account_name = input("enter name of account: ")

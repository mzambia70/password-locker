import random
import pickle

info = {}

with open("pass-display.mz","br") as readfile:
    info = pickle.load(readfile)


s = "abcdefghiklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
len_password = int(input("enter number of letters in password:"))

password ="".join(random.sample(s,len_password))
print(password)

answer =input("like to keep pasword: ")
if("yes" in answer):
    account_name = input("enter name of account: ")
    info[account_name] = password
    with open("pass-display.mz","bw") as filewrite:
        pickle.dump(info,filewrite, protocol=2)



else:
    account_name = input("enter account name: ")
    password = input("enter password: ")
    info[account_name] = password
    with open("pass-display.mz","bw") as filewrite:
        pickle.dump(info,filewrite, protocol=2)
    

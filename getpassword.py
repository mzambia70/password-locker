import pickle
import pyperclip

m_password = input("enter master password: ")

if (m_password == "elchapo"):
     account_name = input("enter account name: ")
     with open("pass-display.mz","br") as readfile:
         info = pickle.load(readfile)

     if account_name in info:
         pyperclip.copy(info[account_name])
         print("password copied")

     else:
         print("password not found")

else:
    print("password doesn't match")
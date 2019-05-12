import pickle

m_password = input("enter master password: ")

if (m_password == "elchapo"):
     account_name = input("enter account name: ")
     with open("pass-display.mz","br") as readfile:
         info = pickle.load(readfile)

     if account_name in info:
         print("password =",info[account_name])
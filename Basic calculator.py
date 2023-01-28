#!/usr/bin/env python
# coding: utf-8

# In[2]:


def calculator():
    while True:
        print("Select operation.")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = int(input("Enter choice(1/2/3/4/5):"))
        
        if choice in [1,2,3,4]:
            n1 = float(input("Enter your first number: "))
            n2 = float(input("Enter your second number: "))
        
            if choice == 1:
                print(n1 + n2)
            elif choice == 2:
                print(n1 - n2)
            elif choice == 3:
                print(n1 * n2)
            elif choice == 4:
                if n2==0:
                    print("Division by zero is not supported")
                else:
                    print(n1 / n2)
        elif choice == 5:
            break
        else:
            print("Invalid Input")

calculator()


# In[ ]:





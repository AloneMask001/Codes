#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random 

loop = 0;
random_number = random.randint(1,100) #Get number from program to guess

while loop < 10:
    try:
        Guess_number = int(input("Guess a number between 1 and 100: "))
    except ValueError:  # For non-int characther
        print("Please enter a valid integer.")
        continue
        
    if random_number == Guess_number:
        print(f"Congratulations! You guessed the {random_number} in {loop + 1} attempts!")
        break
    else:
        if random_number > Guess_number:
            print("Its too low!")
        else:
            print("Its too high!")
        loop +=1
        
if random_number != Guess_number:
        print(f"Sorry, you've run out of attempts. The number was {random_number}.")
                
                   


# In[ ]:





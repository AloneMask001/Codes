"""
Restaurant simulator.
"""
#libraries
import random
                                    
#restaurant area info.
restaurant_area = [
    [" ", " ", " "," ", " ", " "],
    [" ", " ", " "," ", " ", " "],
    [" ", " ", " "," ", " ", " "],
    [" ", " ", " "," ", " ", " "] 
]
#table info.
#konum-kişi sayısı-boş
table_location = [
    [[0, 1],2, 1],  
    [[3, 5],3, 1],  
    [[2, 2],3, 1],  
    [[3, 1],4, 1],  
    [[2, 4],4, 1],  
    [[1, 5],6, 1]   
]

#Number counts.
customer_count = 0
table_count = 6
bill = 0

#food info.
pre_main = ["mushroom soup","lentil soup","tarhana soup","ezo bright soup"]
side_dish = ["french fried","smash patateos","rice","salad"]
main_dish = ["Beff","Doner","Chicken","Fish"]
drinks = ["Coke", "Fanta", "Water", "Lemonade", "Ayran"]

#Price info.
menu = {
    "Mushroom Soup": 7.99,
    "Lentil Soup": 5.49,
    "Tarhana Soup": 6.29,
    "EzoGelin Soup": 8.49,
    "French Fries": 3.99,
    "Smash Potatoes": 4.49,
    "Rice": 2.99,
    "Salad": 4.79,
    "Beef": 15.99,
    "Doner": 12.49,
    "Chicken": 10.99,
    "Fish": 14.49,
    "Coke": 2.49,
    "Fanta": 2.49,
    "Water": 1.49,
    "Lemonade": 3.29,
    "Ayran": 2.19
}
customer_dishes_choice = []

#random waiter chooser. -- #waiter will be avaliable if the customer leaves. 
waiter_list = ["Emine", "Rümeysa", "Nilgün", "Nilüfer", "Atilla", "Erdem","Semih"]
random_waiter_chooser = random.choice(waiter_list)
#greetings to customer info.
print()
if __name__ == "__main__":
    print(f"Hello and welcome to the Los Pollos Hermanos family my name is: {random_waiter_chooser} how can i help you?\n")
    
try:
    customer_choice = int(input("If you are looking for empty table press [1] - If you are looking for menu press [2]\n answer: "))
    print()
    if (customer_choice == 1):
        #For how many people.
        customer_number = int(input("How many people will you be?(2,3,4,6): "))
        if (customer_number  == 5 or customer_number <= 1 or customer_number > 6):
            print(f"Sorry say that we dont have table for {customer_number}")
        else:
            for table in table_location:
                location,capacity,status = table
                if (status == 1 and capacity == customer_number):
                    table[2] = 0
                    waiter_list.remove(random_waiter_chooser)
                    customer_count += 1
                    table_count -= 1
                    print(f"{customer_number} kişilik masa bulundu! Konum: {location}")
                    n = 0
                    while n < 1: 
                        user_input = input("Menüyü görmek ister misiniz(1,0): ")
                        if user_input == '1':
                            n += 1
                            print(f"{'Dishes':<20} {'menu ($)':>10}")
                            print("-" * 30)
                            for dish, price in menu.items():
                                print(f"{dish:<10} \t\t {price:<1}") 
                                
                            for kişi in range(1,customer_number + 1):
                                while(True):
                                    dishes_choice = str(input(f" Kişi {kişi} ,İstediğiniz yemeği giriniz: "))
                                    if dishes_choice in menu:
                                        fiyat = float(menu[dishes_choice])
                                        bill += fiyat
                                        print(f" {dishes_choice} seçildi.")
                                        break
                                    else:
                                        print("Menüde olmayan bir yemek seçtiniz. Lütfen geçerli bir yemek girin.")
                            print(f"Toplam Fatura: {bill:.2f} USD")

                        elif user_input == 0: 
                            pass
                        break                                                    
                

    elif (customer_choice == 2):
        print(f"{'Dishes':<20} {'Menu ($)':>10}")
        # :<20 sola :> sağa yaslamaya olanak verir soldan 20 yer açtıya sola da 10 açar ve oraya hizzalar.
        print("-" * 30)
        for dish, price in menu.items():
            print(f"{dish:<10} \t\t {price:<1}")
        pass
    
    else:
        print("Please choose a number between 1 and 2.")

except ValueError:
    print("Please use valid answer")
except Exception as e:
    print(f"Something went wrong! {e}")

# En yakın zamanda dönmen dileğiyle verep ben kaçar :) kendini çok sev tamam mı ::::::::)




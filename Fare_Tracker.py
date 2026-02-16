### Fare Tracker Program

fares = []                                                 #array to store fares

budget = float(input("Enter your weekly transportation budget: ₱"))         # Ask for the weekly transportation budget of user

while True:
    print("\n===== FARE TRACKER =====")                # Program Menu 
    print("1 - Add Fare")                             # OPTION 1
    print("2 - View Fares")                           # OPTION 2
    print("3 - Total Spent")                          # OPTION 3
    print("4 - Exit")                                 # OPTION 4           
    print("========================")                  
    
    choice = input("Choose option: ")                      # Allows the user to choose option

    ## Add a fare
    if choice == "1":                                                                              #_OPTION 1_
        date = input("Enter date (YYYY-MM-DD): ")                                                  #Date
        transport = input("Transport (Choose here: Jeep, Bus, Tricycle, Train, Taxi): ")           #Transportation used         
        amount = float(input("Fare amount: ₱"))                                                    #Amount of fare
        fares.append([date, transport, amount])                                                    #Save fare record to the list of fares
        print("Fare added!")                                                                       #Confirm 

        print("\nFare Added Successfully!")                                                        #RECEIPT-OUTPUT STYLE
        print("-------------------------")
        print(f"Date: {date}")
        print(f"Transport: {transport}")
        print(f"Amount: ₱{amount:.2f}")
        print("-------------------------")
        
        total = sum(f[2] for f in fares)                                        #Goes through all the fare amounts and adds up all those amounts 
        if total > budget:                                                      #If the sum is greater than the budget allocated.....
            print("⚠ Warning: You exceeded your weekly transportation budget!") #It gives you warning that you exceeded the budget

    ## View all fares
    elif choice == "2":                                                        #_OPTION 2_
        if len(fares) == 0:                                                    #Checks if list is empty
            print("No fares yet.")                                             #If not...
        else:                                                                  #Prints inputted date, transport, and amount for each record.
            print("\nDate      |    Transport   |   Amount")
            for f in fares:
                print(f"{f[0]} | {f[1]} | ₱{f[2]:.2f}")

            transport_totals = {}                                              #Show total per transport type
            for f in fares:
                if f[1] in transport_totals:
                    transport_totals[f[1]] += f[2]
                else:
                    transport_totals[f[1]] = f[2]
            print("\nTotal per transport type:")
            for t, amt in transport_totals.items():
                print(f"{t}: ₱{amt:.2f}")

    # Show total spent
    elif choice == "3":                                                        #_OPTION 3_
       total = sum(f[2] for f in fares)                                        #Goes through all the fare amounts and adds up all those amounts
       print(f"\nTotal spent: ₱{total:.2f}")                                   
        if total > budget:                                                      #If the sum is greater than the budget allocated.....
            print("⚠ Warning: You exceeded your weekly transportation budget!") #It gives you warning that you exceeded the budget
            
    # Exit program
    elif choice == "4":                                                        #_OPTION 4_
        print("Goodbye!")                                                      #Exit the program
        break

    else:
        print("Invalid option.")                                               #Else; invalid option


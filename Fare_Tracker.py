## Fare Tracker Program

fares = []                                                 #array to store fares

while True:
    print("\n1 - Add Fare")                                #OPTION 1              
    print("2 - View Fares")                                #OPTION 2
    print("3 - Total Spent")                               #OPTION 3
    print("4 - Exit")                                      #OPTION 4
    
    choice = input("Choose option: ")                      # Allows the user to choose option

    # Add a fare
    if choice == "1":                                                          #OPTION 1
        date = input("Enter date (YYYY-MM-DD): ")                              #Date
        transport = input("Transport (jeep, bus, tricycle, etc.): ")           #Transportation used         
        amount = float(input("Fare amount: ₱"))                                #Amount of fare
        fares.append([date, transport, amount])                                #Save fare record to the list of fares
        print("Fare added!")                                                   #Confirm 

    # View all fares
    elif choice == "2":                                                        #OPTION 2
        if len(fares) == 0:                                                    #Checks if list is empty
            print("No fares yet.")                                             #If not...
        else:                                                                  #Prints date, transport, and amount for each record.
            print("\nDate      |    Transport   |   Amount")
            for f in fares:
                print(f"{f[0]} | {f[1]} | ₱{f[2]:.2f}")

    # Show total spent
    elif choice == "3":                                                        #OPTION 3
        total = 0
        for f in fares:
            total += f[2]                                                      #Add amount of current fair to total
        print(f"\nTotal spent: ₱{total:.2f}")                                  #Display the result/total

    # Exit program
    elif choice == "4":                                                        #OPTION 4
        print("Goodbye!")                                                      #Exit the program
        break

    else:
        print("Invalid option.")                                               #Else; invalid option

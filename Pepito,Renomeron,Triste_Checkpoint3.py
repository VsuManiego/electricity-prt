#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Calculates the total electricity consumption cost for all appliances owned by the consumer per day, month, and year
print("This program calculates the residential electricity bill per day, month and year.")
print( )
print('Choose between the following appliances: Television, Electric Fan, Refrigerator, Water Heater, Light Bulb')
print( )
appliances = ["Television", "Electric Fan", "Refrigerator", "Water Heater", "Microwave Oven", "Lamp Shade", "Amplifier", "Radio", "Electric Stove","Flourescent Lamp","Total" ]           #different type of appliances owned by the consumer


while True:                                                           #while loop
    


        appliances = input("Enter the appliance: ", )                       #if statement to end loop     
        time_string = input("Enter the hours of usage per day:")                #the average hours of the typical appliance you used in a day
        time = float(time_string)                                                  #the residential rate per kilowatt hour in pesos
        cost = 6.8753                                                       #the fixed residential rate per kilowatt hour in pesos
        
        if appliances == "Television":
            
            while True:
                
                print( )
                answer = input('Do you know the wattage of your television? Yes or No? ', )
                print( )
                
                if answer == 'Yes':
                        tvwc = int(input('Enter the wattage in watts here: '))
                        tvkwc = tvwc*0.001
                        print( )
                        n_string = input("How many televisions of that wattage do you have?: ")
                        n = float(n_string)
                        sum = 0
                        tvdayc = n*tvkwc*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
                        tvmonthc = tvdayc*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
                        tvyearc = tvmonthc*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
                        
                        print("Your television has "+str(tvdayc)+" electricity cost per day in pesos.")
                        print("Your television has "+str(tvmonthc)+" electricity cost per month in pesos.")
                        print("Your television has "+str(tvyearc)+" electricity cost per year in pesos.")
                        print( )
                        
                        break
                        
                if answer == 'No':
                        
                        print("An average television runs on 117 watts of energy.")
                        print( )
                        n_string = input("How many televisions do you have?: ")
                        n = float(n_string)
                        sum = 0
                        tvkwf_string = 0.117                                                   #the fixed electrical power consumption of the typical appliance
                        tvkwf = float(tvkwf_string)                                              #the appliances owned by the consumer
                        tvdayf = n*tvkwf*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
                        tvmonthf = tvdayf*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
                        tvyearf = tvmonthf*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
            
                        print("Your television has "+str(tvdayf)+" electricity cost per day in pesos.")
                        print("Your television has "+str(tvmonthf)+" electricity cost per month in pesos.")
                        print("Your television has "+str(tvyearf)+" electricity cost per year in pesos.")
                        print( )
                        
                        break

             
        if appliances == "Electric Fan":
            
            while True:
                
                print( )
                answer = input('Do you know the wattage of your electric fan? Yes or No? ', )
                print( )
                
                if answer == 'Yes':
                        efanwc = int(input('Enter the wattage in watts here: '))
                        efankwc = efanwc*0.001
                        print( )
                        n_string = input("How many electric fans of that wattage do you have?: ")
                        n = float(n_string)
                        sum = 0
                        efandayc = n*efankwc*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
                        efanmonthc = efandayc*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
                        efanyearc = efanmonthc*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
                        
                        print("Your electric fan has "+str(efandayc)+" electricity cost per day in pesos.")
                        print("Your electric fan has "+str(efanmonthc)+" electricity cost per month in pesos.")
                        print("Your electric fan has "+str(efanyearc)+" electricity cost per year in pesos.")
                        print( )
                        
                        break
                        
                if answer == 'No':
                        
                        print("An average electric fan runs on 64.28 watts of energy.")
                        print( )
                        n_string = input("How many electric fans do you have?: ")
                        n = float(n_string)
                        sum = 0
                        efankwf_string = 0.06428                                                   #the fixed electrical power consumption of the typical appliance
                        efankwf = float(efankwf_string)                                              #the appliances owned by the consumer
                        efandayf = n*efankwf*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
                        efanmonthf = efandayf*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
                        efanyearf = efanmonthf*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
            
                        print("Your electric fan has "+str(efandayf)+" electricity cost per day in pesos.")
                        print("Your electric fan has "+str(efanmonthf)+" electricity cost per month in pesos.")
                        print("Your electric fan has "+str(efanyearf)+" electricity cost per year in pesos.")
                        print( )
                        
                        break


        if appliances == "Refrigerator":
            
            while True:
                
                print( )
                answer = input('Do you know the wattage of your refrigerator? Yes or No? ', )
                print( )
                
                if answer == 'Yes':
                        refwc = int(input('Enter the wattage in watts here: '))
                        refkwc = refwc*0.001
                        print( )
                        n_string = input("How many refrigerators of that wattage do you have?: ")
                        n = float(n_string)
                        sum = 0
                        refdayc = n*refkwc*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
                        refmonthc = refdayc*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
                        refyearc = refmonthc*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
                        
                        print("Your refrigerator has "+str(refdayc)+" electricity cost per day in pesos.")
                        print("Your refrigerator has "+str(refmonthc)+" electricity cost per month in pesos.")
                        print("Your refrigerator has "+str(refyearc)+" electricity cost per year in pesos.")
                        print( )
                        
                        break
                        
                if answer == 'No':
                        
                        print("An average refrigerator runs on 100 watts of energy.")
                        print( )
                        n_string = input("How many refrigerators do you have?: ")
                        n = float(n_string)
                        sum = 0
                        refkwf_string = 0.1                                                   #the fixed electrical power consumption of the typical appliance
                        refkwf = float(refkwf_string)                                              #the appliances owned by the consumer
                        refdayf = n*refkwf*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
                        refmonthf = refdayf*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
                        refyearf = refmonthf*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
            
                        print("Your refrigerator has "+str(refdayf)+" electricity cost per day in pesos.")
                        print("Your refrigerator has "+str(refmonthf)+" electricity cost per month in pesos.")
                        print("Your refrigerator has "+str(refyearf)+" electricity cost per year in pesos.")
                        print( )
                        
                        break

            
        if appliances == "Water Heater":
            
            while True:
                
                print( )
                answer = input('Do you know the wattage of your water heater? Yes or No? ', )
                print( )
                
                if answer == 'Yes':
                        heatwc = int(input('Enter the wattage in watts here: '))
                        heatkwc = heatwc*0.001
                        print( )
                        n_string = input("How many water heaters of that wattage do you have?: ")
                        n = float(n_string)
                        sum = 0
                        heatdayc = n*heatkwc*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
                        heatmonthc = heatdayc*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
                        heatyearc = heatmonthc*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
                        
                        print("Your water heater has "+str(heatdayc)+" electricity cost per day in pesos.")
                        print("Your water heater has "+str(heatmonthc)+" electricity cost per month in pesos.")
                        print("Your water heater has "+str(heatyearc)+" electricity cost per year in pesos.")
                        print( )
                        
                        break
                        
                if answer == 'No':
                        
                        print("An average water heater runs on 1125 watts of energy.")
                        print( )
                        n_string = input("How many water heaters do you have?: ")
                        n = float(n_string)
                        sum = 0
                        heatkwf_string = 1.125                                                   #the fixed electrical power consumption of the typical appliance
                        heatkwf = float(heatkwf_string)                                              #the appliances owned by the consumer
                        heatdayf = n*heatkwf*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
                        heatmonthf = heatdayf*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
                        heatyearf = heatmonthf*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
            
                        print("Your water heater has "+str(heatdayf)+" electricity cost per day in pesos.")
                        print("Your water heater has "+str(heatmonthf)+" electricity cost per month in pesos.")
                        print("Your water heater has "+str(heatyearf)+" electricity cost per year in pesos.")
                        print( )
                        
                        break

            
        if appliances == "Light Bulb":
            print( )
            bulbw = int(input("How many watts does the bulb use?: "))
            print( )
            bulbkw = bulbw*0.001
            
            n_string = input("How many bulbs of that wattage do you have?: ")
            print( )
            n = float(n_string)
            bulbday = n*bulbkw*time*cost
            bulbmonth = bulbday*30
            bulbyear = bulbmonth*12
            
            print("The appliance has "+str(bulbday)+" electricity cost per day in pesos.")
            print("The appliance has "+str(bulbmonth)+" electricity cost per month in pesos.")
            print("The appliance has "+str(bulbyear)+" electricity cost per year in pesos.")
            print( )
        
sum = sum+E                                                      #the formula used to get the total cost of all the appliances consumption cost rated per day in pesos
E3 = sum*30                                                          #the formula used to get the total cost of all the appliances consumption cost rated per month in pesos
E4 = E3*12                                                           #the formula used to get the total cost of all the appliances consumption cost rated per year in pesos

print("The total power consumption costs "+str(sum)+" pesos per day.")
print("The total power consumption costs "+str(E3)+" pesos per month.")
print("The total power consumption costs "+str(E4)+" pesos per year.")


# In[ ]:





# In[ ]:





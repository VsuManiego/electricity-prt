#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Calculates the total electricity consumption cost for all appliances owned by the consumer per day, month, and year
print("This program calculates the residential electricity bill per day, month and year.")
print( )

appliances = ["Television", "Electric Fan", "Refrigerator", "Water Heater", "Microwave Oven", "Lamp Shade", "Amplifier", "Radio", "Electric Stove","Flourescent Lamp","Total" ]           #different type of appliances owned by the consumer


while True:                                                           #while loop
    


        appliances = input("Enter the appliances: ", )                       #if statement to end loop     
        time_string = input("Enter the hours of usage per day:")                #the average hours of the typical appliance you used in a day
        time = float(time_string)                                                  #the residential rate per kilowatt hour in pesos
        cost = 6.8753                                                       #the fixed residential rate per kilowatt hour in pesos
        
        if appliances == "Television":
            print("The fixed kilowatts: 100 ")
            n_string = input("How many televisions do you have?: ")
            n = float(n_string)
            sum = 0
            tvkwhr_string = 100                                                   #the fixed electrical power consumption of the typical appliance
            tvkwhr = float(tvkwhr_string)                                              #the appliances owned by the consumer
            tvday = n*tvkwhr*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
            tvmonth = tvday*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
            tvyear = tvmonth*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos

            print( )
            print("The appliance has "+str(tvday)+" electricity cost per day in pesos.")
            print("The appliance has "+str(tvmonth)+" electricity cost per month in pesos.")
            print("The appliance has "+str(tvyear)+" electricity cost per year in pesos.")
            print( )
            
        if appliances == "Electric Fan":
            print("The fixed kilowatts: 200 ") 
            n_string = input("How many electric fans do you have?: ")
            n = float(n_string)
            sum = 0
            efankwhr_string = 200                                                   #the fixed electrical power consumption of the typical appliance
            efankwhr = float(efankwhr_string)                                              #the appliances owned by the consumer
            efanday = n*efankwhr*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
            efanmonth = efanday*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
            efanyear = efanmonth*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
 
            print( )
            print("The appliance has "+str(efanday)+" electricity cost per day in pesos.")
            print("The appliance has "+str(efanmonth)+" electricity cost per month in pesos.")
            print("The appliance has "+str(efanyear)+" electricity cost per year in pesos.")
            print( )

        if appliances == "Refrigerator":
            print("The fixed kilowatts: 300 ")
            n_string = input("How many refrigerators do you have?: ")
            n = float(n_string)
            sum = 0
            refkwhr_string = 300                                                   #the fixed electrical power consumption of the typical appliance
            refkwhr = float(refkwhr_string)                                              #the appliances owned by the consumer
            refday = n*refkwhr*time*cost                                                        #the formula used to get the typical appliance consumption cost per day in pesos
            refmonth = refday*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
            refyear = refmonth*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
            
            
            print("The appliance has "+str(refday)+" electricity cost per day in pesos.")
            print("The appliance has "+str(refmonth)+" electricity cost per month in pesos.")
            print("The appliance has "+str(refyear)+" electricity cost per year in pesos.")
            print( )
            
sum = sum+E                                                      #the formula used to get the total cost of all the appliances consumption cost rated per day in pesos
E3 = sum*30                                                          #the formula used to get the total cost of all the appliances consumption cost rated per month in pesos
E4 = E3*12                                                           #the formula used to get the total cost of all the appliances consumption cost rated per year in pesos

print("The total power consumption costs "+str(sum)+" pesos per day.")
print("The total power consumption costs "+str(E3)+" pesos per month.")
print("The total power consumption costs "+str(E4)+" pesos per year.")


# In[ ]:





# In[ ]:





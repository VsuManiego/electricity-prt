# Offering No.:G404
# AuthorS:Pepito, Renomeron, Triste
# Date created: 2021/11/26
#Title of the Project: Residential Electricity Cost Estimator using Python


#Calculates the total electricity consumption cost for all appliances owned by the consumer per day, month, and year
print("This program calculates the residential electricity bill per day, month and year.")

sum = 0
for E in range(0,3):                                               #the number of appliances owned by the consumer
  P_string = input("Enter the power consumption in kilowatts: ")   #the electrical power consumption of the typical appliance you want to rate
  P = float(P_string)
  T_string = input("Enter the hours of usage per day: ")           #the average hours you used that typical appliance in a day
  T = float(T_string)
  C = 6.8753                                                       #the fixed residential rate per kilowatt hour in pesos
  E = P*T*C                                                        #the formula used to get the typical appliance consumption cost per day in pesos
  E1 = E*30                                                        #the formula used to get the typical appliance consumption cost per month in pesos
  E2 = E1*12                                                       #the formula used to get the typical appliance consumption cost per year in pesos
  
  print("The appliance has "+str(E)+" electricity cost per day in pesos.")
  print("The appliance has "+str(E1)+" electricity cost per month in pesos.")
  print("The appliance has "+str(E2)+" electricity cost per year in pesos.")
  sum = sum+E                                                      #the formula used to get the total cost of all the appliances consumption cost rated per day in pesos
E3 = sum*30                                                        #the formula used to get the total cost of all the appliances consumption cost rated per month in pesos
E4 = E3*12                                                         #the formula used to get the total cost of all the appliances consumption cost rated per year in pesos

print("The total power consumption costs "+str(sum)+" pesos per day.")
print("The total power consumption costs "+str(E3)+" pesos per month.")
print("The total power consumption costs "+str(E4)+" pesos per year.")

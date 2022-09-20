#Calculating Simple Interest 
print("Enter pamt rate time ")
pamt,rate,time=int(input()),int(input()),int(input())

si=pamt*rate*time//100
amount=pamt+si

print("Interest Amount",si)
print("Amount to be paid",amount)
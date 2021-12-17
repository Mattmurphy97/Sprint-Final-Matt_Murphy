# Purpose:
# Author: Matt Murphy
# Date: Nov/30/2021

# GitHub Link: https://github.com/Mattmurphy97/Sprint-Final-Matt_Murphy

import datetime

curDate = datetime.datetime.now()

MONTHS = 12

def errorMsg():
    print("Invalid Entry, Please Try Again.")
    print()

f = open('OSICDef.dat', 'r')
policyNum = int(f.readline())
basePrem = float(f.readline())
addCar = float(f.readline())
extraLiRate = float(f.readline())
glassCovRate = float(f.readline())
loanerCovRate = float(f.readline())
hstRate = float(f.readline())
processFee = float(f.readline())

f.close()


# Initital Values
forNum = 1 # For car loops
curDate = datetime.datetime.now() # for dates

""""
# This is just a default input for debugging
custFirstName = "Matt"
custLastName = "Murphy"
streetAdd = "1 Old Branch Rd"
city = "Parker's Cove"
prov = "NL"
postCode = "A0E1H0"
phoneNum = "709-567-0978"
print()
carsAddedNum = 2
extraLi = "Y"
glassCov = "Y"
loanerCov = "Y"
paySchd = "M"

"""
# USE THIS CODE WHEN FINISHED DEBUGGING

# Main Program
custFirstName = input("Enter Customer's First Name:     ")
custFirstName = custFirstName.title()
custLastName = input("Enter Customer's Last Name:      ")
custLastName = custLastName.title()
streetAdd = input("Enter Customer's Street Address: ")
streetAdd = streetAdd.title()
city = input("Enter Customer's City:           ")
city = city.title()
prov = input("Enter Customer's Province:       ")
prov = prov.upper()
postCode = input("Enter Customer's Postal Code:    ")
postCode = postCode.upper()
phoneNum = input("Enter Customer's Phone Number:   ")
print()
carsAddedNum = int(input("Number of Cars to be Added to Policy: "))
extraLi = input("Add Extra Liability ? (Y/N):          ")
extraLi = extraLi.capitalize()
glassCov = input("Add Glass Coverage ? (Y/N):           ")
glassCov = glassCov.capitalize()
loanerCov = input("Add Loaner Coverage ? (Y/N):          ")
loanerCov = loanerCov.capitalize()
paySchd = input("Enter Customer Payment Plan (F/M):    ")
paySchd = paySchd.capitalize()




# Calculations & Process
totalOptCost = 0

while True:
    if carsAddedNum == 1:
        totalInsPrem = basePrem
        break
    elif carsAddedNum > 1:
        totalInsPrem = basePrem + ((basePrem * addCar) * carsAddedNum)
        break
    else:
        errorMsg()

if extraLi == "Y":
    totalInsPrem = totalInsPrem + extraLiRate
    totalOptCost = totalOptCost + extraLiRate
else:
    totalInsPrem = totalInsPrem

if glassCov == "Y":
    totalInsPrem = totalInsPrem + glassCovRate
    totalOptCost = totalOptCost + glassCovRate
else:
    totalInsPrem = totalInsPrem

if loanerCov == "Y":
    totalInsPrem = totalInsPrem + loanerCovRate
    totalOptCost = totalOptCost + loanerCovRate
else:
    totalInsPrem = totalInsPrem


hstAmt = totalInsPrem * hstRate
totalInsPremTax = totalInsPrem + hstAmt


if paySchd == "F":
    pass
elif paySchd == "M":
    monthPayAmt = (totalInsPremTax + processFee) / MONTHS


# Output for Receipt
print()
print("--------------------------------------------")
print("         One Stop Insurance Company")
print("--------------------------------------------")
print("             Personal Info:")
print(f" Policy Num:           {policyNum:>20}")
print(f" Customer First Name:  {custFirstName:>20}")
print(f" Customer Last Name:   {custLastName:>20}")
print(f" Customer Phone#:      {phoneNum:>20}")
print(f" Customer Address:     {streetAdd:>20}")
print(f"                       {city:>16}, {prov}")
print(f"                       {postCode:>20}")
print("--------------------------------------------")
print("            Policy Details:")
print(f" Number of Vehicles:   {carsAddedNum:>20}")
if extraLi == "Y":
    print(f" Extra Liability:      {extraLiRate:>20,.2f}")
else:
    print(" Extra Liability:                  DECLINED")

if glassCov == "Y":
    print(f" Glass Coverage:       {glassCovRate:>20,.2f}")
else:
    print(" Glass Coverage:                   DECLINED")

if loanerCov == "Y":
    print(f" Loaner Coverage:      {loanerCovRate:>20,.2f}")
else:
    print(f" Loaner Coverage:                  DECLINED")
print(f" Total Cost of Options:    {totalOptCost:>16,.2f}")
print("--------------------------------------------")
print("               Cost Info:")
print(f" Policy Cost:          {totalInsPrem:>20,.2f}")
print(f" Tax Amount:           {hstAmt:>20,.2f}")
print(f" Total Cost of Policy: {totalInsPremTax:>20,.2f}")
print("--------------------------------------------")
if paySchd == "M":
    print("              Payment Info:")
    print(f" Policy Date:                   ", (curDate.strftime("%m-%d-%Y")))
    print(f" First Monthly Payment Date:") # use beginning of next month UNLESS
                                           # its after the 25th, then its the following month
                                           # ALSO, add to policy file after policy number
    print(f" Monthly Payment Length: {MONTHS:>18}")
    print(f" Monthly Payment Amount: {monthPayAmt:>18,.2f}")
    print("--------------------------------------------")
print(" Thank You For Choosing One Stop Insurance")
print()


# To Increase Policy Number in OSICDef.dat file
policyNum += 1

f = open("Policies.dat", "a")
f.write("{}-{}{}, ".format(policyNum, custFirstName[0], custLastName[0]))
f.write("{} {}, ".format(custFirstName, custLastName))
f.write("{}, ".format(streetAdd))
f.write("{}, ".format(city))
f.write("{}, ".format(prov))
f.write("{}, ".format(postCode))
f.write("{}, ".format(phoneNum))
f.write("{}, ".format(carsAddedNum))
f.write("{}, ".format(extraLi))
f.write("{}, ".format(glassCov))
f.write("{}, ".format(loanerCov))
f.write("{}, ".format(hstAmt)) #12
f.write("{}, ".format(totalOptCost))
f.write("{}, ".format(totalInsPrem))
f.write("{}\n".format(totalInsPremTax)) #15

# To Update: OSICDef.dat
f = open("OSICDef.dat", "w")
f.write("{}\n".format(str(policyNum)))
f.write("{}\n".format(str(basePrem)))
f.write("{}\n".format(str(addCar)))
f.write("{}\n".format(str(extraLiRate)))
f.write("{}\n".format(str(glassCovRate)))
f.write("{}\n".format(str(loanerCovRate)))
f.write("{}\n".format(str(hstRate)))
f.write("{}\n".format(str(processFee)))
f.close()

print("Policy Processed & Saved!")
anykey = input("Press Enter to View Reports...")
print()
print()


# Report #1 - Detailed
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF", (curDate.strftime("%m-%d-%Y")))
print()
print("POLICY     CUSTOMER       INSURANCE     EXTRA     TOTAL")
print("NUMBER       NAME          PREMIUM      COST     PREMIUM")
print("========================================================")


policyCtr = 0
premBeforeTaxAcc = 0
extraCostsAcc = 0
premWithTaxAcc = 0

f = open("Policies.dat", "r")
for policyDatLine in f:
    policyDat = policyDatLine.split(",")
    reportPolicyNum = policyDat[0].strip()
    reportCustName = policyDat[1].strip()
    reportPremAmt = policyDat[14].strip()
    reportExtraAmt = policyDat[13].strip()
    reportPremWithTax = policyDat[15].strip()

    print(f"{reportPolicyNum:<7}   {reportCustName:<15} {reportPremAmt:<7}     {reportExtraAmt:<7} {reportPremWithTax:<7}")

    policyCtr += 1


f.close()
print("========================================================")
print(f"Total Policies: {policyCtr}")
print()
anykey = input("Press Enter to Continue to Next Report...")
print()


policyCtr = 0
premBeforeTaxAcc = 0
extraCostsAcc = 0
premWithTaxAcc = 0

f = open("Policies.dat", "r")
for policyDatLine in f:
    policyDat = policyDatLine.split(",")
    reportPolicyNum = policyDat[0].strip()
    reportCustName = policyDat[1].strip()
    reportPremAmt = policyDat[14].strip()
    reportHstAmt = policyDat[12].strip()
    

    print()

    policyCtr += 1


# Report #2 - Exception
print("ONE STOP INSURANCE COMPANY")
print(f"Monthly Payment Listing as of:", (curDate.strftime("%m-%d-%Y")))
print()
print("POLICY  CUSTOMER          TOTAL                 MONTHLY")
print("NUMBER    NAME           PREMIUM      HST       PAYMENT")
print("========================================================")
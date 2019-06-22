import sys
import math

# Global Variables
# Salary + List of Tax Rates (state = CA), changeable
taxableGrossSalary = 3000

federalTax = 0.25
stateTax = 0.035
localTax = 0
oasdi = 0.062
medicare = 0.0145

# Sum of All Taxes
sumRate = federalTax + stateTax + localTax + oasdi + medicare

# Array of the List
indivTaxName = ["Federal Tax", "State Tax", "Local Tax", "OASDI", "Medicare"]
indivTaxArray = [federalTax, stateTax, localTax, oasdi, medicare]
counter = 0

# Calculates Gross Up Salary
def calculateGrossUpSalary(gross, sumRate):
    revSumRate = 1 - sumRate
    return gross/revSumRate

# Calculates Gross Up Amount
def calculateGrossUp(grossUpSalary, taxableGrossSalary):
    return grossUpSalary - taxableGrossSalary

# Calculates Individual Tax Gross Up Amount
def calculateIndividualTax(extraGross, indivTax):
    return (indivTax/sumRate)*extraGrossUp

grossUpSalary = calculateGrossUpSalary(taxableGrossSalary, sumRate)
extraGrossUp = calculateGrossUp(grossUpSalary, taxableGrossSalary)


print("Total Gross Up Salary:", "%.2f" % grossUpSalary)
print("Total Gross Up:", "%.2f" % extraGrossUp)
print()

for tax in indivTaxArray:
    indiviTax = calculateIndividualTax(extraGrossUp, tax)
    print(indivTaxName[counter], "=", "%.2f" %  indiviTax)
    counter += 1

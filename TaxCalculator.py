# Nelson Oseguera

# March 21st, 2023

# Programming Project 6

# This program will be able to take the user's input about total sales for a month from a retail company, and calculate the sales tax, county tax, and total tax from the user's input. It will then display the results.

# Declare Variables, Real totalSales, Real countyTax, Real stateTax, totalTax

totalSales = 0

countyTax = 0

stateTax = 0

totalTax = 0

def main():

# Function Calls
    
    inputData()

    calcCounty()

    calcState()

    calcTotal()

    printData()

# This module takes in required user input

def inputData():

    global totalSales

    print('Please Enter the total sales for the month.')

    totalSales = float(input())

# This module calculates the county tax

def calcCounty():

    global countyTax

    countyTax = totalSales * .02

# This module calculates the state tax

def calcState():

    global stateTax

    stateTax = totalSales * .04

# This module calculates the total tax

def calcTotal():

    global totalTax

    totalTax = countyTax + stateTax

# This module prints the total, county, and state tax

def printData():

    print('The county tax is $', countyTax)

    print('The state tax is $', stateTax)

    print('The total tax is $', totalTax)

# Call the main function

main()

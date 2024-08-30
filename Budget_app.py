##time is by weeks
year = 52


def budget(income):
    global year
    percent = float(input("What percent do you want to put into your savings account.(no need for % symbol): "))
    yearly_Income = year * income
    savings = percent // 100.0 * yearly_Income 
    checking = yearly_Income * (1.0 - (float(percent) // 100.0))
    print ("you make: $" + str(yearly_Income) + " a year")
    print ("You save : $" + str(savings) + " a year")
    print ("You keep : $" + str(checking) + " a year to spend")
    
    
budget(int(input("How much do you make a two week paycheck: ")))
    
    
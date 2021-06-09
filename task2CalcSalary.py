def calcSalary1(workedDays, oklad, monthDays):
    salary = (workedDays * oklad) / monthDays
    salaryOfYear = salary * 12
    return ("В месяц: "  + str(round(salary, 2)) + " руб.", "В год " + str(round(salaryOfYear, 2))  + " руб.")

def calcSalary2(workedDays, oklad, monthDays):
    salary = (workedDays * oklad) / monthDays
    salaryOfYear = salary * 12
    return salary

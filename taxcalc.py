def getIncomeTax(salary):
    personal_allowance = 11850
    basic_tax_band = 34500
    higher_tax_band = 150000

    if salary <= personal_allowance:
        return 0
    elif salary <= basic_tax_band:
        return (salary - personal_allowance) * 0.2
    elif salary <= higher_tax_band:
        basic_tax = (basic_tax_band - personal_allowance) * 0.2
        higher_tax = (salary - basic_tax_band) * 0.4
        return basic_tax + higher_tax
    else:
        basic_tax = (basic_tax_band - personal_allowance) * 0.2
        higher_tax = (higher_tax_band - basic_tax_band) * 0.4
        additional_tax = (salary - higher_tax_band) * 0.45
        return basic_tax + higher_tax + additional_tax

print(f"Incomne tax with a salary of £10000 is: £{getIncomeTax(10000)}") 
print(f"Incomne tax with a salary of £20000 is: £{getIncomeTax(20000)}")   
print(f"Incomne tax with a salary of £50000 is: £{getIncomeTax(50000)}")
print(f"Incomne tax with a salary of £200000 is: £{getIncomeTax(200000)}")
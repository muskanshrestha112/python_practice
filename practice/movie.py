def TicketCounter(name,age,money):
    if age < 18:
        return "You are not allowed."
    if name == 'Tarun':
        return "Name not allowed."
    if money < 180:
        return " Insufficent money. "
    return f"Thank you {name}, Here is you change {money-180}Rs."

print(TicketCounter('Muskan', 16, 120))
print(TicketCounter('Tarun', 19, 120))
print(TicketCounter('Muskan', 21, 120))
print(TicketCounter('Muskan', 22, 200))



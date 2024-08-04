def DiscountTrack(ticket,name,price,voucher=False, discount=0):
    ticket_price = 180
    if ticket > 10:
        return "Something went wrong tickets."
    if ticket > 5:
        discount += 20 # discount = discount + 20
    if voucher:
        discount += 10 
    print(discount)
    if discount != 0 :
        total_price = (ticket * ticket_price) - ((discount/100) * (ticket * ticket_price)) 
    else:
        total_price = ticket_price * ticket
    if total_price > price:
        return "Money is insuffecient."
    return f"Thank you {name}.Here is your change {price-total_price}"


print(DiscountTrack(9,"ram",5000, voucher=True))
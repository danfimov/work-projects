with open('2.2-input.txt', 'r') as f:
    max_price, max_code = False, False
    min_price, min_code = False, False
    for line in f:
        code, name, price = line.strip().split(';')
        code, price = int(code), int(price)
        if max_price is False or max_price <= price:
            max_price, max_code = price, code
        if min_price is False or min_price >= price:
            min_price, min_code = price, code
with open('2.2-output.txt', 'w', newline='') as f:
    print(max_code, file=f)
    print(min_code, file=f)
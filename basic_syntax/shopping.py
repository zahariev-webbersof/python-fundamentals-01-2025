budget = int(input())
price_counter = 0

while True:
    command = input()

    if command == 'End':
        print('You bought everything needed.')
        break

    product_price = int(command)

    if price_counter + product_price > budget:
        print('You went in overdraft!')
        break

    price_counter += product_price
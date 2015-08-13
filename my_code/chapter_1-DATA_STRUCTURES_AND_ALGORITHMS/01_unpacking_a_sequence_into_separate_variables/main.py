if __name__ == '__main__':
    p = (4, 5)
    x, y = p
    print(x)
    print(y)
    print('-' * 50)

    data = ['ACME', 50, 91.1, (2012, 12, 31)]
    name, share, price, date = data
    print(name)
    print(share)
    print(price)
    print(date)
    name, share, price, (year, month, day) = data
    print(name)
    print(year)
    print(month)
    print(day)
    print('-' * 50)

    try:
        p = (4, 5)
        x, y, z = p
    except ValueError:
        print("An error was occurred")
    print('-' * 50)

    s = 'Hello'
    a, b, c, d, e = s
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print('-' * 50)

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    _, shares, price, _ = data
    print(shares)
    print(price)

n = int(input())
result = 0
if 0 < n <= 9950:
    result = (n / 100) * 10
    print(n - result)
elif 9951 <= n <= 40525:
    result = (n / 100) * 12
    print(n - result)
elif 40526 <= n <= 86375:
    result = (n / 100) * 22
    print(n - result)
elif 86376 <= n <= 164925:
    result = (n / 100) * 24
    print(n - result)
elif 164926 <= n <= 209425:
    result = (n / 100) * 32
    print(n - result)
elif 209426 <= n < 523600:
    result = (n / 100) * 34
    print(n - result)
elif n >= 523600:
    result = (n / 100) * 37
    print(n - result)

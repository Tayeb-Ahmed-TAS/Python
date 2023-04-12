def even_numbers(x):
    for i in range(x + 1):
        if i % 2 == 0:
            yield i


res = list(even_numbers(10))

print(res)

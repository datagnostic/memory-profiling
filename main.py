from memory_profiler import profile


@profile(precision=3)
def measure(func, n):
    return func(n)


def defined_sum_on_list(n):
    return sum([x ** 2 for x in range(n)])


def defined_sum_on_generator(n):
    return sum(x ** 2 for x in range(n))


n = 2000000
print(f"---------{defined_sum_on_list.__name__}---------")
measure(defined_sum_on_list, n)
print(f"---------{defined_sum_on_generator.__name__}---------")
measure(defined_sum_on_generator, n)
print(f"---------lambda y: sum([x ** 2 for x in range(y)])---------")
measure(lambda y: sum([x ** 2 for x in range(y)]), n)
print(f"---------lambda y: sum(x ** 2 for x in range(y))---------")
measure(lambda y: sum(x ** 2 for x in range(y)), n)
print(f"---------lambda y: sum(map(lambda x: x ** 2, range(y)))---------")
measure(lambda y: sum(map(lambda x: x ** 2, range(y))), n)

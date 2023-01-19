```
---------defined_sum_on_list---------

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4   17.996 MiB   17.996 MiB           1   @profile(precision=3)
     5                                         def measure(func, n):
     6   18.359 MiB    0.363 MiB           1       return func(n)


---------defined_sum_on_generator---------

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4   18.359 MiB   18.359 MiB           1   @profile(precision=3)
     5                                         def measure(func, n):
     6   18.359 MiB    0.000 MiB           1       return func(n)


---------lambda y: sum([x ** 2 for x in range(y)])---------

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4   18.359 MiB   18.359 MiB           1   @profile(precision=3)
     5                                         def measure(func, n):
     6   33.586 MiB   15.227 MiB           1       return func(n)


---------lambda y: sum(x ** 2 for x in range(y))---------

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4   33.586 MiB   33.586 MiB           1   @profile(precision=3)
     5                                         def measure(func, n):
     6   33.586 MiB    0.000 MiB           1       return func(n)


---------lambda y: sum(map(lambda x: x ** 2, range(y)))---------

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4   33.586 MiB   33.586 MiB           1   @profile(precision=3)
     5                                         def measure(func, n):
     6   33.586 MiB    0.000 MiB           1       return func(n)
```

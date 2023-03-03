def ft_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ft_fibonacci(n-1) + ft_fibonacci(n-2)
    
print(ft_fibonacci(9))
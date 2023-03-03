def ft_len(str):
    
    if str == "":
        return 0
    else:
        return 1 + ft_len(str[1:])

print("ft_len = ", ft_len("Hello World!"))
print("len = ", len("Hello World!"))
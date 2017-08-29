def fact(x):
    if x<0:
        return None
    elif x<2:
        return x
    else:
        return x*fact(x-1)

print fact(5)

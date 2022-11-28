w = int(input("weight:"))
l = input("l or k:")
if l.upper() == "L":
    wg = w * 0.45
    pritnt("your weigth is{wg}")
else:
    wk = w/0.45
    print("your weigh is {wk} pounds")

order = 7
top_left = 3
int_order = int(order)
int_top_left = int(top_left)
for order in range(int_order):
    for top_left in range(int_order):
        print(int_top_left, end=" ")
    print()

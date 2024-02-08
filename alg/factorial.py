def num_possible_orders(num_posts):
    n = 1 
    for i in range(num_posts):
        n *= i+1
    return n


assert num_possible_orders(11) == 39916800

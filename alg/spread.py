def get_estimated_spread(audiences_followers):
    s = sum(audiences_followers)
    n = len(audiences_followers)
    return (s/n)*(n**1.2)

test_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
assert round(get_estimated_spread(test_list)) == 872


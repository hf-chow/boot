def decayed_followers(intl_followers, fractions_lost_daily, days):
    return round(intl_followers*(1-fractions_lost_daily)**days)

assert decayed_followers(100, 0, 5) == 100
assert decayed_followers(1200, 0.09, 16) == 265

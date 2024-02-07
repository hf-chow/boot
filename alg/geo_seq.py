def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type=="fitness":
        return follower_count*(4**num_months)
    elif influencer_type=="cosmetic":
        return follower_count*(3**num_months)
    return follower_count*(2**num_months)

assert get_follower_prediction(10, "fitness", 8) == 655360


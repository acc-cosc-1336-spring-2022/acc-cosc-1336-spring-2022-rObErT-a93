def get_options_ratio(options, total):
    return float(options / total)

def get_faculty_rating(rating):
    if rating >= .9 and rating <= 1:
        return 'Excellent'
    elif rating >= .8:
        return 'Very Good'
    elif rating >= .7:
        return 'Good'
    elif rating >= .6:
        return 'Needs Improvement'
    else:
        rating >= 0 and rating <= .59
        return 'Unacceptable'
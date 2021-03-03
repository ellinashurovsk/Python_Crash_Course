def build_user_info(first, last, **info):
    """
    Build a dictionary with the user info.
    """
    info['first name'] = first
    info['last name'] = last
    return info


user = build_user_info('Olivia', 'Brown', location='NY',
                       field='electrical engineering', pet='Kitty')
print(user)

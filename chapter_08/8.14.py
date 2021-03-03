def auto_info(producer, model, **auto_info):
    """
    Put the info about the auto in the dictionary
    """
    auto_info['producer'] = producer
    auto_info['model'] = model
    return auto_info


auto_lada = auto_info('lada', '9', height="1,5",
                      lenght="3,5", tow_package=True)
print(auto_lada)

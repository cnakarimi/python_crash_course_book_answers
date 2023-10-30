def build_car(manufactor, model, **optional_feature):
    car = {}
    car['manufactor'] = manufactor
    car['model'] = model
    for k, v in optional_feature.items():
        car[k] = v
    return car


print(build_car('subaru', 'outback', color='blue', tow_package=True))

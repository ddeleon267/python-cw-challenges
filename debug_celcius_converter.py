# lots of small typos in this one, also need to account for errors in spacing/indentation
def convert_to_celcius(temperature):
    # original formula wasn't right
    celsius = (temperature - 32) * (5/9)
    return celsius

def weather_info(temp):
    c = convert_to_celcius(temp)
    if (c > 0):
        return f"{c} is above freezing temperature"
    else:
        return f"{c} is freezing temperature"
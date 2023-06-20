
def get_city_name(city, country, population=''):
    """ do names like santiago, chile work """
    if population:
        city_name = f"{city} {country} {population}"
    else:
        city_name = f"{city} {country}"
        
    return city_name.title()


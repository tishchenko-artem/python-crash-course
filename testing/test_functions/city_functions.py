def city_country(city, country, population=''):
    if population:
        formatting = city + ', ' + country
        return formatting.title() + ' - population ' + str(population) + '.'
    else:
        formatting = city + ', ' + country + '.'
        return formatting.title()

a = city_country('kiev', 'ukraine')
p = city_country('kiev', 'ukraine', 100000)
print(a)
print(p)
from countryinfo import CountryInfo
countryName = input("Please enter country name to fetch its details\n")
country = CountryInfo(countryName)
indiaProvinces = country.provinces()          #This API returns provinces/States list
indiaAlternateNames = country.alt_spellings() #This API returns alternate names
indiaArea = country.area()                    #This API returns area (km²) for a specified country
indiaBorder = country.borders()               #This API bordering countries (ISO3) for a specified country
print("List of all provinces of %s :\n"%(countryName))
print(indiaProvinces)
print("\n")
print("List of alternate names of %s : \n"%(countryName))
print(indiaAlternateNames)
print("\n")
print("Total Area of %s : \n"%(countryName))
print(indiaArea)
print("\n")
print("Names of countries having borders with %s  : \n"%(countryName))
print(indiaBorder)
print("\n")
input()
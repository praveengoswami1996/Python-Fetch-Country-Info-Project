from countryinfo import CountryInfo
countryName = input("Please enter country name to fetch its details\n")
country = CountryInfo(countryName)
indiaProvinces = country.provinces() #It returns provinces/States list
indiaAlternateNames = country.alt_spellings() #It returns alternate names
print("List of all Indian states : \n")
print(indiaProvinces)
print("\n")
print("List of alternate names of India : \n")
print(indiaAlternateNames)
input()
class India:
    def capital(self):
        print("New delhi is the capital of india")
    def language(slef):
        print("Hindi is the most spoken language in india and is an official language")
    def type(self):
        print("India is a developing country")
class USA:
    def capital(self):
        print("Washington D.C is the capital of the USA")
    def language(slef):
        print("English is the most spoken language in the USA and is an official language")
    def type(self):
        print("USA is a developed country")

obj_ind = India()
obj_USA = USA()
for country in (obj_ind, obj_USA):
    country.capital()
    country.language()
    country.type()
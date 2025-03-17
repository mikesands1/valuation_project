# Base class for Subject Property (Both Flats and Houses)
class SubjectProperty:
    def __init__(self, valuation_type, price, address, size, bedrooms, bathrooms, floors, outside_space, age,
                 ex_local_authority, property_type, mortgageable, buy_to_let, adverse_features=[]):
        self.valuation_type = valuation_type  
        self.price = price
        self.address = address
        self.size = size 
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.floors = floors
        self.outside_space = outside_space  
        self.age = age
        self.ex_local_authority = ex_local_authority
        self.property_type = property_type
        self.mortgageable = mortgageable
        self.buy_to_let = buy_to_let
        self.adverse_features = adverse_features


from valuation_project import SubjectProperty

# Subclass for Houses (inherits from SubjectProperty)
class House(SubjectProperty):
    def __init__(self, valuation_type, price, address, size, bedrooms, bathrooms, floors, outside_space, age,
                 ex_local_authority, property_type, adverse_features, mortgageable, buy_to_let, house_type):
        
        super().__init__(self, valuation_type, price, address, size, bedrooms, bathrooms, floors, outside_space, age,
                 ex_local_authority, property_type, adverse_features, mortgageable, buy_to_let)
        
        self.house_type = house_type
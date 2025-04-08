from valuation_project import SubjectProperty

class Flat(SubjectProperty):
    def __init__(self, valuation_type, price, address, size, bedrooms, bathrooms, floors, outside_space, age,
                 ex_local_authority, property_type, adverse_features, mortgageable, buy_to_let, flat_type, lease_length, service_charge, ground_rent, ews1, floor_level):
        
        super().__init__(self, valuation_type, price, address, size, bedrooms, bathrooms, floors, outside_space, age,
                 ex_local_authority, property_type, adverse_features, mortgageable, buy_to_let)
        
        self.flat_type = flat_type  
        self.lease_length = lease_length
        self.service_charge = service_charge
        self.ground_rent = ground_rent
        self.ews1 = ews1  
        self.floor_level = floor_level

hello world

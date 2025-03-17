# Comparable Rental Class
class ComparableRental:
    def __init__(self, rental_price, let_date, letting_agent=None, description=None, distance=None, 
                 location=None, size=None, bedrooms=None, condition=None, outside_space=None, 
                 other_adjustments=None):
        
        self.rental_price = rental_price
        self.let_date = let_date
        self.letting_agent = letting_agent
        self.description = description
        self.distance = distance
        self.location = location  
        self.size = size  
        self.bedrooms = bedrooms
        self.condition = condition  
        self.outside_space = outside_space  
        self.other_adjustments = other_adjustments or []
        self.adjusted_value = self.calculate_adjusted_value()

    def calculate_adjusted_value(self):
        """Apply adjustments to rental value"""
        adjustments = sum(self.other_adjustments) if self.other_adjustments else 0
        return self.rental_price + adjustments
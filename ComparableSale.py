class ComparableSale:
    def __init__(self, sale_price, sold_status, selling_agent, description, property_type, distance, 
                 location, size, bedrooms, condition, under_offer_date=None, sale_date=None, outside_space=None, 
                 outside_space_type=None, other_adjustments=None):
        
        self.sale_price = sale_price
        self.sold_status = sold_status  
        self.selling_agent = selling_agent if sold_status == "Under Offer" or "Sold" else None
        self.under_offer_date = under_offer_date if sold_status == "Under Offer" else None
        self.sale_date = sale_date if sold_status == "Sold" else None
        self.property_type = property_type
        self.distance = distance
        self.location = location  
        self.size = size  
        self.bedrooms = bedrooms
        self.condition = condition  
        self.outside_space = outside_space  
        self.outside_space_type = outside_space_type if outside_space == "Yes" else None
        self.other_adjustments = other_adjustments or []
        self.adjusted_value = self.calculate_adjusted_value()

    # Function to get user input and create an instance of ComparableSale
    def get_comparable_sale_input():
        print("Enter details for the Comparable Sale:")

        sale_price = int(input("Sale Price (£): "))
        sold_status = input("Sold Status (Available, Under Offer, Sold): ").strip()
        sold_status = input("Under Offer, Sold: ")
        selling_agent = input("Selling Agent: ").strip()

        if sold_status == "Under Offer":
            under_offer_date = input("Under Offer Date (YYYY-MM-DD): ").strip()

        if sold_status == "Sold":
            sale_date = input("Sale Date (YYYY-MM-DD): ").strip()

        description = input("Brief Description: ").strip()
        property_type = input("Property Type (Flat, House, etc.): ").strip()
        distance = int(input("Distance from Subject (meters): "))
        location = input("Location (Better, Similar, Worse): ").strip()
        size = int(input("Size (sq m): "))
        bedrooms = int(input("Number of Bedrooms: "))
        condition = input("Very Good, Good, Average, Fair, Unmodernised): ").strip()
        outside_space = input("Does it have outside space? (Yes/No): ").strip()
        outside_space_type = None
        if outside_space.lower() == "yes":
            outside_space_type = input("Outside Space Type (Garden, Balcony, etc.): ").strip()

        other_adjustments = input("Any other adjustments? (Leave blank if none): ").strip() or None
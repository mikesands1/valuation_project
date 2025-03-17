class Comparisons:
    def __init__(self, location, location_adjustment, size, size_adjustment, bedrooms, bedrooms_adjustment, 
                 condition, condition_adjustment, outside_space, outside_space_adjustment, other, other_adjustment):

        self.location = location
        self.location_adjustment = location_adjustment if location != "Similar" else location_adjustment=None
        self.size = size
        self.size_adjustment = size_adjustment if location != "Similar" else size_adjustment=None
        self.bedrooms = bedrooms
        self.bedrooms_adjustment = bedrooms_adjustment if location != "Similar" else bedrooms_adjustment=None
        self.condition = condition
        self.condition_adjustment = condition_adjustment if location != "Similar" else condition_adjustment=None
        self.outside_space = outside_space
        self.outside_space_adjustment = outside_space_adjustment if location != "Similar" else outside_space_adjustment=None
        self.other = other
        self.other_adjustment = other_adjustment if location != "Similar" else other_adjustment=None


    def sum_adjustments(self):
        return self.location_adjustment + self.size_adjustment + self.condition_adjustment + self.outside_space_adjustment + self.other_adjustment

    def location_description(self):
        if self.location == "Worse":
            return f'Location considered inferior to that of the subject'
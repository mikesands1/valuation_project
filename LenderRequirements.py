class LenderRequirements:
    """A class to handle lender requirements and generate standardized report paragraphs."""

    def __init__(self):
        pass 

    @staticmethod
    def outside_6_months():
        return ("Where any comparable with a transaction date more than six months "
                "before the date of valuation has been used, this is because in my experience and opinion, "
                "the sales data is still valid and any market movement in prices since that time has been adjusted for. "
                "Also, this is deemed preferable to using more recent sales of less comparable properties.\n\n")

    @staticmethod
    def sstc():
        return ("SSTC or under offer comparables are considered to be a valid indicator of current market price levels. "
                "This is backed up by additional information provided by the agent, recorded in the notes section.\n\n")

    @staticmethod
    def outside_500m():
        return ("Where any comparable further than 500m from the subject property has been used, "
                "this is because in my experience and opinion the sales data is still valid and any market movement in prices "
                "due to location has been adjusted for.\n\n")

    @staticmethod
    def value_outside_10pc():
        return ("Where any comparable with a Market Value +/- 10% of the subject MV has been used, "
                "this is because in my experience and opinion these sales are still important comparables "
                "and appropriate adjustments have been made.\n\n")

    @staticmethod
    def similar_age_houses():
        return "All three comparables used were houses of a similar age and construction to the subject.\n\n"

    @staticmethod
    def similar_age_flats():
        return "All three comparables used were located in properties of a similar age and construction to the subject.\n\n"

    


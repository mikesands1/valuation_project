# from ComparableSale import ComparableSale
# from Comparisons import Comparisons
from LenderRequirements import LenderRequirements

NUM_SALE_COMPARABLES = 3 
NUM_RENTAL_COMPARABLES = 3

def ask_yes_no(question): # Helper function
        while True:
            response = input(f"{question} (Y/N): ").strip().lower()
            if response in ["y", "yes"]:
                return True
            elif response in ["n", "no"]:
                return False
            else:
                print("Invalid input. Please enter Y or N.")

# Subject property


########## COMPARABLES ##########

# Sales Comparables

# comparable_sale_1 = ComparableSale.get_comparable_sale_input()
# comparable_sale_2 = ComparableSale.get_comparable_sale_input()
# comparable_sale_3 = ComparableSale.get_comparable_sale_input()

###### LENDER REQUIREMENTS ######

print("\n###### LENDER REQUIREMENTS ######\n")
    

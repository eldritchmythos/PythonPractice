# Define a function to create a dictionary from a text file containing the 50 states 
# and their capitals
def get_state_cap_dict():
    # Create an empty dictionary
    state_capital_dict = dict()
    
    # Open and read the text file
    with open('state_cap.txt', 'r') as file:
        for line in file:
            # Split each line into state and capital using multiple assignment
            state, capital = line.strip().split(',')
            # Add the pair to the empty dictionary we created
            state_capital_dict[state] = capital
            
    return state_cap_dict

#call the function
get_state_cap_dict()
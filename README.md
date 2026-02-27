# WAIIAW
Writing An Interpreter In A Week

# Game Plan

Our interpreter will be very basic and single pass. It is the most common type of interpreter- A tree walk interpreter. Here is how it works:

* It takes code line by line
* It creates a dictionary with built-in keys like "LOGIC" or "ARGS"
* It executes code based off of the tree.
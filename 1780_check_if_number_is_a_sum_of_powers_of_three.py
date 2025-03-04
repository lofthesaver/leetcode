class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        # Ternary number system:
        # https://www.geeksforgeeks.org/ternary-number-system-or-base-3-numbers/
        
        # Convert n to a ternary representation (basically binary but with 3 instead of 2),
        # then check if any representation is a 2, if it is then you need two copies of that corresponding
        # power of three to represent the number

        # Function to convert n to ternary representation
        def convert_to_ternary(n):
            ternary_rep = []
            while n > 0:
                ternary_rep.append(n % 3)
                n = n // 3

            return ternary_rep
        
        # Loop through ternary rep, if any value is 2 then return False, else return True
        for v in convert_to_ternary(n):
            if v == 2:
                return False

        return True 
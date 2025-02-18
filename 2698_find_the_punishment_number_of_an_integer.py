class Solution:
    def punishmentNumber(self, n: int) -> int:

        # Function to check whether there is a partition of square such that the partition == i
        def can_be_partitioned(square, i):

            # If i < 0, return False
            if square < 0 or i < 0:
                return False

            # If square is 0 but i != 0, return False
            if square == 0 and i != 0:
                return False

            # If target is found, return True
            if square == i:
                return True

            # Else, perform check of square // 10 == i - square % 10
            else:
                return can_be_partitioned(square // 10, i - (square % 10)) or can_be_partitioned(square // 100, i - (square % 100)) or can_be_partitioned(square // 1000, i - (square % 1000))


        res = 0
        # Loop through integers from 1 to n, for each integer check whether partition can be satisfied
        for i in range(1, n + 1):
            square = i * i
            if can_be_partitioned(square, i):
                res += square

        return res
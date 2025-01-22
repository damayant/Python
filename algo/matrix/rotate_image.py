class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1  # Initialize the left and right bounds

        while l < r:  # Loop until the entire matrix is rotated layer by layer
            for i in range(r - l):  # Iterate over the current layer
                top, bottom = l, r  # Set the top and bottom bounds for the current layer

                # Save the top-left element
                topLeft = matrix[top][l + i]

                # Move the bottom-left element to the top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move the bottom-right element to the bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move the top-right element to the bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move the saved top-left element to the top-right
                matrix[top + i][r] = topLeft

            # Move to the next inner layer
            r -= 1
            l += 1
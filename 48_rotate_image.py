class Solution(object):
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation.

    Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
    """
    def __check_initial_conditions(self, matrix):
        return (len(matrix) <= 20 and 
                len(matrix) >= 1 and
                min(min(sub_list) for sub_list in matrix) >= -1000 and
                max(max(sub_list) for sub_list in matrix) <= 1000)

                                   
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if self.__check_initial_conditions(matrix):
            max_range = len(matrix) - 1
            min_range = 0
            while min_range < max_range:
                max_local_range = max_range
                while min_range < max_local_range:
                    i = min_range
                    j = max_local_range
                    temp = matrix[i][j]
                    for iter in range(4):
                        next_temp = matrix[j][len(matrix)-1-i]
                        matrix[j][len(matrix)-1-i] = temp
                        temp = next_temp
                        temp_j = j
                        j = len(matrix)-1-i
                        i = temp_j
                    max_local_range -= 1
                min_range += 1
                max_range -= 1
            return matrix
        else:
            return "Solution doesn't meet the initial conditions"
        
if __name__ == "__main__":
    obj = Solution()
    print(obj.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
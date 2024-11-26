class Solution(object):
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            min_val = 1
            max_val = 2
            suma = 0
            for i in range(n-2):
                suma = min_val + max_val
                min_val = max_val
                max_val = suma
            return suma


if __name__ == "__main__":
    obj = Solution()
    print(obj.climbStairs(44))
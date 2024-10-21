class Solution(object):

    def __check_initial_conditions(self, weights: list, days: int) -> bool:
        return (days >= 1 and
        days <= len(weights) and
        len(weights) <= 5 * 10**4 and
        min(weights) >= 1 and
        max(weights) <= 500)

    def shipWithinDays(self, weights: list, days: int) -> int:
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        if self.__check_initial_conditions(weights,days):
            max_weight = max(weights)
            sum_weights = sum(weights)
            min_days = 
            

if __name__ == "__main__":
    obj = Solution()
    print(obj.shipWithinDays([180,373,75,82,497,23,303,299,53,426,152,314,206,433,283,370,179,254,265,431,453,17,189,224],12))
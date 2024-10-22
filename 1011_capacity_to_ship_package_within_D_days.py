class Solution(object):
    """
    A conveyor belt has packages that must be shipped from one port to another within days days.
    The i-th package on the conveyor belt has a weight of weights[i]. 
    Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
    We may not load more weight than the maximum weight capacity of the ship.

    Return the least weight capacity of the ship that will result in all the packages on the conveyor belt
    being shipped within days days.

    Constraints:

    * 1 <= days <= weights.length <= 5 * 10^4
    * 1 <= weights[i] <= 500
    """
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
            init_min= max(weights)
            init_max = sum(weights)
            while init_min < init_max:
                capacity = (init_min + init_max) // 2
                day_id = 1
                sum_capacity = 0
                for w in weights:
                    if sum_capacity + w <= capacity:
                        sum_capacity += w
                    else:
                        day_id += 1
                        sum_capacity = w
                if day_id <= days:
                    init_max = capacity
                else:
                    init_min = capacity + 1
                
            return init_min




if __name__ == "__main__":
    obj = Solution()
    print(obj.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))
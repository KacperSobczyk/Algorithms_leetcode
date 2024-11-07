class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        typed_iter = 0
        typed_count = 0
        i = 0
        repeat_count = 0
        while i < len(name):
            if (typed_iter >= len(typed) or 
                len(name) > len(typed) or 
                name[i] != typed[typed_iter]):
                break
            while (typed_iter + typed_count < len(typed) and 
                   name[i] == typed[typed_iter + typed_count]):
                typed_count += 1
            while (i + repeat_count < len(name) and
                   name[i] == name[i + repeat_count]):
                repeat_count += 1
            if repeat_count > typed_count:
                break
            typed_iter += typed_count
            i += repeat_count
            typed_count = 0
            repeat_count = 0
            if i == len(name) and typed_iter != len(typed):
                break
        else:
            return True
        return False
            
if __name__ == "__main__":
    obj = Solution()
    print(obj.isLongPressedName("pyplrz", "ppyypllr"))

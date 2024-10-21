class Solution(object):
    """
    Given two integers a and b, return any string s such that:

    s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
    The substring 'aaa' does not occur in s, and
    The substring 'bbb' does not occur in s.

    Constraints:

    0 <= a, b <= 100
    It is guaranteed such an s exists for the given a and b.
    """
    def set_dominated_letters(self, a: int, b):
        dominated_letter = 'a' if a >= b else 'b'
        second_letter = 'b' if dominated_letter == 'a' else 'a'
        dom_index = a if dominated_letter == 'a' else b
        sec_index = b if dominated_letter == 'a' else a
        return (dominated_letter, second_letter, dom_index, sec_index)

    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        s = ""
        if a >= 0 and b <= 100:
            if 2*a + 2 >= b and 2*b + 2 >= a:
                dom_letter, sec_letter, dom_index, sec_index = self.set_dominated_letters(a,b)
                while dom_index != sec_index:
                    s += 2 * dom_letter + sec_letter
                    dom_index -= 2
                    sec_index -= 1
                    if sec_index == 0:
                        s += dom_index * dom_letter
                        return s
                for i in range(sec_index):
                    s += dom_letter + sec_letter
                return s
        return "Solution doesn't exist"
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.strWithout3a3b(7,8))
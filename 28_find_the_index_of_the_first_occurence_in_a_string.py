class Solution(object):
    """
    Given two strings needle and haystack, 
    return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.

    Constraints:

    * 1 <= haystack.length, needle.length <= 104
    * haystack and needle consist of only lowercase English characters.
    """
    def __set_initial_conditions(self, haystack, needle):
        return (len(haystack) >= 1 and
        len(haystack) <= 10000 and
        haystack.isalpha() and haystack.islower() and
        needle.isalpha() and needle.islower())
        
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if self.__set_initial_conditions(haystack,needle):
            if needle in haystack:
                ned_len = len(needle)
                for i,char in enumerate(haystack):
                    if char == needle[0]:
                        for j in range(1,ned_len):
                            if needle[j] != haystack[i+j]:
                                break
                        else:
                            return i
        return -1
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.strStr("anakonda", "kon"))
#solution-01 : use python function
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
      
#solution-02 : check length and then check if count of each letters in string-1 is equal to the count of each letters in string-2
class Solution(object):
    def isAnagram(self, s, t):
        flag = True
        if len(s) != len(t) :
            flag = False
        else :
            for i in s :
                if s.count(i) != t.count(i) :
                    flag = False
                    break
           
        return flag
      

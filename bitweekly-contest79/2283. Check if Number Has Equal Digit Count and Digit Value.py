class Solution(object):
    def digitCount(self, nums):
        """
        :type num: str
        :rtype: bool
        """
        num=[]
        for j in nums:
            num.append(int(j))
        dic={}
        for i in num:
            dic[i]= dic.get(i,0)+1
        count=0
        for k in nums:
            temp=int(k)
            #print(count)
            if count in dic:
                if dic[count] !=temp: 
                    return False
            elif temp>0:
                    return False
            count=count+1
        
        return True
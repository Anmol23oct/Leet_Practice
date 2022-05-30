class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        d={}
        for let in s:
            d[let]=d.get(let,0)+1
        
        d1={}
        for tim in target:
            d1[tim]=d1.get(tim,0)+1

        #print("d",d)
        #print("d1",d1)
        mins=99999
        for ele in d1:
            if ele not in d:
                return 0
            elif (ele in d) and mins>int(d[ele]/d1[ele]):
                #print("ele",ele)
                #print("d[ele]",d[ele])
                #print("d1[ele]",d1[ele])
                mins=int(d[ele]/d1[ele])
        return mins
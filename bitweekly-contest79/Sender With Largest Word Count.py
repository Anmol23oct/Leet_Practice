class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        dic={}
        for (words,sender) in zip(messages,senders):
            
            length=len(words.split())
            #print(length)
            dic[sender]=dic.get(sender,0)+length

        count=0
        ans=''
        for s in senders:
            if dic[s]>count:
                count=dic[s]
                ans=s
            elif dic[s]==count and s>ans:
                ans=s
                
        return ans
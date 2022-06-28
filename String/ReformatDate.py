class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        dic={"Jan":"01","Feb":"02","Mar":"03", "Apr":"04",  "May":"05", "Jun":"06", "Jul":"07",         "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        init=date.split()
        #print(init)
        i=0
        day=str(init[0])
        #print(day)
        while str.isdigit(day[i]):
            b=day[0:i+1]
            #print("b=",b)
            i=i+1
        
        if len(str(b))==1:
            b="0"+str(b)
        
        m=init[1]
        month=-1
        if m in dic:
            month=dic[m]
        
        print("month",month)
        final=str(init[2])+"-"+str(month)+"-"+str(b)
        return final
        
        
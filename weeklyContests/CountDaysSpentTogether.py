class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
#         d={"01":31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30, "07":31, "08":31, "09":30
#           ,"10":31, "11":30, "12":31}
        
#         print(d)
        
#         count=0
        
#         alice={}
        
#         tempAlice=arriveAlice.split('-')
#         print(tempAlice[0])
#         delAlice=leaveAlice.split('-')
#         monthAlice= int(str(tempAlice[0])) - int(str(delAlice[0]))
#         #print(monthAlice)
        
#         tempBob=arriveBob.split('-')
#         print(tempBob[0])
#         delBob=leaveBob.split('-')
#         monthBob= int(str(tempBob[0])) - int(str(delBob[0]))
#         #print(monthBob)
        
#         for months in range(int(str(tempAlice[0])),int(str(delAlice[0]))+1):
#             alice[months]=[]
        
#         i=0
#         for months in range(int(str(tempAlice[0])),int(str(delAlice[0]))+1):
            
#             if i==0:
#                 for days in range(int(str(tempAlice[1])),int(str(d[tempAlice[0]]))+1):
#                     alice[months].append(days)
                
#                 for days in range(int(str(tempAlice[1])),int(str(d[tempAlice[0]]))+1):
#                     alice[months].append(days)
#                 i+=1
#             else:
                
                
        
#         print(alice)
#         bob={}
#         for months in range(int(str(tempBob[0])),int(str(delBob[0]))+1):
#             bob[months]=[]
        
#         for months in range(int(str(tempBob[0])),int(str(delBob[0]))+1):
#             for days in range(int(str(tempBob[1])),int(str(d[tempBob[0]]))+1):
#                 bob[months].append(days)
        
        
#         def intersection(lst1, lst2):
#             return list(set(lst1) & set(lst2))
#         count=0
#         for ele in alice:
#             if ele in bob:
#                 count+=len(intersection(alice[ele],bob[ele]))
        
#         return count

        ls = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def transform(s):
            m,d = s.split("-")
            m = int(m)
            d = int(d)
            res = 0
            for i in range(m-1):
                res += ls[i]
            res += d
            return res
        w,x,y,z = transform(arriveAlice), transform(leaveAlice), transform(arriveBob), transform(leaveBob)
        print("w",w)
        print("x",x)
        print("y",y)
        print("z",z)
        if x<y or z<w:
            return 0
        return max(min(x,z)-max(w,y)+1,0)


        
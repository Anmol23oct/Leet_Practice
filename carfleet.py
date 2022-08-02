class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair=[[p,s] for p,s in zip(position,speed)]
        # stack=[]
        # arr=sorted(pair,reverse=True)
        # for p,s in arr:
        #     stack.append((target-p)/s)
        #     if len(stack)>=2 and stack[-1]<=stack[-2]:
        #         stack.pop()
        # return len(stack)
        arr=[]
        for pos,speed in zip(position,speed):
            arr.append([pos,speed])
        
        arr=sorted(arr,reverse=True)
        
        print(arr)
        stack=[]
        init=True
        for pos,speed in arr:
            
            if init:
                t=(target-pos) / speed
                sep=(target-pos)
                #print(sep/speed)
                stack.append([pos,t])
                #print("s",speed)
                #print("p",pos)
                init=False
            else:
                told=stack[-1][1]
                #print("old",told)
                #print("s",speed)
                #print("p",pos)
                tnew=(target-pos)/speed
                #print("tnew",tnew)
                if tnew>told:
                    stack.append([pos,tnew])
        
        return len(stack)
        
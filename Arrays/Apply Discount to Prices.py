sentence = "there are $1 $2 and 5$ candies in the shop" 
discount = 50

lisent=sentence.split()
print(lisent)
final=""
for ele in lisent:
    if ele[0]=="$":
        num=int(ele[1:])
        print("before",num)
        num=num-discount/100*num
        print("after",num)
        ele="$"+str(num)
        #print(ele)
        
    final=final+ele+" "

print(final)

        
import detect_mask_video as dt

arr = dt.mailrun()
n = len(arr)
mailstring = "Wore the mask properly"
def getMaxLength(arr, n): 
    count = 0 
    result = 0 
  
    for i in range(0, n): 
        if (arr[i] == 0): 
            count = 0
        else: 
            count+= 1 
            result = max(result, count)  
          
    return result  
  
  
maxlen = getMaxLength(arr, n)
if maxlen>=20:
	mailstring = "Defaulted on the mask"

f = open("check.txt", "w")
f.write(mailstring)
f.close()

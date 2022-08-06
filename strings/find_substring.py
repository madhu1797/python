def count_substring(string, sub_string):
    count = 0
    sub = ''
    sub_len= len(sub_string)
    print(sub_len) 
    for i in range (len(string)-1, 0, -1):
         sub = str(string[i])
         a = i  
         if i != 0:
            for j in range (sub_len, 1, -1):
                a = a - 1
                print ("********",string[a])
                sub= str(sub) + str(string[a])
            if sub_string == sub:
                count += 1 
            else:
                count = count 	
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

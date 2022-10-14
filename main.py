def count_substring(string, sub_string):
    count = 0
    
    while len(string) != 0:
        if string.find(sub_string) != -1:
            count += 1
            string = string[(string.find(sub_string))+1:]
        else:
            break
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

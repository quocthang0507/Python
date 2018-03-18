def has_no(word,char_avoid):
    return not(char_avoid in word)

def main():
    str_avoid=input("Enter a string which contains avoided char:")
    fin=open("E:\OneDrive\Thang\HOC TAP\GIAO TRINH\Python\ThinkPython\code\words.txt")
    count=0
    for line in fin:
        word=line.strip()
        for char in str_avoid:
            if(has_no(word,str(char).lower) and (has_no(word,str(char).upper))):
                count+=1
    return print(count)

main()
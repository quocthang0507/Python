def main():
    fin=open("E:\OneDrive\Thang\HOC TAP\GIAO TRINH\Python\ThinkPython\code\words.txt")
    total=0
    total_not_e=0
    for line in fin:
        word=line.strip()
        total+=1
        if(not('e' in word or 'E' in word)):
            total_not_e+=1
    ratio=total_not_e/total*100
    print("Total words:",total)
    print("Words don't have 'e':",total_not_e)
    print(ratio,'%')

main()
def main():
    fin=open("E:\OneDrive\Thang\HOC TAP\GIAO TRINH\Python\ThinkPython\code\words.txt")
    for line in fin:
        word=line.strip()
        if(len(word)>20):
            print (word)

main()
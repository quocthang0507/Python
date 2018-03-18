def main():
    string=input("Please enter a string: ")
    outfile=open("E:\OneDrive\Thang\HOC TAP\Python\output.txt","w")
    print(string,file=outfile)
    outfile.close()
    print("Your string has been written to",outfile)

main()

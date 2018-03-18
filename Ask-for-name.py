from tkinter.filedialog import askopenfilename

def main():
    infileName=askopenfilename()
    infile=open(infileName,"r")
    data=infile.read()
    print(data)
    outfile=open(infileName,"w")
    print("Hello",file=outfile)
    infile.close()
    outfile.close()

main()
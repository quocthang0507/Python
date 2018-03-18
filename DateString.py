def main():
    dateStr=input("Enter a date (mm/dd/yyyy): ")
    monthStr, dayStr, yearStr=dateStr.split("/")
    print ("Date in VN: "+dayStr+"/"+monthStr+"/"+yearStr)

main()
def main():
    kyTu=input("Nhập vào chuỗi ký tự: ")
    print("Đây là mã Unicode:")
    for kt in kyTu:
        print(ord(kt),end=" ")
    print()

main()
class SinhVien:
    'Document string tai day'

    soluong = 0

    def __init__(self, ten, lop):
        self.ten = ten
        self.lop = lop
        SinhVien.soluong += 1

    @staticmethod
    def xuatSoLuong():
        print('So sinh vien hien co la {}'.format(SinhVien.soluong))

    def xuatSinhVien(self):
        print('Ho va ten: ', self.ten, 'Lop: ', self.lop)

import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Khai báo lớp SinhVien
class SinhVien:
    def __init__(self, id, ten):
        self.id = id
        self.ten = ten
        self.diem = {}

    def themDiem(self, monHoc, diem):
        self.diem[monHoc] = diem

    def tinhGPA(self):
        tongDiem = sum(self.diem.values())
        soMon = len(self.diem)
        return tongDiem / soMon if soMon else 0

# Khai báo lớp QuanLySinhVien
class QuanLySinhVien:
    def __init__(self):
        self.sinhVien = {}

    def themSinhVien(self, id, ten):
        if id not in self.sinhVien:
            self.sinhVien[id] = SinhVien(id, ten)
        #else:
        #    messagebox.showerror("Error", "Sinh viên đã tồn tại")

    def xoaSinhVien(self, id):
        if id in self.sinhVien:
            del self.sinhVien[id]
        #else:
        #    messagebox.showerror("Error", "Không tìm thấy sinh viên")

    def luuDuLieu(self):
        student_json = []
        for student in self.students:
            student = str(student)
            student_json.append(student)
        with open('sinhvien.json', 'w') as f:
            json.dump(student_json, f)

    def taiDuLieu(self):
        try:
            with open('sinhvien.json', 'r') as f:
                self.students = json.load(f)
        except FileNotFoundError:
            pass
    def capnhatSinhVien(self, id, ten):
        if id in self.sinhVien:
            self.sinhVien[id].ten = ten

    def listSinhVien(self):
        return self.sinhVien.values()

    def sapxepSinhVientheoten(self):
        return sorted(self.sinhVien.values(), key=lambda s: s.name)

    def sapxepSinhVientheogpa(self):
        return sorted(self.sinhVien.values(), key=lambda s: s.tinhGPA(), reverse=True)

    def timSinhViendiemcaonhat(self):
        return max(self.sinhVien.values(), key=lambda s: s.tinhGPA(), default=None)

# Tạo giao diện sử dụng Tkinter
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý Sinh viên")
        self.geometry("900x450")
        self.quanLy = QuanLySinhVien()

        self.button_them = tk.Button(self, text="Thêm sinh viên", command=self.them_sinh_vien)
        self.button_xoa = tk.Button(self, text="Xóa sinh viên", command=self.xoa_sinh_vien)

        self.button_them.pack()
        self.button_xoa.pack()

    def them_sinh_vien(self):
        id = tk.simpledialog.askstring("Thêm sinh viên", "Nhập ID sinh viên")
        name = tk.simpledialog.askstring("Thêm sinh viên", "Nhập tên sinh viên")
        self.quanLy.themSinhVien(id, name)
        messagebox.showinfo("Thành công!", "Thêm sinh viên thành công!")
        
    def xoa_sinh_vien(self):
        id = tk.simpledialog.askstring("Xoá sinh viên", "Nhập ID sinh viên")
        name = tk.simpledialog.askstring("Xoá sinh viên", "Nhập tên sinh viên")
        self.quanLy.xoaSinhVien(id, name)
        messagebox.showinfo("Thành công!", "Xoá sinh viên thành công!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()


class student:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def printinfo(self):
        print(f"Name: {self.name} - Age: {self.age} - Class: {self.class_}")

#Nhập thông tin sinh viên
student_A = student(name = "Nguyễn Văn A", age = "6 tuổi", class_= "Lớp 1A3")

#In thông tin ra màn hình
student_A.printinfo()

#Chuyển lớp
student_A.class_ = "Lớp 1A7"

#In lại thông tin
print("Sau khi chuyển lớp:")
student_A.printinfo()

#Xóa thông tin
del student_A

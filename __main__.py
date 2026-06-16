import sqlite3

class student:
    def __init__(self):
        self.serv = sqlite3.connect("std_ser.db")
        self.curser = self.serv.cursor()
        self.curser.execute("""CREATE TABLE IF NOT EXISTS std_data(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            age INTIGER,
                            marks INTIGER,
                            grade TEXT ) """)
    
    def added(self,name,age,marks,grade):
        self.curser.execute("insert into std_data (name,age,marks,grade) values (?,?,?,?) ", (name,age,marks,grade))
        self.serv.commit()
        print("Student Added Successfully")

    def add_function(self):
        name = input("Enter the name of students: ")
        age = int(input("Enter the age of students: "))
        marks = int(input("Enter the marks of students: "))
        if 100 >= marks >= 95 :
            self.added(name,age,marks,'A+')
        elif 95 >= marks >= 85:
            self.added(name,age,marks,'A')
        elif 85 >= marks >= 80:
            self.added(name,age,marks,'B+')
        elif 80 >= marks >= 75:
            self.added(name,age,marks,'B')
        elif 75 >= marks >= 70:
            self.added(name,age,marks,'C')
        else:
            self.added(name,age,marks,'D')

    def view(self):
        self.curser.execute("SELECT * FROM std_data")
        dta = self.curser.fetchall()
        for line in dta:
            if line[3] < 33:
                print(f"id: {line[0]},name: {line[1]},age: {line[2]},marks: {line[3]},grade: {line[4]} = YOU have Failed")
            elif line[3] >= 33:
                print(f"id: {line[0]},name: {line[1]},age: {line[2]},marks: {line[3]},grade: {line[4]} = YOU have Passed")
    
    def search(self):
        name = input("Enter the name of the students: ")
        id = input("Enter id of the students: ")
        self.curser.execute("SELECT * FROM std_data where id = ? AND name = ?",(id,name))
        dta = self.curser.fetchone()
        try:
            print(f"id: {dta[0]},name: {dta[1]},age: {dta[2]},marks: {dta[3]},grade: {dta[4]}")
        except Exception as e:
            print("sir enter a valid namee,id")
    
    def update_marks(self):
        name = input("Enter the name of the students: ")
        id = input("Enter id of the students: ")
        marks = int(input("Enter new marks of the students: "))
        self.curser.execute("UPDATE std_data SET marks = ? WHERE id=? AND name=?",(marks,id,name))
        self.serv.commit()
        print('updated succesfully')
    
    def delet_std(self):
        name = input("Enter the name of the students: ")
        id = input("Enter id of the students: ")
        self.curser.execute("DELETE FROM std_data WHERE name=? AND id=?   ",(name,id))
        self.serv.commit()
        print('deleted succcesfully')
    
    def show_topers(self):
        self.curser.execute("SELECT * FROM std_data ORDER BY marks DESC")
        dta = self.curser.fetchmany(10)
        for line in dta:
            print(f"id: {line[0]},name: {line[1]},age: {line[2]},marks: {line[3]},grade: {line[4]}")

    def avg_marks(self):
        self.curser.execute("SELECT marks FROM std_data")
        dta = self.curser.fetchall()
        marks_all = 0
        for line in dta:
            marks_all += line[0]
            # print(f"id: {line[0]},name: {line[1]},age: {line[2]},marks: {line[3]},grade: {line[4]}")
        print(f'the average is: {marks_all/len(dta)}')

if __name__ =="__main__":
    std = student()
    while True:
        arg = input(""" 
        ========== Student Management =========
        1. Add Student
        2. View Students
        3. Search Student
        4. Update Student Marks
        5. Delete Student
        6. Show Topper
        7. Show Average Marks
        8. Exit
        """)

        if arg == '1':
            std.add_function()
        elif arg == '2':
            std.view()
        elif arg == '3':
            std.search()
        elif arg == '4':
            std.update_marks()
        elif arg == '5':
            std.delet_std()
        elif arg == '6':
            std.show_topers()
        elif arg == '7':
            std.avg_marks()
        elif arg == '8':
            std.serv.close()
            break
    
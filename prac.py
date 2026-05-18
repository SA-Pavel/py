from tkinter import * 

student1 = {"name":"Pavel","roll":"265877"}
student2 = {"name":"Sonda","roll":"349385"}

students = [student1,student2]

root = Tk()
root.title("Student search system")
root.geometry("400x350")


Label(root, text="Student information").pack()


def search():
    data = entry.get()
    found = False
    for student in students:
        if (

            student["name"] == data or
            student["roll"] == data 

        ):
            
            result.config(

                text=f"The student name is: {student["name"]} and roll is {student["roll"]}"
            )

            found = True
        



entry = Entry(root)
entry.pack()

Button(root,text="Search",command=search).pack()

result = Label(root, text="")
result.pack()



root.mainloop()



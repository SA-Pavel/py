# tkinter পাইথনের একটা GUI(Graphics User Interface) 
from tkinter import * #এখানে *(স্টার) মানে এর সব কিছু ব্যবহার করব 



#ইনফরমেশন গুলো সাজাবো
student1 = {"name":"Pavel", "roll":"265877","dept":"CST","shift":"2nd"}
student2 = {"name":"Riyad", "roll":"256906","dept":"CST","shift":"2nd"}

#সব ইনফরমেশন গুলো একটা ভেরিয়েবল এর মধ্যে আনব
students = [student1,student2]


root = Tk()
root.title("Student Information")
root.geometry("400x350")

Label(root, text="Student search system",font=("Arial",18,"bold")).pack()

def search():
    data = entry.get()
    found = False
    for student in students:
        if (
            student["name"] == data or
            student["roll"] == data 
        
            ):

            found = True

            result.config(
                text = f"Name: {student["name"]}\n"f"Roll: {student["roll"]}\n"f"Department: {student["dept"]}\n"f"Shift: {student["shift"]}"
            )

            print(f"Student: {student["name"]}\n"f"Roll: {student["roll"]}\n"f"Department: {student["dept"]}\n"f"Shift: {student["shift"]}")
          
        if found == False:
            result.config(text=f"Result is missing")
        


entry = Entry(root, font=("Arial",14))
entry.pack()


Button(root, text="Search", command=search,font=("Arial",12)).pack()

result = Label(root, text="",font=("Arial",12),justify=LEFT)
result.pack()





root.mainloop()
# tkinter পাইথনের একটা GUI(Graphics User Interface) 
from tkinter import * #এখানে *(স্টার) মানে এর সব কিছু ব্যবহার করব 



#ইনফরমেশন গুলো সাজাবো
student1 = {"name":"Pavel", "roll":"265877"}
student2 = {"name":"Saiful", "roll":"414491"}

#সব ইনফরমেশন গুলো একটা ভেরিয়েবল এর মধ্যে আনব
students = [student1,student2]


root = Tk()
root.title("Student Information")
root.geometry("400x350")

Label(root, text="Student search system").pack()

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
                text = f"Name: {student["name"]} Roll: {student["roll"]}"
            )
          
        if found == False:
            result.config(text=f"Result is missing")
        


entry = Entry(root)
entry.pack()


Button(root, text="Search", command=search).pack()

result = Label(root, text="")
result.pack()





root.mainloop()
note = input("Write your note: ")

file = open("data.txt", "a")
file.write(note)
file.write("\n")

file.close()
print("Note saved")
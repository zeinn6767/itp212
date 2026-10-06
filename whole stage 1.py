SIZE = 5
roster = [None] * SIZE
count = 0

print(roster)



def insert_student(name):
    global count

    if count == SIZE:
        print("Overflow! Roster is full. Cannot add", name)
        return

    roster[count] = name
    count = count + 1

    print(name, "added. Roster:", roster)



insert_student("Ana")
insert_student("Ben")
insert_student("Cara")




def delete_student(name):
    global count

    if name not in roster:
        print(name, "not found in roster.")
        return

    index = roster.index(name)

    
    for i in range(index, count - 1):
        roster[i] = roster[i + 1]

    roster[count - 1] = None
    count = count - 1

    print(name, "removed. Roster:", roster)

delete_student("Ben")




insert_student("Dario")
insert_student("Elena")
insert_student("Fred")
insert_student("Gina")



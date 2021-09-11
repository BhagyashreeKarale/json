total=int(input("Enter numer of tasks you want to add:\n"))
not_started = []
in_progress = []
completed = []
for i in range(1,total+1):
    task=input("Enter the task:\n")
    status=int(input("Enter number according to the status of the task\n1.Not started yet\n2.In progress\n3.Completed\n"))
    if status == 1:
        not_started.append(task)
    elif status == 2:
        in_progress.append(task)
    elif status == 3:
        completed.append(task)
    else:
        print("Invalid option selected!")
change=int(input("Enter option number according to the action you want to perform\n1.Show Task\n2.Change Status\n3.Delete Task\n"))
if change == 1:
    show_task=int(input("Enter option number according to the type of tasks you want to see\n1.Not started yet\n2.In progress\n3.Completed\n"))
    if show_task == 1:
        print("Tasks you have not yet started are:")
        for j in not_started:
            print(j)
    elif show_task == 2:
        print("Tasks in progress are:")
        for k in in_progress:
            print(k)
    elif show_task == 3:
        print("Tasks you have completed are:")
        for l in completed:
            print(l)
    else:   
        print("Invalid option number")
elif change == 2:
    current_status=int(input("Enter current status of the task you want to change\n1.Not started yet\n2.In progress\n3.Completed\n"))
    updated_status=int(input("Enter updated status\n1.Not started yet\n2.In progress\n3.Completed"))
    if current_status == 1:
        for m in range(1,len(not_started)+1):
            print(m,not_started[m-1])
        task_to_change=int(input("Enter option number of the task you want to change:\n"))
        for n in not_started:
            if not_started.index(n) == task_to_change-1:
                not_started.remove(n)
                if updated_status == 3:
                    completed.append(n)
                elif updated_status == 2:
                    in_progress.append(n)
                else:
                    print("ERROR")
        print("Status of the selected task is updated successfully.")
    elif current_status == 2:
        for o in range(1,len(in_progress)+1):
            print(o,not_started[o-1])
        task_to_change=int(input("Enter option number of the task you want to change:\n"))
        for p in in_progress:
            if in_progress.index(p) == task_to_change-1:
                not_started.remove(p)
                if updated_status == 1:
                    not_started.append(p)
                elif updated_status == 3:
                    completed.append(p)
                else:
                    print("ERROR")
        print("Status of the selected task is updated successfully.")
    elif current_status == 3:
        for q in range(1,len(completed)+1):
            print(q,completed[q-1])
        task_to_change=int(input("Enter option number of the task you want to change:\n"))
        for r in completed:
            if completed.index(r) == task_to_change-1:
                not_started.remove(r)
                if updated_status == 1:
                    not_started.append(r)
                elif updated_status == 2:
                    in_progress.append(r)
                else:
                    print("ERROR")
        print("Status of the selected task is updated successfully.")
elif change == 3:
    current_status=int(input("Enter current status of the task you want to change\n1.Not started yet\n2.In progress\n3.Completed\n"))
    if current_status == 1:
        for s in range(1,len(not_started)+1):
            print(s,not_started[s-1])
        task_to_delete=int(input("Enter option number of the task you want to delete:\n"))
        for t in not_started:
            if not_started.index(t) ==task_to_delete-1:
                not_started.remove(t)
        print("Selected task is removed successfully.")
    if current_status == 2:
        for u in range(1,len(in_progress)+1):
            print(u,in_progress[u-1])
        task_to_delete=int(input("Enter option number of the task you want to delete:\n"))
        for v in in_progress:
            if in_progress.index(v) == task_to_delete-1:
                in_progress.remove(v)
        print("Selected task is removed successfully.")
    if current_status == 3:
        for w in range(1,len(completed)+1):
            print(w,completed[w-1])
        task_to_delete=int(input("Enter option number of the task you want to delete:\n"))
        for x in completed:
            if completed.index(x) == task_to_delete-1:
                completed.remove(x)
        print("Selected task is removed successfully.")
else:
    print("Invalid option number")



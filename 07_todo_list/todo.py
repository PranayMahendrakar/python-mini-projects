"""Todo List"""
tasks = []

def main():
      while True:
                print("\n1.Add 2.View 3.Complete 4.Quit")
                c = input("Choice: ")
                if c == "1":
                              tasks.append({"task": input("Task: "), "done": False})
elif c == "2":
            for i, t in enumerate(tasks, 1):
                              print(f"{i}. [{'X' if t['done'] else ' '}] {t['task']}")
elif c == "3":
            try:
                              tasks[int(input("Task #: "))-1]["done"] = True
                          except: pass
elif c == "4": break

if __name__ == "__main__": main()

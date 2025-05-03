print(f"{"-"*20} Welcome To Task Tracker {"-"*20}")

data = {}
task = input("Task: ")


with open('data.json',"w") as f:
    f.write(task)
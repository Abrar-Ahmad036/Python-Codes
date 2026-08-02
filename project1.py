tasks=[]
while True:
 print("\n--- Menue ---")
 print("1. View Tasks ")
 print("2. Add Tasks ")
 print("3. exit ")

 choice=input("please select option 1 to 3 : ")

 if(choice=="1"):
  print("These are all tasks :")
  if not tasks:
   print("No task added yet ")
  else:
   for index,task in enumerate(tasks,start=1):
    print(f"{index}. {task}")

 elif(choice=="2"):
  task=input("Enter new task you want to add : ")
  tasks.append(task)
  print("Task add successfully ")

 elif(choice=="3"):
  print("you exit the programm ")
  break
 else:
  print("Invalid choice ")
  


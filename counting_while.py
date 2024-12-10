1.The program will loop infinitely,printing messagrs continuously.

  
2.print("Type in a message, and I'll display it ten times.")

message = input("Message: ")
print()

n = 0
while n < 10:
    print(f"{n + 1}. {message}")
    n += 1


3.print("Type in a message, and I'll display it ten times.")

message = input("Message: ")
print()

n = 0
while n < 100:
    print(f"{n + 10}. {message}")
    n += 10


4.print("Type in a message, and I'll display it ten times.")

message = input("Message: ")
times=int(input("How many times?"))
print()

n = 0
while n < times*10:
    print(f"{n + 10}. {message}")
    n += 10

try:
    with open("example.txt","r") as file:
        content=file.read().strip()
        print(content)
        result=10/0
except Exception as e:
    print("Something went wrong")
print("The file has been closed automatically.")
import file1

print("File2: __name__ var is: %s"%__name__)
if __name__ == "__main__":
    print("File is being run directly")
else:
    print("File is being imported")
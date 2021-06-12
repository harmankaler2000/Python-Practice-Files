print("File1: __name__ var is: %s"%__name__)

if __name__ == "__main__":
    print("This is the main module and is being run directly.")
else:
    print("File is being imported")
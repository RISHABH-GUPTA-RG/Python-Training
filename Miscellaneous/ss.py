import shutil
def print_centre(s):
    print(s.centre(shutil.get_terminal_size().columns))
print_centre()
input()

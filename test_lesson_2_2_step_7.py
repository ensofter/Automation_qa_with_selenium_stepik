import os
print(os.path.abspath(__file__))
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_path = os.path.join(current_dir, 'file.txt')
print(file_path)


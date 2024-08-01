###joining the paths
import os
dir_name="folder"
file_name="file.txt"
full_path=os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)


path="example1.txt"

if os.path.exists(path):
    print(f"the path {path} exist")

else:
    print("less go")

if os.path.isfile(path):
    print(f"the path '{path}' is a file")

elif os.path.isdir(path):
    print(f"the path '{path}' is a directory")


else:
    print(f"the path '{path}' is neither a file nor a directory")

relative_path="example.txt"
aboslute_path=os.path.abspath(relative_path)
print(aboslute_path)
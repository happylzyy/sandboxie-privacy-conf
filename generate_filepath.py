import os

exclude_dirs = [
    "C:\\Windows",
    "C:\\Program Files",
    "C:\\Program Files (x86)",
    "C:\\$Recycle.Bin",
    "C:\\ProgramData",
    "C:\\Sandbox"
]

exclude_dirs2 = [
    "C:\\ProgaramData\\Microsoft"
]

def list_filtered_directories(root_dir, exclude_dirs):
	directories = [os.path.join(root_dir, d) for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
	filtered_directories = [d for d in directories if d not in exclude_dirs]
	return filtered_directories
	
filtered_directories = list_filtered_directories("C:\\", exclude_dirs)
filtered_directories += list_filtered_directories("C:\\ProgramData", exclude_dirs2)

output_file = "output.ini"
with open(output_file, 'w', encoding="UTF-8") as f:
    f.write("## Specified file path for C volume\n")
    for dir_path in filtered_directories:
        f.write(f"WriteFilePath={dir_path}\n")
        
print(f"Output written to {output_file}")

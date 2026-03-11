import platform, sys

with open("os_info.txt", "w") as f:
    f.write(f"OS info is {platform.system()} Python version is {sys.version}")

import os 
import shutil
import psutil


def create_file(file):
    """Create a basic file or import file (future case) 

    Args:
        file (object): file to be created
    """
    code = """print("This is a sample file... ")"""
    try:
        with open(file, "w") as f:
            f.write(code)
        print(f"{file} successfully created")
    except Exception as error:
        print(f"Error creating file: {error}")


def main():
    """Create the sample file

    Args:
        filepath (_type_): _description_
    """
    file_name = "auto_sample_file.py"
    create_file(file_name)
    #call the create_file 
    print(f"Adding {file_name}..")
    find_usb(file_name)
    print(f"Searching for USB...")
    #call find_usb function
    #print(os.cwd()) # get the current working directory

def find_usb_mountpoint():
    """Finds the usb mountpoint. Considerations- MacOs, Linux

    Returns:
        _type_: _description_
    """
    for partition in psutil.disk_partitions():
        if "removable" in partition.opts.lower():
            return partition.mountpoint
    return None

def find_usb(file_name):
    """Find a USB....Move the file.
    """
    #current working directory
    dir_path = os.path.dirname(__file__)
    #Join the file name and the current directory..source to file
    source = os.path.join(dir_path,file_name)
    #destination is the mountpoint
    dest_path = find_usb_mountpoint()
    if not dest_path:
        print("USB Drive not found. Please insert USB drive")
        return None
    
    destination = os.path.join(dest_path,file_name)

    

    try:
        shutil.move(source,destination)
        print(f"File moved successfully to {destination}")
    except FileNotFoundError:
        print(f"Source file {source} not found.")

    except Exception as error:
        print(f"Error moving file: {error}")


if __name__ == "__main__":
    main()

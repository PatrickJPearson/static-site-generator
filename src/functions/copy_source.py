import os
import shutil

def copy_source(dest, source, remove):
    if remove and os.path.isdir(dest):
        shutil.rmtree(dest)
        remove = False
        os.mkdir(dest)
    for item in os.listdir(source):
        dest_path = os.path.join(dest, item)
        source_path = os.path.join(source, item)
        if os.path.isdir(source_path):
            os.mkdir(dest_path)
            copy_source(dest_path, source_path, False)
        else:
            shutil.copy(source_path,dest_path)



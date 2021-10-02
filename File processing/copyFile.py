
#copyFile() = copy content of a file
#copy() = copyfile() + permisson mode + destination can be directory 
#copy2() = copy() + copies metadata (file's creation  and modification times)

import shutil

shutil.copy('Learning/File processing/alive.txt', 'alive2.txt')  #(src path, des path)
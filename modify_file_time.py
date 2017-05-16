"""
将传入文件的创建时间，访问时间，修改时间全改为当前时间


当前脚本的绝对路径：sys.argv[0]
当前脚本的文件名：os.path.basename(sys.argv[0])
当前脚本所在目录：os.path.dirname(sys.argv[0])
"""

import sys

if len(sys.argv)>1:
    import os
    from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
    from win32file import CreateFile,SetFileTime, CloseHandle
    from pywintypes import Time
    import time
    
    fName=sys.argv[1]
    createTime = Time(time.time())
    accessTime = Time(time.time())
    modifyTime = Time(time.time())
    
    
    fh=CreateFile(fName, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
    SetFileTime(fh, createTime, accessTime, modifyTime) 
    
    CloseHandle(fh)



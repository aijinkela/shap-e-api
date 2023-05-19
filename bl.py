import os
import sys
import subprocess

import psutil

def killProcess(processName):
    for proc in psutil.process_iter():
        # print(pid)
        try:
            p = psutil.Process(proc.pid)
            # print(p.name)
            if processName in p.name():
                print(proc.pid)
                print(p.name())
                proc.kill()
                #os.kill(pid,signal.SIGKILL)
                return True  # 如果找到该进程则打印它的PID，返回true
        except Exception as e:
            print(e)
    return False  # 没有找到该进程，返回false

def ply2blend(ply_file, target_blend_file):

    # record.blend_file = 'file.blend'
    # record.save(update_fields=["blend_file"])
    # filename = os.path.join(LOCAL_DATA_DIR,'sketchfab',id,'file.glb')
    # if not os.path.isfile(filename) or True :
    bg_arg = ' --background '
    cmd = 'blender template.blend' + bg_arg + '--python ply2blend.py  -- --ply_file ' + ply_file 
    cmd += ' --target_blend_file ' + target_blend_file
    cmd += ' > ./log.txt'
    if sys.platform != 'win32' and sys.platform != 'darwin':
        cmd = '/usr/bin/xvfb-run -n 0 ' + cmd
    print('#######################################################')
    print(cmd)
    print('#######################################################')
    
    result = 1
    try:
        result = subprocess.call(cmd, shell=True, cwd=".", timeout=60*100)
        killProcess('blender')
        if not os.path.exists(target_blend_file):
            raise Exception('blender convert subprocess error!')
    except Exception as e:
        raise Exception('blender convert subprocess error!')
        
    

import subprocess

def runProc(proc):
    return subprocess.check_output(proc,shell=True)

def findFileNameByExt(str,ext):
    words = str.split(' ')

    for word in words:
        if(word[-len(ext):] == ext):
            return word

    return 'None'

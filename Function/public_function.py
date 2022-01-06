import time
import os

def getCurrentWD():
    return os.getcwd()

def getCurrentTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

def full_mkdir(inputdir):
    if os.path.isdir(inputdir):
        pass
    else:
        os.mkdir(inputdir)

def saveLogText(LogText):
    timestring = getCurrentTime()
    timestring = timestring.replace(':', '-')
    log_wd = getCurrentWD() + "\\log"
    full_mkdir(log_wd)
    filename = getCurrentWD() +  "\\log\\CSDNDownloader" + timestring + ".log"
    with open(filename,mode="w",encoding="utf-8") as f:
        print(f.write('{}'.format(LogText)))
        f.close()

if __name__ == '__main__':
    saveLogText("LogText")

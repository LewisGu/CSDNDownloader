import time
import os

def get_current_wd():
    return os.getcwd()

def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

def full_mkdir(inputdir):
    if os.path.isdir(inputdir):
        pass
    else:
        os.mkdir(inputdir)

def save_log_text(LogText):
    timestring = get_current_time()
    timestring = timestring.replace(':', '-')
    log_wd = get_current_wd() + "\\log"
    full_mkdir(log_wd)
    filename = get_current_wd() +  "\\log\\CSDNDownloader" + timestring + ".log"
    with open(filename,mode="w",encoding="utf-8") as f:
        print(f.write('{}'.format(LogText)))
        f.close()

if __name__ == '__main__':
    save_log_text("LogText")

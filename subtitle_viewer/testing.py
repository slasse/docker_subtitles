import os



path = 'z:/'

def file_list(dir):
    withsubs = []
    withoutsubs = []
    dirname = []
    for dirName, subdirlist, fileList in os.walk(dir):
        dirname.append(dirName)
        for file in os.listdir(dirName):
            if file.endswith(".srt"):
                if dirName not in withsubs:
                    withsubs.append(dirName)
                    break
        else:
            if dirName not in withoutsubs:
                withoutsubs.append(dirName)


    return withsubs, withoutsubs, dirname


files = file_list(path)
print(len(files[0]))
print(len(files[1]))
print(len(files[2]))
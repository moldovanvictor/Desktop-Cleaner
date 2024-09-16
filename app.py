import os
import shutil


def getAllFiles(directory):
    files = os.listdir(directory)
    return files


def makeFolders(dic, directory):
    newdic = {}
    for key in dic:
        folder = os.path.join(directory, key)
        if not os.path.exists(folder):
            os.makedirs(folder)
        newdic[key] = folder
    return newdic


def organizeFiles(directory):
    dic = {}
    files = getAllFiles(directory)
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            dic[os.path.splitext(file)[1]] = []

    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            dic[os.path.splitext(file)[1]].append(file)

    newdic = makeFolders(dic, directory)
    for key in dic:
        for f in dic[key]:
            if not os.path.exists(os.path.join(newdic[key], f)):
                shutil.move(os.path.join(directory, f), os.path.join(newdic[key], f))
            else:
                print(f'A file with name {f} already exists in {newdic[key]}. Please check if it has the same contents. If not, please rename it.')
    print( "Folder organized successfully" )



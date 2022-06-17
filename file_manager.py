import os, shutil

class Format:
    def formatFileSize(size): # Format a number from bytes
        sizeNumber = size
        if size < 1000:
            size = str(size) + ' B'
        elif size in range(1000, 1000000):
            size = size / 1000
            sizeNumber = size
            sizeNumber = '{:.2f}'.format(sizeNumber)
            size = str(sizeNumber) + ' KB'
        elif size in range(1000000, 1000000000):
            size = size / 1000000
            sizeNumber = size
            sizeNumber = '{:.2f}'.format(sizeNumber)
            size = str(sizeNumber) + ' MB'
        elif size in range(1000000000, 1000000000000):
            size = size / 1000000000
            sizeNumber = size
            sizeNumber = '{:.2f}'.format(sizeNumber)
            size = str(sizeNumber) + ' GB'
        elif size > 1000000000000:
            size = size / 1000000000000
            sizeNumber = size
            sizeNumber = '{:.2f}'.format(sizeNumber)
            size = str(sizeNumber) + ' TB'
        return size

class FileManager(Exception): # Errors
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return '{0} '.format(self.message)
        else:
            return 'FileManager error has been raised'

def createFile(path): # Creates a file in the specified path
    try:
        if '.' in path:
            f = open(path, 'x')
        else:
            f = open(str(path + '.txt'), 'x')
        f.close()
    except FileNotFoundError:
        raise FileManager(f'Unknown directory \'{path}\'')
    except FileExistsError:
        raise FileManager(f'File \'{path}\' already exists')

def removeFile(path): # Deletes a specified file
    try:
        os.remove(path)
    except FileNotFoundError:
        raise FileManager(f'Unknown file \'{path}\'')

def renameFile(path, name): # Renames a file
    try:
        os.rename(path, str(name))
    except FileNotFoundError:
        raise FileManager(f'Unknown file \'{path}\'')

def createDirectory(path): # Creates a directory
    try:
        os.mkdir(path)
    except FileExistsError:
        raise FileManager(f'Folder \'{path}\' already exists')

def removeDirectory(path): # Deletes a directory
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        raise FileManager(f'Unknown directory \'{path}\'')

def renameDirectory(path, name): # Renames a directory
    try:
        os.rename(path, str(name))
    except FileNotFoundError:
        raise FileManager(f'Unknown directory \'{path}\'')

def getDirectoryContent(path): # Returns content from a directory
    try:
        files = os.listdir(path)
        return files
    except FileNotFoundError:
        raise FileManager(f'Unknown directory \'{path}\'')

def copyDirectory(path, destination): # Copy a directory to another directory
    try:
        shutil.copytree(path, destination)
    except FileExistsError:
        raise FileManager(f'Destination \'{destination}\' already exists')
    except FileNotFoundError:
        raise FileManager(f'Unknown directory \'{path}\'')

def copyDirectoryContent(path, destination): # Copy content from a directory to another directory
    for i in os.listdir(path):
        try:
            shutil.copy2(os.path.join(path, i), destination)
        except IsADirectoryError:
            folderDirectory = destination + '/' + i
            pathDirectory = path + '/' + i
            copyDirectory(pathDirectory, folderDirectory)

def clearDirectoryContent(path, limit = 1000000): # Clears the content of a specific folder
    for folder, subfolders, files in os.walk(path):
        deletedFiles = 0
        for file in files:
            if deletedFiles < limit:
                deletedFiles += 1
                filePath = os.path.join(folder, file)
                if os.path.isfile(filePath):
                    os.remove(filePath)
                elif os.path.isdir(filePath):
                    shutil.rmtree(filePath)
            else:
                break

def clearFileContent(path): # Clears the content of a file
    try:
        with open(path, 'r+') as f:
            f.truncate(0)
    except FileNotFoundError:
        raise FileManager(f'Unknown directory \'{path}\'')

def readFile(path, line = None): # Reads a file's content
    try:
        if line == None:
            f = open(path)
            return f.read()
        elif type(line) == int:
            try:
                f = open(path)
                lines = f.readlines()
                try:
                    return lines[line - 1]
                except IndexError:
                    raise FileManager(f'Line \'{line}\' is out of range')
            except FileNotFoundError:
                raise FileManager(f'Unknown file \'{path}\'')
        else:
            raise FileManager(f'Line \'{line}\' must be None type or int type. Type: {type(line)}')
    except FileNotFoundError:
        raise FileManager(f'Unknown file \'{path}\'')

def copyFile(path, destination): # Copy a file to another directory
    try:
        shutil.copyfile(path, destination)
    except FileNotFoundError:
        raise FileManager(f'Unknown path \'{path}\' or unknown destination \'{destination}\'')
    except IsADirectoryError:
        raise FileManager(f'Path \'{path}\' is a directory or destination \'{destination}\' is a directory')
    except shutil.SameFileError:
        raise FileManager(f'Destination \'{destination}\' already exists')
    except PermissionError:
        raise FileManager(f'Permission denied')

def writeFile(path, text, line = None, writeType = 'add'): # Writes text inside a file
    try:
        f = open(path)
        lines = f.readlines()
        try:
            if writeType == 'add':
                lines.append(str(text) + '\n')
            elif writeType == 'replace':
                lines[line - 1] = str(text) + '\n'
            elif writeType == 'insert':
                lines.insert(line - 1, str(str(text) + '\n'))
        except IndexError:
            raise FileManager(f'Index \'{line}\' is out of range')

        linesStr = ''
        
        for i in lines:
            linesStr = linesStr + i

        with open(path, 'w') as f:
            f.truncate(0)
            f.write(linesStr)
        f.close()
    except FileNotFoundError:
        raise FileManager(f'Unknown file \'{path}\'')

def clearLine(path, line): # Clears a line inside a file
    try:
        f = open(path)
        lines = f.readlines()
        try:
            lines[line - 1] = '\n'
        except IndexError:
            raise FileManager(f'Line \'{line}\' is out of range')

        linesStr = ''

        for i in lines:
            linesStr = linesStr + i

        with open(path, 'w') as f:
            f.truncate(0)
            f.write(linesStr)
        f.close()
    except FileNotFoundError:
        raise FileManager(f'Unknown file \'{path}\'')

def getFileExtension(path): # Returns the file extension of a directory
    try:
        name, extension = os.path.splitext(path)
        if extension == '':
            return 'directory'
        else:
            return extension[1:]
    except FileNotFoundError:
        raise FileManager(f'Unknown file \'{path}\'')

def getFileSize(path, formatted = False): # Returns the file size of a path
    try:
        f = open(path)
        f.seek(0, os.SEEK_END)
        fileSize = f.tell()
        if formatted == True:
            fileSize = Format.formatFileSize(fileSize)
        return str(fileSize)
    except IsADirectoryError:
        raise FileManager(f'\'{path}\' is a directory')
    except FileNotFoundError:
        raise FileManager(f'Unknown file \'{path}\'')

def getDirectorySize(path, formatted = False): # Returns the file size of a directory
    directory = path.split('/')
    name = directory[-1]
    del directory[-1]
    createZip(path, name, directory)
    size = getFileSize(path)
    return size

def createZip(path, name, destination): # Creates a zip from a directory
    try:
        shutil.make_archive(name, 'zip', path)
        moveFile(str(path + '/' + name + '.zip'), destination)
    except FileNotFoundError:
        raise FileManager(f'Unknown file \'{path}\'')

def findFile(path): # Returns whether a file exists or not
    return os.path.exists(path)

def moveFile(path, destination): # Moves a file to a directory
    try:
        shutil.move(path, destination)
    except FileNotFoundError:
        raise FileManager(f'Unknown path \'{path}\' or unknown destination \'{destination}\'')

def countFiles(file, path = '/'): # Returns the amount of specified files and directories found in the specified directory
    fileCount = 0
    for i in os.walk(path):
        for i in i:
            if file in i:
                fileCount += 1
    return fileCount

def countAllFiles(): # Returns the amount of all files and directories found in the user's computer
    fileCount = 0
    for i in os.walk('/'):
            fileCount += 1
    return fileCount

def getDirectory(): # Returns the directory of the file
    return os.getcwd()

def diskStorageUsed(formatted = False): # Returns the disk storage used
    storageUsed = shutil.disk_usage('/').used
    if formatted == True:
        storageUsed = Format.formatFileSize(storageUsed)
    return storageUsed

def diskStorageTotal(formatted = False): # Returns the total disk storage
    totalStorage = shutil.disk_usage('/').total
    if formatted == True:
        totalStorage = Format.formatFileSize(totalStorage)
    return totalStorage

def diskStorageFree(formatted = False): # Returns the free disk storage
    freeStorage = shutil.disk_usage('/').free
    if formatted == True:
        freeStorage = Format.formatFileSize(freeStorage)
    return freeStorage
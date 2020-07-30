import zipfile, os, shutil

# zips whole directory
print(os.getcwd())
os.chdir('C:\\Users\\pawel\\Desktop')
print(os.getcwd())
def createZip():
    shutil.make_archive('new', 'zip', 'tapety')

def readingZipFiles():
    exampleZip = zipfile.ZipFile('new.zip')
    exampleZip.namelist()
    FileInfo = exampleZip.getinfo('50ifs69e2sg41.jpg')
    FI1 = FileInfo.file_size
    FI2 = FileInfo.compress_size
    print(FI1)
    print(FI2)
    print('Compressed file is %sx smaller.' % (round(FI1 / FI2, 5)))
    exampleZip.close()

def extractZipFile():
    extractZip = zipfile.ZipFile('new.zip')
    extractZip.extractall('tt') #giving value causes python to extract to this folder and create a new one if it doesn't exist
    extractZip.close()

#createZip()
readingZipFiles()
extractZipFile()
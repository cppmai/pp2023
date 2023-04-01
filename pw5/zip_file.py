import os
import zipfile 

# compress 
def compress_file():
    fantasy_zip = zipfile.ZipFile('C:\\Users\\ADMIN\\Desktop\\git\\pp2023\\lab5\\students.zip', 'w')
    # walk through all files and folder in selected path
    for folder, subfolders, files in os.walk('C:\\Users\\ADMIN\\Desktop\\git\\pp2023\\lab5'):
        for file in files:
            # find file txt 
            if file.endswith('.txt'):
                fantasy_zip.write(os.path.join(folder, file), file, compress_type = zipfile.ZIP_DEFLATED)
                # fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Users\\ADMIN\\Desktop\\git\\pp2023\\lab5'), compress_type = zipfile.ZIP_DEFLATED)
 
                os.remove(file)
    fantasy_zip.close()
    print("Compress!!!")


# exactract 
import zipfile
def extract_file():     	
    fantasy_zip = zipfile.ZipFile('C:\\Users\\ADMIN\\Desktop\\git\\pp2023\\lab5\\students.zip')
    fantasy_zip.extractall('C:\\Users\\ADMIN\\Desktop\\git\\pp2023\\lab5')
    fantasy_zip.close()
    os.remove('C:\\Users\\ADMIN\\Desktop\\git\\pp2023\\lab5\\students.zip')
    print("Extract!!!")


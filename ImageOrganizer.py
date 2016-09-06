'''
This script organizes the image and video file based on their 'date taken'. for e.g. Image taken on date 1st January 2016 will be stored
in directory "2016/01/2016_01_01"
'''

import exifread
from os import listdir
from os.path import isfile, join
import os
import sys

source = ('I:\old_fotos\Photos\Sony phone bakup\Photos\Photo\sinhgad trip 02-08-08')
dest = "I:\Canon Photo Library"


def CheckDirectory(fdir,ext):
    if ext == 'raw':
        newpath = join(dest, fdir[:4], fdir[5:7], fdir.replace(':', '_'))
    elif ext == 'mp4':
        newpath= join(dest, fdate[:4], fdate[4:6],fdate[:4] + "_" + fdate[4:6] + "_" + fdate[6:8])

    if not os.path.exists(newpath):
        os.makedirs(newpath)


onlyfiles = [f for f in listdir(source) if isfile(join(source, f))]

for file in onlyfiles:
        fobj= open(join(source, file), "rb")
        name, ext = os.path.splitext(file)
        tags = exifread.process_file(fobj)
        fobj.close()
        fdate=""
        if len(ext.strip()) != 0 and (ext.lower() == '.cr2' or ext.lower() == '.dng' or ext.lower() == '.jpg'):
            try:
                datetime = str(tags['EXIF DateTimeOriginal'])
                fdate, ftime = datetime.split()
                CheckDirectory(fdate,'raw')
                os.rename(join(source, file), join(dest, fdate[:4], fdate[5:7], fdate.replace(':', '_'), file))
                print(file, "= OK")
            except:
                print("\nError saving data in file : %s" % sys.exc_info()[0], sys.exc_info()[1])
                print(join(source, file))
                print(join(source, fdate[:4], fdate[5:7], fdate.replace(':', '_'), file))
        elif ext.lower() == '.mp4':
            try:
                fdate, temp = file.split('_')
                print(file, fdate[:4], fdate[4:6], fdate[6:8])
                CheckDirectory(fdate,'mp4')
                os.rename(join(source, file), join(dest, fdate[:4], fdate[4:6],
                       fdate[:4] + "_" + fdate[4:6] + "_" + fdate[6:8], file))
            except:
                print("\nError saving data in file : %s" % sys.exc_info()[0], sys.exc_info()[1])
                print(join(source, file))
                print(join(dest, fdate[:4], fdate[4:6],
                       fdate[:4] + "_" + fdate[4:6] + "_" + fdate[6:8]))


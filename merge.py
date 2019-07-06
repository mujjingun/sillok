import os
import shutil
import glob

with open('merge.merge', 'w') as outfile:
    for korfile in glob.glob('KOR_*.txt'):
        outfile.write("\n------" + korfile[4:-4] + "\n")
        with open(korfile, 'r') as kr:
            outfile.write(kr.read())
        outfile.write("\n--------\n")
        with open("LZH_" + korfile[4:-4] + ".txt", "r") as lz:
            outfile.write(lz.read())

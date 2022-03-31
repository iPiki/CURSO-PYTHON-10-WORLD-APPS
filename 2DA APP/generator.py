import urllib.request
import cv2
import time
from datetime   import datetime
import pandas

link="https://github.com/iPiki/CURSO-PYTHON-10-WORLD-APPS/raw/main/2DA%20APP/VID_20220318_101454.mp4"
urllib.request.urlretrieve(link,"VIDEO")
video=cv2.VideoCapture("VIDEO")
if video.isOpened()==False:
    print("Archivo no existe")

status_list=[None, None]
tiempos=[]
fps=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
data=pandas.DataFrame(columns=["Inicia","Termina"])
primer_cuadro=None
contador=0

while video.isOpened():

    check, frame=video.read()
    status=0
    contador=contador+1
    if check==True:
        time.sleep(1/fps)
        gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gris=cv2.GaussianBlur(gris,(21,21),0)

        if primer_cuadro is None:
            primer_cuadro=gris
            continue

        cuadro_delta=cv2.absdiff(primer_cuadro,gris)
        desgranar_cuadro=cv2.threshold(cuadro_delta,25,255,cv2.THRESH_BINARY)[1]
        desgranar_cuadro=cv2.dilate(desgranar_cuadro,None,iterations=5)

        (cnts,_)=cv2.findContours(desgranar_cuadro.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour)<5000:
                continue
            (x,y,w,h)=cv2.boundingRect(contour) 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
            status=1

        status_list.append(status)

        status_list=status_list[-2:]

        if status_list[-1]==1 and status_list[-2]==0:
            tiempos.append(datetime.now())
        if status_list[-1]==0 and status_list[-2]==1:
            tiempos.append(datetime.now())
    
        cv2.imshow("Gris",gris)
        cv2.imshow("Cuadro_delta",cuadro_delta)
        cv2.imshow("Desgranar_cuadro",desgranar_cuadro)
        cv2.imshow("Color frame",frame)

        if cv2.waitKey(1) & 0xFF==ord('q') or fps==contador:
            status==1
            tiempos.append(datetime.now())
            break

for n in range(0,len(tiempos),2):
    data=data.append({"Inicia":tiempos[n],"Termina":tiempos[n+1]},ignore_index=True)
print(data)
data.to_csv(r"C:\Users\carlos.gonzalez\Desktop\Tiempos.csv")
video.release()
cv2.destroyAllWindows()
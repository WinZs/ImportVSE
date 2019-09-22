import bpy
import os
from pathlib import Path

##########################################################################################
#################################         PARAMETRES          ############################
##########################################################################################
LeChemin = Path('J:/test')  ### chemin absolu où se trouve la sequence
Piste = 1                   ### strip ou sera ajouté les images
StripStartFrame = 1         ### on insert la séquence à partir de quelle frame dans la TimeLine ? 
StartFrame = 1              ### on démarre à partir de quelle image
NbFrame = 1                 ### Nombre de frame de décalage
DureeFrame = 1              ### Durée en nombre d'images de chaque image insérée

bpy.context.area.type = 'SEQUENCE_EDITOR'
i = 0
j = 1
for root, dirs, files in os.walk(LeChemin, topdown=False):
    for name in files[StartFrame-1:]:
        if not(i%NbFrame):
            bpy.ops.sequencer.image_strip_add(directory=str(LeChemin), files=[{"name":name, "name":name}], show_multiview=False, frame_start=j+StripStartFrame-1, frame_end=j+StripStartFrame-1+(DureeFrame-1), channel=Piste)
            j += 1 + (DureeFrame - 1)
        i += 1
bpy.context.area.type = 'TEXT_EDITOR'

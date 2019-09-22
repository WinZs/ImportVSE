# ImportVSE
Blender 2.8 VSE , Custom import script Image sequence

This script can import images sequence in the Video Sequence Editor (VSE) for Blender 2.8 with custom settings.


##########################################################################################
#################################         PARAMETERS          ############################
##########################################################################################
-LeChemin = Path('J:/test')  ### path where the files are ;  beware of the '/' in the path , even on Windows (do not use '\').
-Piste = 1                   ### strip, where imported images will be placed
-StripStartFrame = 1         ### which frame on the timeline , where images will be imported 
-StartFrame = 1              ### set the start number of image 
-NbFrame = 1                 ### how many frames will be droped (I.E. if set to 10 , only images 1,10,20,30,40... will be imported) 
-DureeFrame = 1              ### How many frame / duration for each imported picture 

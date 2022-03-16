# El codigo necesita las librerias de OpenCV (cv2), os y numpy.
# El código carga las imagenes (png y jpg) que esten en la carpeta
# "data_photos". Después las va mostrando con los siguientes cambios:
# NOTA: Para que se siga ejecutando el código se debe cerrar la ventana de la imagen.
#   - Muestra la imagen original .
#   - Muestra la imagen cuando se aplica un contraste que se controla con la variable "porcentage".
#   - Muestr

############ LIBRERIAS ESTANDAR ###########
import cv2 as cv                                # Open CV
from os.path import dirname, abspath, join      # Libreria os que tiene funciones para manejar carpetas del sistema operativo
import numpy as np                              # Libreria para manejar vectores.



############ FUNCIONES PROPIAS ###########
from aux_function.fastiecm import fastiecm
from aux_function.f_get_files import f_get_files
from aux_function.f_get_metadata import f_get_metadata
from aux_function.f_contrast_stretch import f_contrast_stretch
from aux_function.f_display_image import f_display_image
from aux_function.f_calc_ndvi import f_calc_ndvi


############# EJECUCION CODIGO ##########

####### LEER LA RUTA DE LAS FOTOS ######
current_path = dirname(abspath(__file__))
data_folder = 'data_photos'
path_data = join(current_path, data_folder)

####### OBTIENE EL NOMBRE DE TODOS LOS ARCHIVOS DE IMAGEN ####
files = f_get_files(path_data)

###### OBTIENE LOS DATOS DEL NOMBRE DE LOS ARCHIVOS DE IMAGEN ####
df_data = f_get_metadata(path_data)

##### BUCLE QUE ANALIZA TODAS LAS IMAGENES ENCONTRADAS #####

percentage = 5                                              #CONFIGURA EL PORCENTAJE PARA EL CONTRASTE

for file in files:

    imagen = cv.imread(join(path_data, file))                           # LEE IMAGEN ORIGINAL
    f_display_image(imagen, 'Original')                                 # MUESTRA IMAGEN ORIGINAL          

    contrasted   = f_contrast_stretch(imagen, percentage)               # HACE EL CONTRASTE DE LA IMAGEN ORIGINAL
    f_display_image(contrasted , 'contrasted')                          # MUESTRA IMAGEN ORIGINAL CONTRASTADA

    ndvi = f_calc_ndvi(contrasted)                                      # CALCULA NDVI DE LA IMAGEN CONTRASTADA
    ndvi_contrasted = f_contrast_stretch(ndvi, percentage)              # CONTRASTA LA IMAGEN NDVI
    f_display_image(ndvi_contrasted, 'NDVI Contrasted')                 # MUESTRA IMAGEN NDVI CONTRASTADA

    color_mapped_prep = ndvi_contrasted.astype(np.uint8)                # CONVIERTE LOS NUMERO RGB A UINT8  
    color_mapped_image = cv.applyColorMap(color_mapped_prep, fastiecm)  # CREA MAPA DE COLOR NDVI
    f_display_image(color_mapped_image, 'Color mapped')                 # MUESTRA MAPA DE COLOR NDVI
    
    # cv.imwrite('color_mapped_image.png', color_mapped_image)          # GUARDA IMAGEN (DESCOMENTAR PARA HACERLO)

    print("Procesado de imagen " + file + " hecho correctamente")
    print("Procesado de imagen " + file + " hecho correctamente")


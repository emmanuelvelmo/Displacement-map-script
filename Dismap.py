import os
import cv2
import numpy as np2

print("Place the program next to the directories (containing png files) to generate displacement maps")
input("Press enter to continue...")

#SE OBTIENE LA RUTA DEL PROGRAMA
iter_dir = os.path.dirname(os.path.realpath(__file__))

#SE ITERA EN LOS DIRECTORIOS RECURSIVAMENTE
for dir_it, subdir_it, arch_it in os.walk(iter_dir):
    #SE ACCEDE A CADA ARCHIVO DEL DIRECTORIO
    for arch_n in arch_it:
        #SI ES UN ARCHIVO PNG
        if arch_n.endswith(".png"):
            #CARGAR EL ARCHIVO
            arch_dir = os.path.join(dir_it, arch_n)
            arch_tmp = cv2.imread(arch_dir)

            #CONVERTIR A ESCALA DE GRISES
            arch_tmp_byn = cv2.cvtColor(arch_tmp, cv2.COLOR_BGR2GRAY)

            #CALCULAR EL MAPA DE ALTURA
            alt_map = np2.zeros_like(arch_tmp_byn, dtype = np2.float32)
            
            for cord_y in range(0, alt_map.shape[0] - 1):
                for cord_x in range(0, alt_map.shape[1] - 1):
                    #SE CALCULA DIFERENCIA EN X
                    dx = int(arch_tmp_byn[cord_y, cord_x + 1]) - int(arch_tmp_byn[cord_y, cord_x - 1])
                    #SE CALCULA DIFERENCIA EN Y
                    dy = int(arch_tmp_byn[cord_y + 1, cord_x]) - int(arch_tmp_byn[cord_y - 1, cord_x])
                    #SE CALCULA MAGNITUD DEL GRADIENTE Y SE ASIGNA
                    alt_map[cord_y, cord_x] = 255 - np2.sqrt((dx * dx) + (dy * dy))

            #NORMALIZACIÓN
            alt_map = cv2.normalize(alt_map, None, 0, 255, cv2.NORM_MINMAX)

            #CONVERTIR A ENTERO
            arch_fin = cv2.convertScaleAbs(alt_map)

            #SE SEPARAN EL NOMBRE BASE Y LA EXTENSIÓN DEL NOMBRE DEL ARCHIVO / SE CREAR NUEVO NOMBRE
            arch_base, arch_ext = os.path.splitext(arch_n)
            arch_nv = arch_base + ' (dismap).png'
            
            #RUTA COMPLETA PARA GUARDAR ARCHIVO
            dir_gdr = os.path.join(dir_it, arch_nv)

            #SE GUARDA ARCHIVO
            cv2.imwrite(dir_gdr, arch_fin)

            # IMPRIMIR EL NOMBRE DEL ARCHIVO PROCESADO
            print(arch_n)

input("Press enter to continue...")
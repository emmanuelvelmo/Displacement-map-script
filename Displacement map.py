import os
import cv2

iter_dir = input("Enter path: ")
print("")

cont_arch = 0

# SE ITERA EN LOS DIRECTORIOS RECURSIVAMENTE
for dir_it, subdir_it, arch_it in os.walk(iter_dir):
    # SE ACCEDE A CADA ARCHIVO DEL DIRECTORIO
    for arch_n in arch_it:
        # SI ES UN ARCHIVO png
        if arch_n.endswith(".png"):
            # SE CARGA EL ARCHIVO
            arch_dir = os.path.join(dir_it, arch_n)
            arch_tmp = cv2.imread(arch_dir)

            # SE CONVIERTE A ESCALA DE GRISES
            arch_tmp_byn = cv2.cvtColor(arch_tmp, cv2.COLOR_BGR2GRAY)

            # SE APLICA DESENFOQUE GAUSSIANO PARA SUAVIZAR IMAGEN
            arch_tmp_byn = cv2.GaussianBlur(arch_tmp_byn, (3, 3), 0)

            # SE CALCULA MAPA DE ALTURA CON FILTRO DE SOBEL
            cord_x = cv2.Sobel(arch_tmp_byn, cv2.CV_64F, 1, 0, ksize = 0)
            cord_y = cv2.Sobel(arch_tmp_byn, cv2.CV_64F, 0, 1, ksize = 0)
            alt_map = cv2.magnitude(cord_x, cord_y)
            
            # SE NORMALIZAN VALORES
            alt_map = cv2.normalize(alt_map, None, 0, 255, cv2.NORM_MINMAX)

            # SE CONVIERTEN VALORES A ENTEROS
            arch_fin = cv2.convertScaleAbs(alt_map)

            # SE INVIERTEN COLORES
            arch_fin = 255 - arch_fin

            # SE REEMPLAZA PARTE DEL NOMBRE DEL ARCHIVO
            arch_nv = arch_n.replace(".png", " (dismap).png")
            
            # RUTA COMPLETA PARA GUARDAR ARCHIVO
            dir_gdr = os.path.join(dir_it, arch_nv)

            # SE GUARDA ARCHIVO
            cv2.imwrite(dir_gdr, arch_fin, [cv2.IMWRITE_PNG_COMPRESSION, 9])

            # SE MUESTRA EL ARCHIVO PROCESADO
            print(arch_n)

            cont_arch += 1

print("")
print(f"{cont_arch} generated files.")
input("Press enter to exit...")

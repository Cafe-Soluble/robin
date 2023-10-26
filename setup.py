import shutil
import os

path_start_menu="/mnt/c/Users/Formation/AppData/Roaming/Microsoft/Windows/Start Menu/Programmes/Startup/"
source_file_name="main.lnk"

source_file = os.path.abspath(source_file_name)
try:
    shutil.move(source_file, path_start_menu)
    print(f'Le fichier "{source_file}" a été déplacé avec succès vers "{path_start_menu}".')
except FileNotFoundError:
    print(f'Le fichier "{source_file}" n\'a pas été trouvé dans le répertoire courant.')
except shutil.Error as e:
    print(f'Une erreur s\'est produite lors du déplacement du fichier : {e}')


import os
import winsound
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def play_music(file_name):
    winsound.PlaySound(file_name, winsound.SND_FILENAME)

def set_system_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def unmute_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Vérifiez si le volume est actuellement en mode muet
    if volume.GetMute():
        # Si c'est le cas, désactivez le mode muet
        volume.SetMute(0, None)


if __name__ == "__main__":
    target_volume = 0.45
    music_file = "robin.wav"
    sound_test_file="sound_opening.wav"
    current_directory = os.path.dirname(os.path.realpath(__file__))
    music_path = os.path.join(current_directory, music_file)
    sound_test_path = os.path.join(current_directory, sound_test_file)

    # Obtenir le chemin du répertoire courant
    

def main_func():
    # ACTIVER LE VOLUME 
    try:
        unmute_system_volume()
        print("Volume du système réactivé")
    except Exception as e:
        print(f"Erreur lors de la réactivation du volume : {e}")

# AUGMENTER LE VOLUME A 55% 
    try:
        set_system_volume(target_volume)
        print(f"Volume du système réglé sur {target_volume}")
    except Exception as e:
        print(f"Erreur lors de la configuration du volume : {e}")
           # Chemin complet du fichier audio

# ON JOUE LA MUSIQUE
    try:
        print("Playing the song !")
        play_music(music_path)
    except KeyboardInterrupt:
        print("Arrêt du programme.")
# ON REMET VOLUME A ZERO
    try:
        set_system_volume(0.00)
        print(f"Volume du système réglé sur {0.00}")
    except Exception as e:
        print(f"Erreur lors de la configuration du volume : {e}")
           # Chemin complet du fichier audio



 


print("Starting the troll session")
print("Running the sound test...")
try:
    print("Playing the song !")
    set_system_volume(0.35)
    play_music(sound_test_path)
    print("Sound test is OK.")
except Exception as e:
    print(f"Error: : {e}")
    exit()

print("Script is running !")
while True:
    current_time = time.localtime()
    if current_time.tm_min % 60 == 0:
        main_func()
        time.sleep(61)
    time.sleep(1)  # Attendez une minute avant de vérifier à nouveau
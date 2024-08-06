import multiprocessing
import subprocess
import os

# To run Jarvis
def startJarvis():
    # Code for process 1
    print("Process 1 is running.")
    from main import start
    start()

# To run hotword
def listenHotword():
    # Code for process 2
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()

# Start both processes
if __name__ == '__main__':
    # Define the paths
    base_dirD = os.path.abspath('C:\\Users\\hp\\jarvis-main')
    base_dir = os.path.abspath('C:\\Users\\hp\\jarvis-main\\jarvis-main')
    device_bat_path = os.path.join(base_dirD, 'device.bat')
    audio_dir = os.path.join(base_dir, 'www\\assets\\audio')
    start_sound_path = os.path.join(audio_dir, 'start_sound.mp3')

    # Print the contents of the base directory
    print(f"Contents of {base_dir}:")
    for item in os.listdir(base_dir):
        print(item)

    # Print the contents of the audio directory
    print(f"Contents of {audio_dir}:")
    if os.path.exists(audio_dir):
        for item in os.listdir(audio_dir):
            print(item)
    else:
        print(f"The directory {audio_dir} does not exist.")

    # Check if the paths exist
    if not os.path.exists(device_bat_path):
        raise FileNotFoundError(f"Cannot find 'device.bat' at {device_bat_path}")
    
    if not os.path.exists(start_sound_path):
        raise FileNotFoundError(f"Cannot find 'sound.mp3' at {start_sound_path}")

    # Start the processes
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotword)

    p1.start()
    subprocess.call([device_bat_path])
    p2.start()

    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("system stop")

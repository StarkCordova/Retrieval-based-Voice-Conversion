import os
import shutil
import soundfile as sf

def preprocess_audio_folder(folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(folder):
        if filename.endswith(".wav"):
            path = os.path.join(folder, filename)
            try:
                data, sr = sf.read(path)
                if sr != 40000:
                    print(f"Saltando {filename}, sample rate no válido: {sr}")
                    continue
                shutil.copy(path, os.path.join(output_folder, filename))
                print(f"Copiado: {filename}")
            except Exception as e:
                print(f"Error con {filename}: {e}")

if __name__ == "__main__":
    preprocess_audio_folder("dataset_raw/eliseo", "dataset/eliseo")

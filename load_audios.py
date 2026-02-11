import os
import librosa

# ==== PATH SETTINGS ====
DATA_DIR = "data"
CLEAN_DIR = os.path.join(DATA_DIR, "clean")
NOISE_DIR = os.path.join(DATA_DIR, "noise")

# ==== CONFIG ====
TARGET_SR = 16000  # sample rate

# ==== LOAD CLEAN AUDIOS ====
print("Loading clean audios...")
clean_audios = []

for file in os.listdir(CLEAN_DIR):
    if file.endswith(".mp3"):
        path = os.path.join(CLEAN_DIR, file)
        audio, sr = librosa.load(path, sr=TARGET_SR)
        clean_audios.append(audio)

print(f"Loaded {len(clean_audios)} clean audios ")

# ==== LOAD NOISE AUDIOS ====
print("Loading noise audios (from subfolders)...")
noise_audios = []

for root, dirs, files in os.walk(NOISE_DIR):
    for file in files:
        if file.endswith(".wav"):
            path = os.path.join(root, file)
            audio, sr = librosa.load(path, sr=TARGET_SR)
            noise_audios.append(audio)

print(f"Loaded {len(noise_audios)} noise audios ")

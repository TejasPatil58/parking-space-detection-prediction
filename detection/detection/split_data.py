import os
import shutil
import random

train_path = r"D:\parking-space-detection-prediction\detection\dataset\train"
val_path = r"D:\parking-space-detection-prediction\detection\dataset\valid"

classes = ["empty", "occupied"]

for cls in classes:
    os.makedirs(os.path.join(val_path, cls), exist_ok=True)

    files = os.listdir(os.path.join(train_path, cls))
    random.shuffle(files)

    split = int(0.2 * len(files))  # 20% validation

    for file in files[:split]:
        src = os.path.join(train_path, cls, file)
        dst = os.path.join(val_path, cls, file)

        shutil.move(src, dst)

print("Validation split done!")
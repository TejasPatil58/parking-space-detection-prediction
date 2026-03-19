import os
import shutil

source = r"D:\parking-space-detection-prediction"
target_empty = r"D:\parking-space-detection-prediction\detection\dataset\train\empty"
target_occupied = r"D:\parking-space-detection-prediction\detection\dataset\train\occupied"

os.makedirs(target_empty, exist_ok=True)
os.makedirs(target_occupied, exist_ok=True)

count = 0

for root, dirs, files in os.walk(source):

    # 🔥 VERY IMPORTANT: skip dataset folder to avoid infinite copy
    if "dataset" in root:
        continue

    for file in files:
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            src_path = os.path.join(root, file)

            if count % 2 == 0:
                dst = os.path.join(target_empty, file)
            else:
                dst = os.path.join(target_occupied, file)

            # Avoid same file error
            if not os.path.exists(dst):
                shutil.copy(src_path, dst)
                count += 1

print("DONE! Total images copied:", count)
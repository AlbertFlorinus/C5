import os
import json

"""
this assumes a dir strucutre of

target_dir:
    - blabla.ext
    - ehiughru.ext
    ...
where ext is some image format
"""
target_dir = "hua_images"
s_name = target_dir.split[0]

#this is just preset for groundtruth, otherwise code breaks
placeholder_preset = {"illuminant_color_raw":[0.70450692619758248,0.65185828786184485,0.28062566433856068]}

c = 0
for filename in os.listdir(target_dir):
    new_name = f"field_{c}_sensorname_{s_name}"
    c += 1
    print(new_name+".png")
    os.rename(os.path.join(target_dir, filename), os.path.join(target_dir, new_name + ".png"))
    with open(os.path.join(target_dir, new_name + "_metadata.json"), "w") as f:
        json.dump(placeholder_preset, f)
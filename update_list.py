import time
import os

file_name = "new.m3u"

def update_m3u():
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")

    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()

    timestamp = str(int(time.time()))
    version_tag = f"#EXT-X-VERSION:{timestamp}\n"

    if not lines or not lines[0].startswith("#EXTM3U"):
        lines = ["#EXTM3U\n", version_tag]
    else:
        new_content = [lines[0], version_tag]
        for line in lines[1:]:
            if "#EXT-X-VERSION" not in line:
                new_content.append(line)
        lines = new_content

    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(lines)

if __name__ == "__main__":
    update_m3u()

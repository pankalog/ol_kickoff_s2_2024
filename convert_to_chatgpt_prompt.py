import sys
import os

rootdir = "./trainingData/"

for folder, subs, files in os.walk(rootdir):
    for filename in files:
        print(filename)
        with open(os.path.join(folder, filename), 'r') as src:
            with open(os.path.join(rootdir, "ResearchMethodList.json"), 'a+') as tgt:
                mdString = src.read()
                tgt.write(f""
                          f"")


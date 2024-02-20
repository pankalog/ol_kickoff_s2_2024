import sys
import os

rootdir = "./trainingData/"

for folder, subs, files in os.walk(rootdir):
    for filename in files:
        print(filename)
        with open(os.path.join(folder, filename), 'r') as src:
            with open(os.path.join(rootdir, "trainingDataPrompts.json"), 'a+') as tgt:
                mdString = src.read()
                tgt.write(mdString)


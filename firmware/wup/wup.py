from zipfile import ZipFile
import os, threading
import json

def execute_wup(filepath):
    ZipFile(filepath).extractall("./wup")
    manifest = json.load(open("./wup/manifest.json", "r"))
    os.system("./loadwup.sh")

def load_wup_manifest(filepath):
    ZipFile(filepath).extractall("./wup")
    manifest = json.load(open("./wup/manifest.json", "r"))
    return manifest
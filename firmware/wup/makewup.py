import shutil

output = "../firmware/titles/testgame.wup"

shutil.make_archive(output, "zip", ".")
shutil.move(output + ".zip", output)
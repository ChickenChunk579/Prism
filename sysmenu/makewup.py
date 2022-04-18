import shutil

output = "../firmware/sysmenu.wup"

shutil.make_archive(output, "zip", ".")
shutil.move(output + ".zip", output)
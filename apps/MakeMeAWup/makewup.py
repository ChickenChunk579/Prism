import shutil

output = "../../firmware/titles/MakeMeAWup.wup"

shutil.make_archive(output, "zip", ".")
shutil.move(output + ".zip", output)
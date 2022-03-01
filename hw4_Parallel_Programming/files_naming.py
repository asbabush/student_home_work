def file_naming(index):
    index = str(index)
    file_name_0 = "00000"
    file_name_out = file_name_0[: -(len(index))] + index + ".jpg"
    return file_name_out

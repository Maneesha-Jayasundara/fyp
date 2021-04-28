filenames = ["file1.txt", "file2.txt", "file3.txt"]

with open("output_file.txt", "w") as outfile:
    for filename in filenames:
        with open(filename) as infile:
            contents = infile.read()
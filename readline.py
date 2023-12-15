import time

if __name__ == '__main__':
    while True:
        with open('test.txt', 'r') as f:
            f_content = f.readline()
            if len(f_content) > 12:
                print(f_content.lstrip())
        with open('test.txt', 'r+') as fp:
            # read an store all lines into list
            lines = fp.readlines()
            # move file pointer to the beginning of a file
            fp.seek(0)
            # truncate the file
            fp.truncate()

            # start writing lines except the first line
            # lines[1:] from line 2 to last line
            fp.writelines(lines[1:])
        time.sleep(5)
def read_file_into_lines(file_path, strip=True):
    """
    A simple function to read a file into
    a list of lines, removing the newline
    character (\n) at the end.

    Arguments:
    ==========
    file_path: str
        The location of a text file to read.

    Returns:
    ========
    list[str]
        A list that contains all stripped lines
        of the input text file.
    """
    lines = []
    with open(file_path, 'r') as infile:
        for line in infile.readlines():
            cleaned = line.rstrip()
            lines.append(cleaned)
    return lines


# from Niko's Util
def file_to_list(path, raw=False):
    lines = []
    with open(path, 'r') as infile:
        for line in infile.readlines():
            if raw:
                lines.append(line[:-1])
            else:
                lines.append(line.strip())

    return lines
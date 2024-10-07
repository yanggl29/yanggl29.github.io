# python3 SedImagesUrlForMd.py -d "/path/to/your/dir" -u "https://cdn.jsdelivr.net/gh/yourgithub"

import os
import re
import argparse

IMGPATTERN=r'!\[.*?\]\((.*?)\)|<img.*?src\ *=\ *[\'\"](.*?)[\'\"].*?>'

def getAllMds(dir_name):
    md_files = []
    from fnmatch import fnmatch

    for path, subdirs, files in os.walk(dir_name):
        for name in files:
            if fnmatch(name, "*.md"):
                md_files.append(os.path.join(path, name))
    return md_files

def replaceImgUrl(file_name, prefix):
    content = ""
    with open(file=file_name) as file:
        lines = file.readlines()
        for line in lines:
            urls = re.findall(IMGPATTERN, line)
            urls = [item for t in urls for item in t]
            for url in urls:
                if len(url) != 0 and not url.startswith('http'):
                    new_url = prefix + url.strip()
                    line = line.replace(url, new_url)
            content += line
    with open(file=file_name, mode='w') as file:
        file.write(content)

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('-d', '--dir', help='Directory to sed')
    args_parser.add_argument('-u', '--url', help='Prefix of new img urls')

    args = args_parser.parse_args()

    if (args.dir == None or args.url == None):
        args_parser.print_help()
        exit(1)

    md_files = getAllMds(args.dir)
    
    for file in md_files:
        replaceImgUrl(file, args.url)
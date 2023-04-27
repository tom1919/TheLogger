# -*- coding: utf-8 -*-
'''
TODO: add logging
'''
#%% imports

import os 
import re
import shutil
import subprocess

#%% ver bump
# this breaks after 1000 ver bumps

with open('setup.py', 'r') as f:  setup = f.read()

pattern = r"ver = 'v\d.\d.\d'"
ver = re.search(pattern, setup).group(0)

ver_str = re.search(r"'v(.+)'", ver).group(1)
ver_num = ver_str.replace('.','')
ver_num = ver_num.lstrip("0")

new_ver = str(int(ver_num) + 1)
new_ver = list(new_ver)
while len(new_ver) < 3:
    new_ver.insert(0,'0')

new_ver_str = '.'.join(new_ver)
new_ver_line = f"ver = 'v{new_ver_str}'"

setup = setup.replace(ver, new_ver_line)

ver_bump = input(f"Bump ver from {ver_str} to {new_ver_str}? [y/n]:")
if ver_bump == 'y':
    with open('setup.py', 'w') as f: f.write(setup)

#%% copy folder
# dropbox folder interfers with the build

src_dir = os.getcwd()
dst_dir = f'C:{os.sep}Users{os.sep}tommy'

trgt_dir =  os.path.join(dst_dir, os.path.basename(src_dir))
shutil.copytree(src_dir, trgt_dir)

#%% build

subprocess.check_call(['python', 'setup.py', 'bdist_wheel'], cwd = trgt_dir)

#%% upload

upload = input("Upload to pypi? [y/n]:")

if upload == 'y':
    username = os.getenv('pypi_user')
    password = os.environ.get('pypi_pw')
    subprocess.check_call(['twine', 'upload', '--username', username, 
                           '--password', password, 'dist/*'], cwd = trgt_dir)

#%% delete copied folder

shutil.rmtree(trgt_dir)

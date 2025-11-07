# https://atmarkit.itmedia.co.jp/ait/articles/2510/20/news015.html

import os
user_input = 'hp_kawasaki; touch newfile.txt; ls -l newfile.txt'
cmd_to_exec = f'echo hello {user_input}'
os.system(cmd_to_exec)

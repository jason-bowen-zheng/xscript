#!/usr/bin/python3
# Copyright (C) 2020 hason-bowen-zheng

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import core
import os.path as path
import sys

def main():
    if len(sys.argv) < 2:
        print('xscript: Not enough argument')
        exit(1)
    elif not path.isfile(sys.argv[1]):
        print('xscript: No such file or directory: %s' % sys.argv[1])
        exit(1)
    else:
        source = open(sys.argv[1], 'r+').readlines()
        interpreter = core.XScriptInterpreter(source, argv=sys.argv[1:])
        interpreter.run()

if __name__ == '__main__':
    main()

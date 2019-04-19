# ！/usr/bin/python
#author:xx

import os


def data_dir(dir,data):
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),dir,data)

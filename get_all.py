#!/usr/bin/python3
""" collects all the info"""

from models import get_token
import sys

token = get_token(sys.argv[1], sys.argv[2], sys.argv[3])

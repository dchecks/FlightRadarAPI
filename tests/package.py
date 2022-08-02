# -*- coding: utf-8 -*-

import os, sys

current_dir = os.getcwd()
sys.path.append(current_dir)

from flightradar24 import __version__ as version
from flightradar24.api import FlightRadar24API
from flightradar24.core import Core

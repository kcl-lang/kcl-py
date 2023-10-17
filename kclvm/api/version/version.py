# Copyright 2021 The KCL Authors. All rights reserved.

import os
from pathlib import Path

VERSION = "0.6.0"
CHECKSUM = Path(os.path.dirname(__file__)).joinpath("checksum.txt").read_text().strip()

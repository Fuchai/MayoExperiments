import sys
from pathlib import Path
import os
thispath=Path(os.path.realpath(__file__))
sys.path.append(thispath.parent.parent/"pretrained")
sys.path.insert(0,thispath.parent.parent.parent)
for i in sys.path:
	print(i)




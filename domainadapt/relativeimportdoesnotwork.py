from .DNC.archi.controller import Controller
'''
ssh://xxx@infodev6:22/home/xxx/.conda/envs/jason2/bin/python -u /home/xxx/git/mayoexperiments/domainadapt/relativeimportdoesnotwork.py
Traceback (most recent call last):
  File "/home/xxx/git/mayoexperiments/domainadapt/relativeimportdoesnotwork.py", line 1, in <module>
    from .DNC.archi.controller import Controller
ModuleNotFoundError: No module named '__main__.DNC'; '__main__' is not a package

Process finished with exit code 1
'''

ctrl=Controller()

# I gotta rewrite my DNC code to make it backward compatible.
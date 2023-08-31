from pathlib import Path
path = 'mail'
if(Path.rmdir(path)):
    print('file created')
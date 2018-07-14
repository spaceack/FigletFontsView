import os, sys
fonts_path = sys.argv[1] if len(sys.argv) == 2 else './fonts'
for _, _, filenames in os.walk(fonts_path):
    for f in filenames:
        if f.split('.')[-1] == 'flf':
            os.system('echo "{}"'.format(f))
            os.system('echo "<pre>"')
            os.system('figlet -f {} Embrace 2018'.format(f))
            os.system('echo "</pre>"')

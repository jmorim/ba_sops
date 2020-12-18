import pypandoc
import os

#folder_list = os.listdir('.')
folder_list = next(os.walk('.'))[1]
folder_list.remove('.git', 'templates')
file_types = ['html', 'pdf', 'docx']

for folder in folder_list:
    for filetype in file_types:
        output = pypandoc.convert_file(paste('.\\', folder, '\\', folder, '.md',
                format = 'filetype',
                #outputfile = 'countess\\countess.pdf',
                outputfile = paste(folder, '\\', folder, '.', filetype),
                extra_args = ['--template ..\templates\template.latex',
                    '--variable urlcolor=cyan',
                    '-c ..\templates\github.css']
#ouput = pypandoc.convert_file('.\\countess\\countess.md', 'docx',
#        outputfile='countess\\countess.docx')

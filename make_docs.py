import pypandoc
import os

# Working commands ------------------------------------------------------------
## pdf
### pandoc -o countess.pdf --template ../templates/template.latex countess.md
### --variable urlcolor=cyan
## html
### pandoc -s -o countess.html -c ../templates/github.css countess.md
### --variable urlcolor=cyan
## docx
### pandoc -o countess.docx countess.md --variable urlcolor=cyan
#------------------------------------------------------------------------------

#folder_list = os.listdir('.')
folder_list = next(os.walk('.'))[1]
folder_list.remove('.git')
folder_list.remove('templates')
#file_types = ['html', 'pdf', 'docx']
file_types = ['pdf']
#pdoc_args = ['--template .\\templates\\template.latex',
#        '--variable urlcolor=cyan',
#        '-c .\\templates\\github.css']
pdoc_args = ['-s',
            '-c ..\\templates\\github.css']
#            '--template ..\\templates\\template.latex',
#            '--variable urlcolor=cyan']

for folder in folder_list:
    print(folder)
    os.chdir(folder)
    for filetype in file_types:
        print('Selected filetype: ' + filetype)
        md_file = '.\\' + folder + '.md'
        print('Converting ' + md_file)
        output_file = '.\\' + folder + '.' + filetype
        print('Saving output as: ' + output_file)

        output = pypandoc.convert_file(
                md_file,
                to = filetype,
                outputfile = output_file,
                extra_args = pdoc_args
                )
    os.chdir('..')

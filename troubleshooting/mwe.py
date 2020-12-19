import pypandoc

output = pypandoc.convert_file(
        'test.md',
        to = 'pdf',
        outputfile = 'test.pdf',
        extra_args = ['template template.latex']
        )

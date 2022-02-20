from shell import shell
ls = shell('id root')
for file in ls.output():
    print (file)
def parsing_fasta():
    '''
    This function allows to read a fasta file line by line and prints out the source organism
    and the sequence length for the records that are not from Homo sapiens.
    First it is necessary to open the input file and the output file, then line by line is checked
    if there is the string 'Homo sapiens', and if it is true this line is written (that represents
    the heading). Then all the sequence is stored until another heading doesn't come out. When this
    occurs, the source organism and the sequence length of that record is printed out.
    In the end the output file is closed
    '''
    file=open('sprot_prot.fasta')
    output=open("ouptut.txt","w+")
    stringa=''
    for line in file:
        if line.startswith('>') and ('Homo sapiens' not in line):
            source=''
            source=line.split('OS=',1)[1].split(' GN=',1)[0]
            output.write(line)
            l=file.readline()
            while not '>' in l:
                stringa=stringa+l.strip()
                output.write(l)
                l=file.readline()
                if '>' in l:
                    print("The source organism is '%s' and the sequence length is %d" %(source,len(stringa)))
                    stringa=''
    output.close()

parsing_fasta()

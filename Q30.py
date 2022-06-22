# This program is for the calculation of %Q30 in fastq files.
import sys

def main():
    # Check if there is one parameter in the command line
    print("Notice: It is only suitable for fastq file with Phred+33!")
    if len(sys.argv)!=2:
        print("Please enter like: python Q30.py xxx.fastq, or python Q30.py xxx.fq")
    else:
        infilename=sys.argv[1]
        # Check if the input file format is fastq
        if infilename.endswith('.fq') or infilename.endswith('.fastq'):
            print(f'%Q30: {findQ30(infilename):.2f}')
        else:
            print("Please enter like: python Q30.py xxx.fastq, or python Q30.py xxx.fq")




# This function is used for %Q30 calculation
def findQ30(infilename):
    q_tot=0   #total number of q, start from 0
    q30_count=0  # total number of q that q>30, start from 0
    with open(infilename,'r') as infile:
        # Read the first line
        line=infile.readline()
        while line!='':
            if line.startswith('+'):
                # If line starts with '+', use next line as the quality sequence
                qseq=infile.readline().strip()
                q_tot+=len(qseq)
                for character in qseq:
                    # Add Q30 counts
                    if ord(character)-33>=30:
                        q30_count+=1
            # Read next line
            line = infile.readline()
        return q30_count/q_tot*100





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



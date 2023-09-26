f=open("dna.example.fasta")
s=dict()
for line in f:
    line=line.rstrip()
    if line.startswith('>'):
        head=line.split()
        k=head[0]
        s[k]=" "
    else:
        s[k]=s[k]+line

for key,val in s.items():
    print(key,'\n',val)

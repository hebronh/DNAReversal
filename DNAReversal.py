dnaCodes = 'ACGT'
#rnaCodes = 'UGCA'

dna = input('Enter a dna sequence:  ') 

invdna = input('Enter the pattern:    ')
l = []

pre = dna[:4]
print('Prefix: ', pre.upper())  

mrk = invdna
print('Marker: ',invdna) 

x = len(dna) 
y = x//2  
Middle = dna[y-3]+dna[y-2]+dna[y-1]+dna[y]+dna[y+1]
print('Middle: ', Middle)
  
rvrmid = Middle[::-1] 
print('Reversed Middle:', rvrmid.upper())

rvrmark = invdna[::-1] 
print('Reversed Marker: ', rvrmark)

suf = dna[-5:] 
print('Suffix: ', suf.upper()) 

print('Result: ', pre+mrk+Middle+rvrmid+rvrmark+suf)

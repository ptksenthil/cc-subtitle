from lxml import etree

doc=etree.parse(r'C:\Users\dsk\Desktop\timedtext.xml')

tt=doc.xpath('//p/@t')
dd=doc.xpath('//p/@d')
words=doc.xpath('//p/text()')

n=len(tt)

def timm(a):
    s=int(a)/1000
    m,s=divmod(s,60)
    h,m=divmod(m,60)
    st=float(s)
    s2=format(st,'.3f')
    m2=int(m)
    h2=int(h)
    s3=str(s2)
    m3=str(m2)
    h3=str(h2)
    i=s3.index('.')
    s4=s3.replace('.',',')
    m4=m3.zfill(2)
    h4=h3.zfill(2)
    return h4,m4,s4
        
i=0
print ("the value of n",n)
f=open(r'C:\Users\dsk\Desktop\sub.srt','w')
while i <=(n-1):

    f.write(str(i+1)+'\n')
    h,m,s=timm(tt[i])
    a=int(tt[i])
    b=int(dd[i])
    h2,m2,s2=timm(a+b)
    c=h+":"+m+":"+s+' --> '+h2+":"+m2+":"+s2
    f.write(c+'\n')
    f.write(words[i]+'\n')
    f.write('\n')
    i=i+1

f.close()



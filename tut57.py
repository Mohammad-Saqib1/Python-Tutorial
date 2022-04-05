
#if you want to print regular string
import re
mystr ='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiiin'''
#some function{findall,search ,split,sub , finder}

# {print same type string}patt=re.compile(r'fass')
# patt=re.compile(r'.adm')
# patt=re.compile(r'^Tata')#start with Tata
# patt=re.compile(r'iin$')#end with iin
# patt=re.compile(r'ai{2}')#exactly specified number
# patt=re.compile(r'ai{2}')#exactly specified number
# patt=re.compile(r'ai{1}|Fax')#Either or

# patt=re.compile(r'ai{1}|Fax')#Either or
#special sequence
patt=re.compile(r'Fax\b')#return special char which beggining this name(Fax)
patt=re.compile(r'27\b')#return special char which beggining this name(Fax)
patt=re.compile(r'\d{5}-\d{4}')#return digits
#Any more special sequence and regular exprssn on internet
matches=patt.finditer(mystr)
for match in matches:
    print(match)
import base64
import des

with open("images/test3.png", "rb") as imageFile:
    img_byte = base64.b64encode(imageFile.read())
    #print(type(img_byte))
    img_str = img_byte.decode("utf-8")
    #print(type(img_str))
    #print((img_str))
    
len_img_str = len(img_str)    
img_bin=''.join(format(ord(x), '07b') for x in img_str)
#print(type(img_bin))

#print(img_bin)

#print(img_bin)
len_img_bin= len(img_bin)
img_bin_temp = img_bin

#print(str_bin)
#print(len_img_bin)
pad_len = 64 - len_img_bin%64
for i in range(pad_len):
    img_bin+='0'
pad_export = str(pad_len)
#print(pad_export)
#print(len(img_bin))

img_hex = '%0*X' % ((len(img_bin) + 3) // 4, int(img_bin, 2))

#print(len(img_hex))
## 21472
#print(img_hex)
img_enc=""
K = '133457799BBCDFF1'

for i in range(0,len(img_hex),16):
    img_enc=img_enc + des.encrypt(img_hex[i:i+16],K)

#print((img_enc))
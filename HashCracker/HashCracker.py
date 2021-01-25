import hashlib
flag = 0
pass_hash = input("Enter Hash: ")
wordlist = input("Enter file name : ")
try:
  pass_file = open(wordlist,'r')
except:
  print("No file")
  quit()
for word in pass_file:
  encwrd = word.encode('utf-8')
  digest = hashlib.md5(encwrd.strip()).hexdigest()
  if digest == pass_hash:
    print("Password found!")
    print("Password is "+ word)
    flag = 1
    break
if flag == 0:
  print("password/passhash not in the list")

# PythonOTP
This is a simple OTP (One Time Pad) encryption program for encrypting/decrypting text.
This is writen in python 2.7 it will not work in python3!

## Settings
```
  -h, --help            show this help message and exit
  -v, --view            Print key and fine details to screen
  -e, --encrypt         Encrypt mode
  -ko KEYOUT, --keyout KEYOUT
                        Output file name for your one time pad key. Default
                        filename is pad.key
  -do DATAOUT, --dataout DATAOUT
                        Output file name for your encrypted data. Default will
                        just print it to the screen
  -da DATA, --data DATA
                        Text you want to encrypt. Put data in quotes to avoid
                        problems. If this argument is not used then you will
                        be promoted an area to enter data
  -d, --decrypt         Decrypt mode
  -kf KEYFILE, --keyfile KEYFILE
                        File with your key stored in it. If a file is not
                        specified the default file name 'pad.key' will be used
  -ef ENFILE, --EnFile ENFILE
                        File with your encrypted data. If a file is not
                        specified you will be promoted an area to enter it
  -DD ENCRYPTEDDATA, --encryptedData ENCRYPTEDDATA
                        Text you want to decrypt. Put data in quotes to avoid
                        problems. If this argument is not used then you will
                        be promoted an area to enter data
```

### Examples
#### All of the decryption exmaples wont work because you dont have the same private key as me unless you use your own data and private key.

##### Basic encrypting
```
python OneTimePad.py -e -da "Wow this really works does it?"
```
The following data will be return to you

```
Generating random one time pad...
You entered "Wow this really works does it?", now encrypting this data with the generated key 
----DATA BEGIN----
 5776 8453 3968 4153 9209 1283 5971 9197 2862 9244 5444 9782 4153 1543 3350 3968 8780 8428 3079 9244 1283 9292 842 5035 2862 9244 4921 851 1283 6412 377 8297 8780 9244 842 8714 4153 1178 4035 9782 4153 4153 4821 5320 6551 2862 1817 842 5252 903 8593 4493
----DATA END----
```

###### Basic decrypting
```
python OneTimePad.py -d -DD "5776 8453 ..."
```
This will return
```
Decrypting data...
Decrypted data: Wow this really works does it?
```
##### Custom key filenames
To use a custom filename for the private key you must use -ko to define the filename
```
python OneTimePad.py -e -da "Wow this really works does it?" -ko keypass.key
```
This will save the decryption key to 'keypass.key'

To use a custom key filename to decrypt you have to use -kf or --keyfile
```
python OneTimePad.py -d -DD "5776 8453 ..." -kf keypass.key
```



## Author

* **Keegan Currie** - [My Profile](https://github.com/therealkeeg1)


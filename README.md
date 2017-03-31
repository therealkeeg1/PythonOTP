# PythonOTP
This is a simple OTP (One Time Pad) encryption program for encrypting/decrypting text.
This program is writen in python 2.7 it will not work in python3!

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
#### All of the decryption exmaples wont work because you dont have the same private key as me unless you use your own data and private key. By default the private key is saved as 'pad.key' and is created everytime the encryption mode is ran. It will overwrite itself, so create backups if you want to save the data.

##### Detailed view
To use the detailed view mode do -v or --view. This command will print out extra data that some users might find useful or intresting.
```
python OneTimePad.py -e -da "Wow this really works!" -v
```
Or
```
python OneTimePad.py -d -DD "5776 8453 ..." -v
```

##### Basic encrypting
```
python OneTimePad.py -e -da "Wow this really works!"
```
The following data will be return to you.

```
Generating random one time pad...
You entered "Wow this really works!", now encrypting this data with the generated key 
----DATA BEGIN----
 1065 3926 5753 7617 4932 4609 3191 5488 3225 3244 4687 1467 7617 1342 8728 5753 8295 6214 1412 3244 4609 2010 3635 8338 3225 3244 764 7589 4609 7176 7613 1332 7928 7066 7928 1065 4787 1597 1597 525
----DATA END----
```

###### Basic decrypting
```
python OneTimePad.py -d -DD "5776 8453 ..."
```
This will return
```
Decrypting data...
Decrypted data: Wow this really works!
```

##### Save encrypted data to file
To save encrypted data to a file the user must use -do or --dataout then the desired filename
```
python OneTimePad.py -e -da "Wow this really works!" -do data.txt
```
This will save the encrypted text to 'data.txt'


##### Reading encrypted data from file
To read encrypted data from a file the user must use -ef or --EnFile then the filename
```
python OneTimePad.py -d -ef data.txt
```
This will decrypt the encrypted text in 'data.txt'


##### Custom key filenames
To use a custom filename for the private key you must use -ko to define the filename
```
python OneTimePad.py -e -da "Wow this really works!" -ko keypass.key
```
This will save the decryption key to 'keypass.key'

To use a custom key filename to decrypt you have to use -kf or --keyfile
```
python OneTimePad.py -d -DD "5776 8453 ..." -kf keypass.key
```



## Author

* **Keegan Currie** - [My Profile](https://github.com/therealkeeg1)


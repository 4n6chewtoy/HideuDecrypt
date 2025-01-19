# HideuDecrypt
A python script designed to decrypt the database 'HideU.db' for the Android application com.calculator.hideu ('HideU: Calculator Lock - https://play.google.com/store/apps/details?id=com.calculator.hideu&hl=en).

## Script Usage

Script requires one value only as the passphrase is hardcoded (92e418a05804d6fcaa5e0a0f3729b4ee):

1. Encrypted database salt (the first 16 bytes within the encrypted DB).

The script will print the raw key required to decrypt the database.

The user PIN is stored in the table 'cal_table'.

Any questions, or issues let me know https://twitter.com/4n6chewtoy

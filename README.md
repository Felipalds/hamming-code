# Hamming code

> Hamming code is a error-correcting code to detect and correct bit errors

1. If you have you bit flipped, Hamming code will find it and correct.
2. If you have two bits flippeds, Hamming code will warn that there are some errors.

## How to run it:
1. Choose a file that you want to send to someone.
2. ```python3 ./main.py file.bin -w``` to generate the Hamming Code.
3. Send it to someone you like :)
4. The person who recieved it can see if the message had some flipped bits or if the file is corrupted: ```python3 ./main.py file.bin -r```
#Read from the file phone_number.txt and output all valid phone numbers to stdout
awk '/^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/' phone_number.txt 


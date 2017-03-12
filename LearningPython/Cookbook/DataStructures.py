##############1.1 - 1.2 Unpacking###################
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)
############
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
############
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
from pwnlib.tubes.remote import remote
import re

# flag =  247CTF{6ae15c0aeb45a334b3f01eb0dda5cab1}

address = "ea2cef7b6883d028.247ctf.com"
port = 50281

pattern = r"What is the answer to (\d+) \+ (\d+)\?"

r = remote(address, port)

for _ in range(500):
    s = r.recv().decode("utf-8")
    print(f"<<< {s}")
    
    search = re.search(pattern, s)
    
    a, b = search.group(1), search.group(2)
    result = int(a) + int(b)

    print(f">>> {a} + {b} = {result}")
    response = bytes("{}\r\n".format(result), 'utf-8')
    r.send(response)

print(r.recv().decode("utf-8"))

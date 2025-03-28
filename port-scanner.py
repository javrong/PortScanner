import nmap

scanner = nmap.PortScanner()


# Define target IP or Hostname
target = "gitpod.io"

# Run a basic scan on the target
scanner.scan(target)

# Print the scan results
for host in scanner.all_hosts():
    print("Host: ", host)
    print("State: ", scanner[host].state())

    for proto in scanner[host].all_protocols():
        print("Protocol: ", proto)
        ports = scanner[host][proto].keys()

        for port in ports:
            print("Port: ", port, "State: ", scanner[host][proto][port]['state'])

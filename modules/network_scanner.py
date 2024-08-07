# modules/network_scanner.py
import nmap
import threading

def scan_target(target, port_range):
    nm = nmap.PortScanner()
    nm.scan(target, port_range)
    return nm.csv()

def run(target, port_range="1-1024", threads=4):
    ports = port_range.split('-')
    start_port, end_port = int(ports[0]), int(ports[1])
    port_ranges = [(start_port + i * (end_port - start_port) // threads,
                    start_port + (i + 1) * (end_port - start_port) // threads - 1)
                   for i in range(threads)]
    
    threads_list = []
    results = []

    def thread_function(port_range):
        result = scan_target(target, f"{port_range[0]}-{port_range[1]}")
        results.append(result)
    
    for pr in port_ranges:
        t = threading.Thread(target=thread_function, args=(pr,))
        threads_list.append(t)
        t.start()  # Start the thread

    for t in threads_list:
        t.join()  # Wait for all threads to finish

    return "\n".join(results)

from scapy.all import IP, ICMP, sr1
import time

def ping_host(ip):
    packet = IP(dst=ip) / ICMP()
    start = time.perf_counter()
    reply = sr1(packet, timeout=1, verbose=0)
    end = time.perf_counter()

    if reply:
        return True, (end - start) * 1000  # Convert to ms
    return False, None

def scan_range(prefix, start, end):
    print(f"\nScanning: {prefix}{start} → {prefix}{end}\n")
    
    reachable = []

    for i in range(start, end + 1):
        ip = f"{prefix}{i}"
        alive, rtt = ping_host(ip)
        if alive:
            print(f"[+] {ip} is UP | RTT: {rtt:.2f} ms")
            reachable.append((ip, rtt))
        else:
            print(f"[-] {ip} is DOWN")
    
    return reachable

if __name__ == "__main__":
    reachable = scan_range("10.10.20.", 91, 111)
    
    print("\n" + "=" * 40)
    print(f"Reachable Hosts: {len(reachable)}")
    print("=" * 40)
    for ip, rtt in reachable:
        print(f"  {ip:<20} {rtt:>8.2f} ms")

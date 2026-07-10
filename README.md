Markdown
# ⚡ Network Scanner Fast (Multi-threaded)

A high-performance Python network automation script designed to scan a local network, detect online hosts, and measure their latency. Utilizing multi-threading via `ThreadPoolExecutor`, this scanner asynchronously analyzes a range of 254 hosts in just a few seconds.

---

## 🎯 Features

* **Ultra-Fast Scanning**: Uses `ThreadPoolExecutor` to parallelize ICMP (Ping) requests concurrently.
* **Smart Sorting**: Results are logically sorted by IP address in ascending order using the native `ipaddress` module.
* **Clean Output**: Clear console display featuring `[ONLINE]` status, IP address, latency in milliseconds, and a final execution summary (total time, active hosts found).

---

## 🛠️ Technologies & Libraries Used

* **Python 3.x**
* `ping3`: For handling ICMP ping requests.
* `concurrent.futures` (`ThreadPoolExecutor`): For asynchronous and parallel execution.
* `ipaddress`: For accurate IPv4 parsing and sorting.
* `time`: For script performance measurement.

---

## 🚀 Installation & Usage

### 1. Prerequisites

Make sure you have Python 3 installed on your system. One external dependency is required for the ping functionality:

```bash
pip install ping3
⚠️ Important Note on Admin Privileges: On certain operating systems (such as Linux or macOS), sending raw ICMP packets (raw sockets) requires root privileges. If the script fails to detect hosts or throws an error, run it with sudo:

Bash
sudo python network_scanner.py
2. Configuration & Launch
Clone this repository or download the network_scanner.py script.

Open the file and modify the VOTRE_RESEAU variable at the bottom of the script to match your local subnet (e.g., "192.168.1.").

Run the script:

Bash
python network_scanner.py
📊 Sample Console Output
Plaintext
[+] Début du scan rapide (trié) sur 192.168.1.0/1-254...
--------------------------------------------------
[ONLINE] 192.168.1.1 - Réponse en 4.52 ms
[ONLINE] 192.168.1.15 - Réponse en 12.1 ms
[ONLINE] 192.168.1.23 - Réponse en 2.18 ms
[ONLINE] 192.168.1.50 - Réponse en 45.32 ms
--------------------------------------------------
[+] Scan terminé en 2.34 secondes.
[+] 4 machine(s) active(s) trouvée(s).
👨‍💻 Project Context
This independent project was built as part of my career transition into IT and my preparation for a work-study contract (alternance) at ESGI Toulon.

The primary goals were to practice:

Network programming and infrastructure task automation.

Asynchronous/multi-threaded development in Python to drastically optimize performance compared to traditional sequential scanning.

Advanced data structure manipulation and object sorting.

Asynchronous/multi-threaded development in Python to drastically optimize performance compared to traditional sequential scanning.

Advanced data structure manipulation and object sorting.

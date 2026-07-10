import time
import ipaddress
from ping3 import ping
from concurrent.futures import ThreadPoolExecutor

def test_ip(ip):
    """
    Teste une seule IP. Si elle répond, retourne un dictionnaire avec les infos.
    Sinon, retourne None.
    """
    response = ping(ip, timeout=0.2)
    
    if response is not None and response is not False:
        ms = round(response * 1000, 2)
        return {"ip": ip, "latency": ms}
    return None

def scan_network_fast_sorted(base_ip, start_host=1, end_host=254, max_workers=60):
    """
    Scanne le réseau en parallèle, trie les machines trouvées par IP,
    et affiche le résultat proprement.
    """
    start_time = time.time()
    print(f"[+] Début du scan rapide (trié) sur {base_ip}0/{start_host}-{end_host}...")
    print("-" * 50)

    liste_ips = [f"{base_ip}{host}" for host in range(start_host, end_host + 1)]
    machines_trouvees = []

    # Étape 1 : Collecte des données en parallèle (asynchrone)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(test_ip, liste_ips)
        
        for result in results:
            if result:
                machines_trouvees.append(result)

    # Étape 2 : Le Tri Intelligent
    # On trie la liste en convertissant la chaîne de caractères IP en objet IPv4Address
    machines_triees = sorted(
        machines_trouvees, 
        key=lambda x: ipaddress.IPv4Address(x["ip"])
    )

    # Étape 3 : L'affichage propre et ordonné
    for machine in machines_triees:
        print(f"[ONLINE] {machine['ip']} - Réponse en {machine['latency']} ms")

    end_time = time.time()
    execution_time = round(end_time - start_time, 2)
    
    print("-" * 50)
    print(f"[+] Scan terminé en {execution_time} secondes.")
    print(f"[+] {len(machines_triees)} machine(s) active(s) trouvée(s).")

if __name__ == "__main__":
    # Adaptez la racine selon votre réseau local
    VOTRE_RESEAU = "192.168.1."
    
    scan_network_fast_sorted(VOTRE_RESEAU, start_host=1, end_host=254, max_workers=60)

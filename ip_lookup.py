import os
import sys
import subprocess
import pandas as pd
import requests
from tabulate import tabulate

API_URL = "https://ipinfo.io/{}/json"  # API Fallback

def run_command(command):
    """Runs a shell command and returns output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "N/A"
    except FileNotFoundError:
        return "Command not found"

def get_whois(ip):
    """Fetch WHOIS details using the appropriate WHOIS server."""
    details = {"IP": ip, "OrgName": "N/A", "Country": "N/A", "CIDR": "N/A", "NetRange": "N/A"}

    whois_output = run_command(["whois", ip])
    for line in whois_output.splitlines():
        if "OrgName" in line:
            details["OrgName"] = line.split(":", 1)[1].strip()
        elif "Country" in line:
            details["Country"] = line.split(":", 1)[1].strip()
        elif "CIDR" in line:
            details["CIDR"] = line.split(":", 1)[1].strip()
        elif "NetRange" in line:
            details["NetRange"] = line.split(":", 1)[1].strip()

    return details

def get_dns_info(ip):
    """Fetch DNS details using dig and nslookup."""
    reverse_dns = run_command(["dig", "-x", ip, "+short"])
    nslookup = run_command(["nslookup", ip])
    
    return {
        "Reverse DNS": reverse_dns if reverse_dns else "N/A",
        "NSLookup": nslookup.split("\n")[-1] if nslookup else "N/A"
    }

def get_ipinfo(ip):
    """Fetch IP details from the IPinfo.io API."""
    try:
        response = requests.get(API_URL.format(ip), timeout=5)
        data = response.json()
        return {
            "City": data.get("city", "N/A"),
            "Region": data.get("region", "N/A"),
            "ISP": data.get("org", "N/A"),
            "ASN": data.get("asn", {}).get("asn", "N/A")
        }
    except requests.RequestException:
        return {"City": "N/A", "Region": "N/A", "ISP": "N/A", "ASN": "N/A"}

def main():
    """Main function to process IPs from a file."""
    if len(sys.argv) != 2:
        print("Usage: python whois_lookup.py <file_with_ips>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found!")
        sys.exit(1)

    with open(filename, "r") as file:
        ips = [line.strip() for line in file if line.strip()]

    results = []
    for ip in ips:
        print(f"Fetching details for: {ip} ...")
        whois_data = get_whois(ip)
        dns_data = get_dns_info(ip)
        ipinfo_data = get_ipinfo(ip)

        results.append({
            **whois_data, 
            **dns_data, 
            **ipinfo_data
        })

    # Convert to DataFrame & display in a clean table
    df = pd.DataFrame(results)
    print(tabulate(df, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()

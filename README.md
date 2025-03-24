# 🔍 IP WHOIS & Threat Intelligence Script

**A powerful script to fetch WHOIS details, DNS records, and IP intelligence in one go!**

---

## ⚡ Features
✅ Fetches **WHOIS details** (Org, Country, CIDR, etc.)
✅ Runs **Reverse DNS & NSLookup** for domain info
✅ Queries **IPinfo API** for ISP, ASN, and location
✅ Detects **the correct WHOIS registry (ARIN, RIPE, APNIC, etc.)**
✅ Formats output in a **clean table** using `pandas`
✅ **Blacklist support** – maintain a list of suspicious IPs

---

## 🚀 Installation & Usage

### 1️⃣ Install Dependencies
```sh
pip install pandas tabulate requests
```

### 2️⃣ Add IPs to `ips.txt`
```sh
echo "64.227.85.71" >> ips.txt
echo "159.89.50.196" >> ips.txt
```

### 3️⃣ Run the script
```sh
python3 whois_lookup.py ips.txt
```

---

## 📜 Example Output
```
+---------------+-------------------+---------+---------------+--------------------+----------------------+-------------+--------+-----------+----------------+
| IP            | OrgName           | Country | CIDR          | NetRange           | Reverse DNS          | NSLookup    | City   | Region    | ISP            |
+---------------+-------------------+---------+---------------+--------------------+----------------------+-------------+--------+-----------+----------------+
| 64.227.85.71  | DigitalOcean, LLC | US      | 64.227.0.0/16 | 64.227.0.0-64.227  | server.example.com   | example.com | NYC    | New York  | DigitalOcean   |
| 159.89.50.196 | DigitalOcean, LLC | ...     | ...           | ...                | ...                  | ...         | ...    | ...       | ...            |
+---------------+-------------------+---------+---------------+--------------------+----------------------+-------------+--------+-----------+----------------+
```

---

## 🛡️ Bad IP List
⚠️ This repo maintains a **blacklist of suspicious IPs** identified from scans & abuse reports. Contributions are welcome!

### 🕵️ **How to Contribute?**
1. **Submit a PR** with new bad IPs in `bad_ips.txt`
2. Provide **proof or abuse reports** (optional but helpful)
3. Keep the format **one IP per line**

---

## 🏗️ To-Do
- [ ] Add **GeoIP lookup**
- [ ] Implement **Threat Intelligence API**
- [ ] Create a **real-time monitoring tool**

---

## 🖥️ License
**MIT License** – Feel free to modify & improve! 💜

---

### ⭐ **Star this repo if you find it useful!** ⭐


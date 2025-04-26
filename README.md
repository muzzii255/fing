# HTTP/2 & TLS Fingerprint Manipulation Toolkit

A powerful toolkit for manipulating TLS and HTTP/2 fingerprints to simulate different browser behaviors and evade detection. Built for researchers, red teamers, and developers needing fine-grained control over TLS handshakes and HTTP/2 characteristics.

---

## 📄 Overview
This toolkit allows you to:

- Generate **realistic browser-specific JA3 and Akamai fingerprints** (Chrome, Firefox, Safari, Edge)
- Randomize TLS cipher suites, extensions, curves, and JA3 strings
- Customize HTTP/2 settings, window update values, priority frames, and pseudo-header order
- Integrate easily with `curl_cffi` for actual HTTP requests

Perfect for:
- Penetration testing & bypassing bot detection
- TLS/HTTP/2 fingerprint evasion
- Automated scraping
- Security research

---

## 🛠️ Installation
```bash
git clone https://github.com/yourusername/fing.git
cd fing
pip install -r requirements.txt  # Requires curl-cffi
```

---

## 🚀 Features

### TLS Fingerprints
- Generate valid JA3 fingerprints for modern browsers
- Simulate TLS handshakes with custom curve lists, extension order, GREASE, and cipher suite shuffling

### HTTP/2 Fingerprints (Akamai Style)
- Full control over SETTINGS, WINDOW_UPDATE, PRIORITY frames, and pseudo-header order

### Browser Profiles Supported
- Chrome
- Firefox
- Safari
- Edge

---

## 📚 Usage Examples

### Generate JA3 Fingerprints
```python
from main import generate_browser_ciphers

chrome_ja3 = generate_browser_ciphers("chrome")
print(chrome_ja3)
```

### Generate HTTP/2 (Akamai) Fingerprints
```python
from akamai import generate_akami_fingerprint

firefox_fp = generate_akami_fingerprint("firefox")
print(firefox_fp)
```

### Perform HTTP Request with Fingerprints
```python
from curl_cffi import requests
from main import generate_browser_ciphers
from akamai import generate_akami_fingerprint

ja3 = generate_browser_ciphers("chrome")
akamai_fp = generate_akami_fingerprint("chrome")
extra_fp = requests.ExtraFingerprints(
        tls_signature_algorithms=[
            "ecdsa_secp256r1_sha256",
            "rsa_pss_rsae_sha256",
            "rsa_pkcs1_sha256",
            "ecdsa_secp384r1_sha384",
            "rsa_pss_rsae_sha384",
            "rsa_pkcs1_sha384",
            "rsa_pss_rsae_sha512",
            "rsa_pkcs1_sha512",
            "rsa_pkcs1_sha1"],
        tls_grease=True,
        tls_permute_extensions=True)



response = requests.get(
    'https://tls.browserleaks.com/json',
    ja3=ja3,
    akamai=akamai_fp,
    extra_fp=extra_fp,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...'
    }
)

print(response.json())
```

---

## 🔧 Advanced Options

### New TLS 1.3 Cipher Support
Add to `TLS_CIPHER_NAME_MAP` inside `curl_cffi`:
```python
0x1305: "TLS_AES_128_CCM_8_SHA256",
0x1306: "TLS_AEGIS_256_SHA512",
0x1307: "TLS_AEGIS_128L_SHA256",
```

### Firefox Curves
Add to `TLS_EC_CURVES_MAP`:
```python
256: "ffdhe2048",
257: "ffdhe3072",
```

---

## 🔍 HTTP/2 Akamai Format Guide
Each fingerprint contains 4 fields:
1. **SETTINGS**: e.g., `1:65536;4:4194304`
2. **WINDOW_UPDATE**: e.g., `15663105`
3. **PRIORITY**: e.g., `3:0:0:201,...`
4. **Pseudo-header order**: e.g., `m,a,s,p`

---

## 🎓 Research-Based
Built upon Akamai's research into passive fingerprinting and TLS/HTTP/2 client identification.
[Passive-Fingerprinting-Of-HTTP2-Clients] (https://www.blackhat.com/docs/eu-17/materials/eu-17-Shuster-Passive-Fingerprinting-Of-HTTP2-Clients-wp.pdf)
[TLS Fingerprinting with JA3 and JA3S] (https://engineering.salesforce.com/tls-fingerprinting-with-ja3-and-ja3s-247362855967/)
---

## 📅 License
MIT License © Muzzii255

---

## ✨ Credits
Special thanks to:
- Salesforce for the original JA3 whitepaper
- Akamai for publishing fingerprinting research
- curl_cffi for enabling fine-tuned TLS control

---



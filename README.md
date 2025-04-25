HTTP/2 Fingerprint Manipulation Tools
A comprehensive toolkit for manipulating HTTP/2 and TLS fingerprints to evade detection and simulate various browser behaviors.
📋 Overview
This repository provides tools for generating and manipulating HTTP/2 and TLS fingerprints. Based on extensive research on browser fingerprinting techniques (particularly from Akamai's HTTP/2 client fingerprinting research), this toolkit allows you to:

Generate realistic browser-specific fingerprints (Chrome, Firefox, Safari, Edge)
Create random but plausible fingerprints
Manipulate HTTP/2 settings, window updates, and priorities
Customize TLS extensions and cipher suites
Generate both JA3 fingerprints and Akamai fingerprints

Perfect for researchers, penetration testers, web scrapers, and anyone interested in browser fingerprinting technology.
🧩 Components

akamai.py: Generate Akamai-style HTTP/2 fingerprints with format settings|window_update|priority|pseudo_headers
ciphers.py: Comprehensive database of TLS cipher suites for both TLS 1.2 and TLS 1.3
main.py: Tools to generate JA3 fingerprints and manipulate TLS extensions, curves, and cipher suites

⚙️ Installation
bash# Clone the repository
git clone https://github.com/yourusername/fing.git
cd fing

# Install dependencies
pip install curl-cffi
🚀 Usage
Generate Browser-Specific Akamai Fingerprints
pythonfrom akamai import generate_akami_fingerprint

# Generate a Chrome-like fingerprint
chrome_fp = generate_akami_fingerprint("chrome")
print(chrome_fp)  # 1:65536;3:1000;4:6291456|15663105|0|m,a,s,p

# Generate a Firefox-like fingerprint
firefox_fp = generate_akami_fingerprint("firefox")
print(firefox_fp)  # 1:65536;4:131072;5:16384|12517377|3:0:0:201,5:0:0:101,7:0:0:1,9:0:7:1,11:0:3:1|m,p,a,s
Generate Custom JA3 Fingerprints
pythonfrom main import generate_browser_ciphers

# Generate a Chrome-like JA3 fingerprint
chrome_ja3 = generate_browser_ciphers("chrome")
print(chrome_ja3)

# Generate a Firefox-like JA3 fingerprint
firefox_ja3 = generate_browser_ciphers("firefox")
print(firefox_ja3)
Using with curl-cffi for HTTP Requests
pythonfrom curl_cffi import requests
from akamai import generate_akami_fingerprint

# Generate a Chrome-like fingerprint
chrome_fp = generate_akami_fingerprint("chrome")

# Use the fingerprint for a request
response = requests.get(
    'https://example.com',
    impersonate="chrome110",
    akamai=chrome_fp
)
print(response.status_code)
Advanced Example with Browser Simulation
pythonfrom curl_cffi import requests
from main import generate_browser_ciphers
from akamai import generate_akami_fingerprint

# Generate fingerprints
ja3 = generate_browser_ciphers("chrome")
akamai_fp = generate_akami_fingerprint("chrome")

# Configure request options
options = {
    'ja3': ja3,  
    'akamai': akamai_fp,
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }
}

# Make request with configured fingerprints
response = requests.get('https://tls.browserleaks.com/json', **options)
print(response.json())
🔧 Advanced Configuration
Using New TLS 1.3 Cipher Suites
To use the new TLS 1.3 cipher suites with the add_new_tls13=True option in generate_browser_ciphers, you need to add the following values to the TLS_CIPHER_NAME_MAP in your curl-cffi installation:
python# Add to Lib\site-packages\curl_cffi\requests\impersonate.py
TLS_CIPHER_NAME_MAP = {
    # ... existing entries ...
    0x1305: "TLS_AES_128_CCM_8_SHA256",
    0x1306: "TLS_AEGIS_256_SHA512",
    0x1307: "TLS_AEGIS_128L_SHA256",
}
Supporting Firefox EC Curves
To properly simulate Firefox fingerprints, add the following EC curves to your curl-cffi installation:
python# Add to Lib\site-packages\curl_cffi\requests\impersonate.py
TLS_EC_CURVES_MAP = {
    # ... existing entries ...
    256: "ffdhe2048",
    257: "ffdhe3072",
}
🔍 Understanding HTTP/2 Fingerprints
HTTP/2 fingerprints in Akamai format consist of four parts separated by |:

SETTINGS parameters (e.g., 1:65536;3:1000;4:6291456):

1: SETTINGS_HEADER_TABLE_SIZE
2: SETTINGS_ENABLE_PUSH
3: SETTINGS_MAX_CONCURRENT_STREAMS
4: SETTINGS_INITIAL_WINDOW_SIZE
5: SETTINGS_MAX_FRAME_SIZE
6: SETTINGS_MAX_HEADER_LIST_SIZE


WINDOW_UPDATE value (e.g., 15663105):
The increment by which the client increases its receive window.
PRIORITY frames (e.g., 3:0:0:201,5:0:0:101,7:0:0:1,9:0:7:1,11:0:3:1):
Stream priority information in the format StreamID:Exclusivity_Bit:Dependant_StreamID:Weight.
Pseudo-header order (e.g., m,a,s,p):
The order of HTTP/2 pseudo-headers:

m: :method
p: :path
a: :authority
s: :scheme



📚 Research Background
This toolkit is based on Akamai's research on passive fingerprinting of HTTP/2 clients. Different browsers and HTTP client libraries implement HTTP/2 differently, creating unique fingerprints that can be used to identify clients regardless of User-Agent spoofing.

## 🧾 License

MIT © Muzzii255

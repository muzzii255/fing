
import random
from ciphers import *
from akamai import generate_akami_fingerprint



CORE_CURVE = [
    29, # X25519
    23, # P-256
    24, # P-384
    25, # P-521
]
OPTIONAL_CURVE = [
    4588, #X25519MLKEM768
    25497, #X25519Kyber768Draft00
]

CORE_EXTENSIONS = [
    23,  #extended_master_secret
    35,  #session_ticket
    # 22,  #encrypt_then_mac
    0,   # server_name (inserted later based on placement)
    10,  # supported_groups
    11,  # ec_point_formats
    13,  # signature_algorithms
    43,  # supported_versions
    45,  # psk_key_exchange_modes
    51,  # key_share
    16, # application_layer_protocol_negotiation
]
OPTIONAL_EXTENSIONS = [
    5,   # status_request
    18,  # signed_certificate_timestamp
    21,  # padding
    27,  # compress_certificate
    # 42,  #early_data
    # 1,   #max_fragment_length
    # 28,  # record_size_limit
    # 34,  # delegated_credential
    # 44,  # cookie
    # 47,  # certificate_authorities
    # 49,  # post_handshake_auth
    # 50,  # signature_algorithms_cert
]

GREASE_VALUES = [
    # 2570, 
    # 6682, 
    # 41377, 
    # 52393,
    # 56797,
    65037, 
    65281
]

def generate_curve(browser_type):
    curve = list(CORE_CURVE)
    if browser_type != "chrome":
        # 256 ffdhe2048
        # 257 ffdhe3072 
        # add these 2 on TLS_EC_CURVES_MAP Lib\site-packages\curl_cffi\requests\impersonate.py
        # if you want to use firefox ja3
        curve.extend([256,257])# Firefox often includes FFDHE groups
    
    
    op_curve = list(OPTIONAL_CURVE)
    
    if random.choice([True,False]):
        curve = op_curve + curve
    else:
        curve = [random.choice(op_curve)] + curve
    return '-'.join([str(x) for x in curve])
    
        

def generate_extensions(include_alps=False,
                        place_sni="start"):  # "start", "end", "random"

    exts = [e for e in CORE_EXTENSIONS if e != 0]

    if include_alps:
        exts.append(17513)

    exts += random.sample(OPTIONAL_EXTENSIONS, k=random.randint(2, len(OPTIONAL_EXTENSIONS)))


    for g in GREASE_VALUES:
        exts.insert(random.randint(0, len(exts)), g)

    if place_sni == "start":
        exts = [0] + exts
    elif place_sni == "end":
        exts.append(0)
    elif place_sni == "random":
        exts.insert(random.randint(0, len(exts)), 0)

    return '-'.join([str(x) for x in exts])


def generate_browser_ciphers(browser_type,add_new_tls13=False):
   
    tls13_recommended = [v["int"] for k, v in Tls13Ciphers.items()]
    tls13_new = [v["int"] for k, v in Tls13CiphersNew.items()]
    tls12_recommended = [v["int"] for k, v in Tls12Ciphers.items()]
    
    base_ciphers = {
        # base ciphers
        "chrome": {
            "tls13":[4865, 4866, 4867,],
            "tls12":[int(x) for x in "49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53".split('-')],
        },
        "firefox": {
            "tls13":[4865, 4867, 4866,],
            "tls12": [int(x) for x in "49195-49199-52393-52392-49196-49200-49162-49161-49171-49172-156-157-47-53".split('-')],
        },
        "safari": {
            "tls13" : [4865, 4866, 4867,],
            "tls12" : [int(x) for x in "4865-4866-4867-49196-49195-52393-49200-49199-52392-49162-49161-49172-49171-157-156-53-47-49160-49170-10".split('-')],
        }
    }
    
    if browser_type.lower() in base_ciphers:
        tls13_ciphers = base_ciphers[browser_type.lower()]["tls13"]
        tls12_ciphers = base_ciphers[browser_type.lower()]['tls12']
        unused_ciphers =  [x for x in tls12_recommended if x not in tls12_ciphers]
        
        if add_new_tls13:
            tls13_ciphers = tls13_ciphers[:1]
            tls13_ciphers.extend([random.sample(tls13_new,k=random.randint(2,len(tls13_new)))])
        
        if random.choice([True,False]):
                tls12_ciphers = tls12_ciphers[:-2]
                tls12_ciphers.append(random.choice(unused_ciphers))
                tls12_ciphers.append(random.choice(unused_ciphers))
        
        num_swaps = random.randint(1, 3)
        for _ in range(num_swaps):
            idx1 = random.randint(4, len(tls12_ciphers) - 1)
            idx2 = random.randint(4, len(tls12_ciphers) - 1)
            tls12_ciphers[idx1], tls12_ciphers[idx2] = tls12_ciphers[idx2], tls12_ciphers[idx1]
        
        if browser_type.lower() == 'chrome':
            alps = True
        else:
            alps = False
        place_sni = random.choice(["start","end","random"])
            
        
        cipher_suites =   f'{"-".join([str(x) for x in tls13_ciphers])}-{"-".join([str(x) for x in tls12_ciphers])}'
        exts = generate_extensions(include_alps=alps,place_sni=place_sni)  
        ec_curve = generate_curve(browser_type=browser_type)
        return f'771,{cipher_suites},{exts},{ec_curve},0'
        
            
    else:
        return "Skill Issues"
    


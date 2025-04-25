import random
import time

def generate_random_fingerprint():
    settings = generate_random_settings()
    window_update = generate_random_window_update()
    priority = "0"
    pseudo_headers = generate_random_pseudo_header_order()
    
    # Combine all parts
    return f"{settings}|{window_update}|{priority}|{pseudo_headers}"

def generate_random_settings():
    params = [1, 2, 3, 4, 5, 6]
    random.shuffle(params)
    num_params = random.randint(2, 5)
    
    settings = []
    for i in range(min(num_params, len(params))):
        param = params[i]
        value = generate_value_for_param(param)
        settings.append(f"{param}:{value}")
    
    return ";".join(settings)


def generate_value_for_param(param):
    if param == 1:  # SETTINGS_HEADER_TABLE_SIZE
        return random.choice([4096, 8192, 16384, 32768, 65536])
    elif param == 2:  # SETTINGS_ENABLE_PUSH
        return random.choice([0, 1])
    elif param == 3:  # SETTINGS_MAX_CONCURRENT_STREAMS
        return random.choice([100, 128, 256, 1000, 1024])
    elif param == 4:  # SETTINGS_INITIAL_WINDOW_SIZE
        return random.choice([65535, 131072, 262144, 1048576, 2097152, 4194304, 6291456, 10485760])
    elif param == 5:  # SETTINGS_MAX_FRAME_SIZE
        return random.choice([16384, 32768, 65536])
    elif param == 6:  # SETTINGS_MAX_HEADER_LIST_SIZE
        return random.choice([16384, 32768, 65536, 131072, 262144])
    else:
        return 0

def generate_random_window_update():
    common_values = [
        12517377,  # Firefox
        15663105,  # Chrome
        10485760   #Safari
        
    ]
    
    if random.randint(0, 9) < 3:
        return random.randint(10000000, 30000000)
    
    return random.choice(common_values)

def generate_random_pseudo_header_order():
    header_orders = [
        "m,a,s,p",  # Chrome
        "m,s,a,p",  # Chromium
        "m,p,a,s",  # Firefox
        "m,s,p,a",  # Safari
    ]
    return random.choice(header_orders)

def generate_akami_fingerprint(browser_type):
    if browser_type == "chrome":
        settings = "1:65536;3:1000;4:6291456"
        window_update = 15663105
        priority = "0"
        headers = "m,a,s,p"
        if random.randint(0, 9) < 3:
            window_update += random.randint(-500, 500)
            
    elif browser_type == "firefox":
        settings = "1:65536;4:131072;5:16384"
        window_update = 12517377
        priority = "3:0:0:201,5:0:0:101,7:0:0:1,9:0:7:1,11:0:3:1"
        headers = "m,p,a,s"
        
    elif browser_type == "safari":
        settings = "1:65536;4:131072;5:16384"
        window_update = 16777216
        priority = "0"
        headers = "m,s,p,a"
        
    elif browser_type == "edge":
        settings = "3:1024;4:10485760"
        window_update = 10420225
        priority = "0"
        headers = "m,a,s,p"
        
    else: 
        return generate_random_fingerprint()
    
    return f"{settings}|{window_update}|{priority}|{headers}"

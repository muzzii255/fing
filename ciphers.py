
Tls13Ciphers = {
   
    "TLS_AES_128_GCM_SHA256": { "hex": 0x1301 , "int": 4865, "recommend": "Y" },
    "TLS_AES_256_GCM_SHA384": { "hex": 0x1302 , "int": 4866, "recommend": "Y" },
    "TLS_CHACHA20_POLY1305_SHA256": {"hex": 0x1303 , "int": 4867, "recommend": "Y" },
    "TLS_AES_128_CCM_SHA256": { "hex": 0x1304 , "int": 4868, "recommend": "Y" },

}

Tls13CiphersNew = {
    "TLS_AES_128_CCM_8_SHA256": { "hex": 0x1305 , "int": 4869, "recommend": "N" },
    "TLS_AEGIS_256_SHA512": { "hex": 0x1306 , "int": 4870, "recommend": "N" },
    "TLS_AEGIS_128L_SHA256": { "hex": 0x1307 , "int": 4871, "recommend": "N" },
}


Tls12Ciphers = {
  "TLS_RSA_WITH_3DES_EDE_CBC_SHA": {"hex": 0xa,"int": 10,"recommend": "N" },
  "TLS_RSA_WITH_AES_128_CBC_SHA": {"hex": 0x2f,"int": 47,"recommend": "N" },
  "TLS_RSA_WITH_AES_256_CBC_SHA": {"hex": 0x35,"int": 53,"recommend": "N" },
  "TLS_RSA_WITH_AES_128_CBC_SHA256": {"hex": 0x3c,"int": 60,"recommend": "N" },
  "TLS_RSA_WITH_AES_256_CBC_SHA256": {"hex": 0x3d,"int": 61,"recommend": "N" },
  "TLS_PSK_WITH_AES_128_CBC_SHA": {"hex": 0x8c,"int": 140,"recommend": "N" },
  "TLS_PSK_WITH_AES_256_CBC_SHA": {"hex": 0x8d,"int": 141,"recommend": "N" },
  "TLS_RSA_WITH_AES_128_GCM_SHA256": {"hex": 0x9c,"int": 156,"recommend": "N" },
  "TLS_RSA_WITH_AES_256_GCM_SHA384": {"hex": 0x9d,"int": 157,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA": {"hex": 0xc008,"int": 49160,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA": {"hex": 0xc009,"int": 49161,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA": {"hex": 0xc00a,"int": 49162,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA": {"hex": 0xc012,"int": 49170,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA": {"hex": 0xc013,"int": 49171,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA": {"hex": 0xc014,"int": 49172,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256": {"hex": 0xc023,"int": 49187,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384": {"hex": 0xc024,"int": 49188,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256": {"hex": 0xc027,"int": 49191,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384": {"hex": 0xc028,"int": 49192,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256": {"hex": 0xc02b,"int": 49195,"recommend": "Y" },
  "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384": {"hex": 0xc02c,"int": 49196,"recommend": "Y" },
  "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256": {"hex": 0xc02f,"int": 49199,"recommend": "Y" },
  "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384": {"hex": 0xc030,"int": 49200,"recommend": "Y" },
  "TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA": {"hex": 0xc035,"int": 49205,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA": {"hex": 0xc036,"int": 49206,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256": {"hex": 0xcca8,"int": 52392,"recommend": "Y" },
  "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256": {"hex": 0xcca9,"int": 52393,"recommend": "Y" },
  "TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256": {"hex": 0xccac,"int": 52396,"recommend": "Y" },
  "TLS_DH_RSA_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc041,"int": 49217,"recommend": "N"}
}


# Need more research
Tls12CiphersOther = {
  "TLS_NULL_WITH_NULL_NULL": { "hex": 0x0, "int": 0, "recommend": "N" },
  "TLS_RSA_WITH_NULL_MD5": { "hex": 0x1, "int": 1, "recommend": "N" },
  "TLS_RSA_WITH_NULL_SHA": { "hex": 0x2, "int": 2, "recommend": "N" },
  "TLS_RSA_EXPORT_WITH_RC4_40_MD5": {"hex": 0x3,"int": 3,"recommend": "N" },
  "TLS_RSA_WITH_RC4_128_MD5": { "hex": 0x4, "int": 4, "recommend": "N" },
  "TLS_RSA_WITH_RC4_128_SHA": { "hex": 0x5, "int": 5, "recommend": "N" },
  "TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5": {"hex": 0x6,"int": 6,"recommend": "N" },
  "TLS_RSA_WITH_IDEA_CBC_SHA": { "hex": 0x7, "int": 7, "recommend": "N" },
  "TLS_RSA_EXPORT_WITH_DES40_CBC_SHA": {"hex": 0x8,"int": 8,"recommend": "N" },
  "TLS_RSA_WITH_DES_CBC_SHA": { "hex": 0x9, "int": 9, "recommend": "N" },
  "TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA": {"hex": 0xb,"int": 11,"recommend": "N" },
  "TLS_DH_DSS_WITH_DES_CBC_SHA": {"hex": 0xc,"int": 12,"recommend": "N" },
  "TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA": {"hex": 0xd,"int": 13,"recommend": "N" },
  "TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA": {"hex": 0xe,"int": 14,"recommend": "N" },
  "TLS_DH_RSA_WITH_DES_CBC_SHA": {"hex": 0xf,"int": 15,"recommend": "N" },
  "TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA": {"hex": 0x10,"int": 16,"recommend": "N" },
  "TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA": {"hex": 0x11,"int": 17,"recommend": "N" },
  "TLS_DHE_DSS_WITH_DES_CBC_SHA": {"hex": 0x12,"int": 18,"recommend": "N" },
  "TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA": {"hex": 0x13,"int": 19,"recommend": "N" },
  "TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA": {"hex": 0x14,"int": 20,"recommend": "N" },
  "TLS_DHE_RSA_WITH_DES_CBC_SHA": {"hex": 0x15,"int": 21,"recommend": "N" },
  "TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA": {"hex": 0x16,"int": 22,"recommend": "N" },
  "TLS_DH_anon_EXPORT_WITH_RC4_40_MD5": {"hex": 0x17,"int": 23,"recommend": "N" },
  "TLS_DH_anon_WITH_RC4_128_MD5": {"hex": 0x18,"int": 24,"recommend": "N" },
  "TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA": {"hex": 0x19,"int": 25,"recommend": "N" },
  "TLS_DH_anon_WITH_DES_CBC_SHA": {"hex": 0x1a,"int": 26,"recommend": "N" },
  "TLS_DH_anon_WITH_3DES_EDE_CBC_SHA": {"hex": 0x1b,"int": 27,"recommend": "N" },
  "TLS_KRB5_WITH_DES_CBC_SHA": { "hex": 0x1e, "int": 30, "recommend": "N" },
  "TLS_KRB5_WITH_3DES_EDE_CBC_SHA": {"hex": 0x1f,"int": 31,"recommend": "N" },
  "TLS_KRB5_WITH_RC4_128_SHA": { "hex": 0x20, "int": 32, "recommend": "N" },
  "TLS_KRB5_WITH_IDEA_CBC_SHA": {"hex": 0x21,"int": 33,"recommend": "N" },
  "TLS_KRB5_WITH_DES_CBC_MD5": { "hex": 0x22, "int": 34, "recommend": "N" },
  "TLS_KRB5_WITH_3DES_EDE_CBC_MD5": {"hex": 0x23,"int": 35,"recommend": "N" },
  "TLS_KRB5_WITH_RC4_128_MD5": { "hex": 0x24, "int": 36, "recommend": "N" },
  "TLS_KRB5_WITH_IDEA_CBC_MD5": {"hex": 0x25,"int": 37,"recommend": "N" },
  "TLS_KRB5_EXPORT_WITH_DES_CBC_40_SHA": {"hex": 0x26,"int": 38,"recommend": "N" },
  "TLS_KRB5_EXPORT_WITH_RC2_CBC_40_SHA": {"hex": 0x27,"int": 39,"recommend": "N" },
  "TLS_KRB5_EXPORT_WITH_RC4_40_SHA": {"hex": 0x28,"int": 40,"recommend": "N" },
  "TLS_KRB5_EXPORT_WITH_DES_CBC_40_MD5": {"hex": 0x29,"int": 41,"recommend": "N" },
  "TLS_KRB5_EXPORT_WITH_RC2_CBC_40_MD5": {"hex": 0x2a,"int": 42,"recommend": "N" },
  "TLS_KRB5_EXPORT_WITH_RC4_40_MD5": {"hex": 0x2b,"int": 43,"recommend": "N" },
  "TLS_PSK_WITH_NULL_SHA": { "hex": 0x2c, "int": 44, "recommend": "N" },
  "TLS_DHE_PSK_WITH_NULL_SHA": { "hex": 0x2d, "int": 45, "recommend": "N" },
  "TLS_RSA_PSK_WITH_NULL_SHA": { "hex": 0x2e, "int": 46, "recommend": "N" },
  "TLS_DH_DSS_WITH_AES_128_CBC_SHA": {"hex": 0x30,"int": 48,"recommend": "N" },
  "TLS_DH_RSA_WITH_AES_128_CBC_SHA": {"hex": 0x31,"int": 49,"recommend": "N" },
  "TLS_DHE_DSS_WITH_AES_128_CBC_SHA": {"hex": 0x32,"int": 50,"recommend": "N" },
  "TLS_DHE_RSA_WITH_AES_128_CBC_SHA": {"hex": 0x33,"int": 51,"recommend": "N" },
  "TLS_DH_anon_WITH_AES_128_CBC_SHA": {"hex": 0x34,"int": 52,"recommend": "N" },
  "TLS_DH_DSS_WITH_AES_256_CBC_SHA": {"hex": 0x36,"int": 54,"recommend": "N" },
  "TLS_DH_RSA_WITH_AES_256_CBC_SHA": {"hex": 0x37,"int": 55,"recommend": "N" },
  "TLS_DHE_DSS_WITH_AES_256_CBC_SHA": {"hex": 0x38,"int": 56,"recommend": "N" },
  "TLS_DHE_RSA_WITH_AES_256_CBC_SHA": {"hex": 0x39,"int": 57,"recommend": "N" },
  "TLS_DH_anon_WITH_AES_256_CBC_SHA": {"hex": 0x3a,"int": 58,"recommend": "N" },
  "TLS_RSA_WITH_NULL_SHA256": { "hex": 0x3b, "int": 59, "recommend": "N" },
  "TLS_DH_DSS_WITH_AES_128_CBC_SHA256": {"hex": 0x3e,"int": 62,"recommend": "N" },
  "TLS_DH_RSA_WITH_AES_128_CBC_SHA256": {"hex": 0x3f,"int": 63,"recommend": "N" },
  "TLS_DHE_DSS_WITH_AES_128_CBC_SHA256": {"hex": 0x40,"int": 64,"recommend": "N" },
  "TLS_RSA_WITH_CAMELLIA_128_CBC_SHA": {"hex": 0x41,"int": 65,"recommend": "N" },
  "TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA": {"hex": 0x42,"int": 66,"recommend": "N" },
  "TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA": {"hex": 0x43,"int": 67,"recommend": "N" },
  "TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA": {"hex": 0x44,"int": 68,"recommend": "N" },
  "TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA": {"hex": 0x45,"int": 69,"recommend": "N" },
  "TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA": {"hex": 0x46,"int": 70,"recommend": "N" },
  "TLS_DHE_RSA_WITH_AES_128_CBC_SHA256": {"hex": 0x67,"int": 103,"recommend": "N" },
  "TLS_DH_DSS_WITH_AES_256_CBC_SHA256": {"hex": 0x68,"int": 104,"recommend": "N" },
  "TLS_DH_RSA_WITH_AES_256_CBC_SHA256": {"hex": 0x69,"int": 105,"recommend": "N" },
  "TLS_DHE_DSS_WITH_AES_256_CBC_SHA256": {"hex": 0x6a,"int": 106,"recommend": "N" },
  "TLS_DHE_RSA_WITH_AES_256_CBC_SHA256": {"hex": 0x6b,"int": 107,"recommend": "N" },
  "TLS_DH_anon_WITH_AES_128_CBC_SHA256": {"hex": 0x6c,"int": 108,"recommend": "N" },
  "TLS_DH_anon_WITH_AES_256_CBC_SHA256": {"hex": 0x6d,"int": 109,"recommend": "N" },
  "TLS_RSA_WITH_CAMELLIA_256_CBC_SHA": {"hex": 0x84,"int": 132,"recommend": "N" },
  "TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA": {"hex": 0x85,"int": 133,"recommend": "N" },
  "TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA": {"hex": 0x86,"int": 134,"recommend": "N" },
  "TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA": {"hex": 0x87,"int": 135,"recommend": "N" },
  "TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA": {"hex": 0x88,"int": 136,"recommend": "N" },
  "TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA": {"hex": 0x89,"int": 137,"recommend": "N" },
  "TLS_PSK_WITH_RC4_128_SHA": { "hex": 0x8a, "int": 138, "recommend": "N" },
  "TLS_PSK_WITH_3DES_EDE_CBC_SHA": {"hex": 0x8b,"int": 139,"recommend": "N" },
  "TLS_DHE_PSK_WITH_RC4_128_SHA": {"hex": 0x8e,"int": 142,"recommend": "N" },
  "TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA": {"hex": 0x8f,"int": 143,"recommend": "N" },
  "TLS_DHE_PSK_WITH_AES_128_CBC_SHA": {"hex": 0x90,"int": 144,"recommend": "N" },
  "TLS_DHE_PSK_WITH_AES_256_CBC_SHA": {"hex": 0x91,"int": 145,"recommend": "N" },
  "TLS_RSA_PSK_WITH_RC4_128_SHA": {"hex": 0x92,"int": 146,"recommend": "N" },
  "TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA": {"hex": 0x93,"int": 147,"recommend": "N" },
  "TLS_RSA_PSK_WITH_AES_128_CBC_SHA": {"hex": 0x94,"int": 148,"recommend": "N" },
  "TLS_RSA_PSK_WITH_AES_256_CBC_SHA": {"hex": 0x95,"int": 149,"recommend": "N" },
  "TLS_RSA_WITH_SEED_CBC_SHA": {"hex": 0x96,"int": 150,"recommend": "N" },
  "TLS_DH_DSS_WITH_SEED_CBC_SHA": {"hex": 0x97,"int": 151,"recommend": "N" },
  "TLS_DH_RSA_WITH_SEED_CBC_SHA": {"hex": 0x98,"int": 152,"recommend": "N" },
  "TLS_DHE_DSS_WITH_SEED_CBC_SHA": {"hex": 0x99,"int": 153,"recommend": "N" },
  "TLS_DHE_RSA_WITH_SEED_CBC_SHA": {"hex": 0x9a,"int": 154,"recommend": "N" },
  "TLS_DH_anon_WITH_SEED_CBC_SHA": {"hex": 0x9b,"int": 155,"recommend": "N" },
  "TLS_DHE_RSA_WITH_AES_128_GCM_SHA256": {"hex": 0x9e,"int": 158,"recommend": "Y" },
  "TLS_DHE_RSA_WITH_AES_256_GCM_SHA384": {"hex": 0x9f,"int": 159,"recommend": "Y" },
  "TLS_DH_RSA_WITH_AES_128_GCM_SHA256": {"hex": 0xa0,"int": 160,"recommend": "N" },
  "TLS_DH_RSA_WITH_AES_256_GCM_SHA384": {"hex": 0xa1,"int": 161,"recommend": "N" },
  "TLS_DHE_DSS_WITH_AES_128_GCM_SHA256": {"hex": 0xa2,"int": 162,"recommend": "N" },
  "TLS_DHE_DSS_WITH_AES_256_GCM_SHA384": {"hex": 0xa3,"int": 163,"recommend": "N" },
  "TLS_DH_DSS_WITH_AES_128_GCM_SHA256": {"hex": 0xa4,"int": 164,"recommend": "N" },
  "TLS_DH_DSS_WITH_AES_256_GCM_SHA384": {"hex": 0xa5,"int": 165,"recommend": "N" },
  "TLS_DH_anon_WITH_AES_128_GCM_SHA256": {"hex": 0xa6,"int": 166,"recommend": "N" },
  "TLS_DH_anon_WITH_AES_256_GCM_SHA384": {"hex": 0xa7,"int": 167,"recommend": "N" },
  "TLS_PSK_WITH_AES_128_GCM_SHA256": {"hex": 0xa8,"int": 168,"recommend": "N" },
  "TLS_PSK_WITH_AES_256_GCM_SHA384": {"hex": 0xa9,"int": 169,"recommend": "N" },
  "TLS_DHE_PSK_WITH_AES_128_GCM_SHA256": {"hex": 0xaa,"int": 170,"recommend": "Y" },
  "TLS_DHE_PSK_WITH_AES_256_GCM_SHA384": {"hex": 0xab,"int": 171,"recommend": "Y" },
  "TLS_RSA_PSK_WITH_AES_128_GCM_SHA256": {"hex": 0xac,"int": 172,"recommend": "N" },
  "TLS_RSA_PSK_WITH_AES_256_GCM_SHA384": {"hex": 0xad,"int": 173,"recommend": "N" },
  "TLS_PSK_WITH_AES_128_CBC_SHA256": {"hex": 0xae,"int": 174,"recommend": "N" },
  "TLS_PSK_WITH_AES_256_CBC_SHA384": {"hex": 0xaf,"int": 175,"recommend": "N" },
  "TLS_PSK_WITH_NULL_SHA256": { "hex": 0xb0, "int": 176, "recommend": "N" },
  "TLS_PSK_WITH_NULL_SHA384": { "hex": 0xb1, "int": 177, "recommend": "N" },
  "TLS_DHE_PSK_WITH_AES_128_CBC_SHA256": {"hex": 0xb2,"int": 178,"recommend": "N" },
  "TLS_DHE_PSK_WITH_AES_256_CBC_SHA384": {"hex": 0xb3,"int": 179,"recommend": "N" },
  "TLS_DHE_PSK_WITH_NULL_SHA256": {"hex": 0xb4,"int": 180,"recommend": "N" },
  "TLS_DHE_PSK_WITH_NULL_SHA384": {"hex": 0xb5,"int": 181,"recommend": "N" },
  "TLS_RSA_PSK_WITH_AES_128_CBC_SHA256": {"hex": 0xb6,"int": 182,"recommend": "N" },
  "TLS_RSA_PSK_WITH_AES_256_CBC_SHA384": {"hex": 0xb7,"int": 183,"recommend": "N" },
  "TLS_RSA_PSK_WITH_NULL_SHA256": {"hex": 0xb8,"int": 184,"recommend": "N" },
  "TLS_RSA_PSK_WITH_NULL_SHA384": {"hex": 0xb9,"int": 185,"recommend": "N" },
  "TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xba,"int": 186,"recommend": "N" },
  "TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xbb,"int": 187,"recommend": "N" },
  "TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xbc,"int": 188,"recommend": "N" },
  "TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xbd,"int": 189,"recommend": "N" },
  "TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xbe,"int": 190,"recommend": "N" },
  "TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xbf,"int": 191,"recommend": "N" },
  "TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256": {"hex": 0xc0,"int": 192,"recommend": "N" },
  "TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA256": {"hex": 0xc1,"int": 193,"recommend": "N" },
  "TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA256": {"hex": 0xc2,"int": 194,"recommend": "N" },
  "TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256": {"hex": 0xc3,"int": 195,"recommend": "N" },
  "TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256": {"hex": 0xc4,"int": 196,"recommend": "N" },
  "TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256": {"hex": 0xc5,"int": 197,"recommend": "N" },
  "TLS_SM4_GCM_SM3": { "hex": 0xc6, "int": 198, "recommend": "N" },
  "TLS_SM4_CCM_SM3": { "hex": 0xc7, "int": 199, "recommend": "N" },
  "TLS_EMPTY_RENEGOTIATION_INFO_SCSV": {"hex": 0xff,"int": 255,"recommend": "N" },
  "TLS_FALLBACK_SCSV": { "hex": 0x5600, "int": 22016, "recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_NULL_SHA": {"hex": 0xc001,"int": 49153,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_RC4_128_SHA": {"hex": 0xc002,"int": 49154,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA": {"hex": 0xc003,"int": 49155,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA": {"hex": 0xc004,"int": 49156,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA": {"hex": 0xc005,"int": 49157,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_NULL_SHA": {"hex": 0xc006,"int": 49158,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_RC4_128_SHA": {"hex": 0xc007,"int": 49159,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_NULL_SHA": {"hex": 0xc00b,"int": 49163,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_RC4_128_SHA": {"hex": 0xc00c,"int": 49164,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA": {"hex": 0xc00d,"int": 49165,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA": {"hex": 0xc00e,"int": 49166,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA": {"hex": 0xc00f,"int": 49167,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_NULL_SHA": {"hex": 0xc010,"int": 49168,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_RC4_128_SHA": {"hex": 0xc011,"int": 49169,"recommend": "N" },
  "TLS_ECDH_anon_WITH_NULL_SHA": {"hex": 0xc015,"int": 49173,"recommend": "N" },
  "TLS_ECDH_anon_WITH_RC4_128_SHA": {"hex": 0xc016,"int": 49174,"recommend": "N" },
  "TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA": {"hex": 0xc017,"int": 49175,"recommend": "N" },
  "TLS_ECDH_anon_WITH_AES_128_CBC_SHA": {"hex": 0xc018,"int": 49176,"recommend": "N" },
  "TLS_ECDH_anon_WITH_AES_256_CBC_SHA": {"hex": 0xc019,"int": 49177,"recommend": "N" },
  "TLS_SRP_SHA_WITH_3DES_EDE_CBC_SHA": {"hex": 0xc01a,"int": 49178,"recommend": "N" },
  "TLS_SRP_SHA_RSA_WITH_3DES_EDE_CBC_SHA": {"hex": 0xc01b,"int": 49179,"recommend": "N" },
  "TLS_SRP_SHA_DSS_WITH_3DES_EDE_CBC_SHA": {"hex": 0xc01c,"int": 49180,"recommend": "N" },
  "TLS_SRP_SHA_WITH_AES_128_CBC_SHA": {"hex": 0xc01d,"int": 49181,"recommend": "N" },
  "TLS_SRP_SHA_RSA_WITH_AES_128_CBC_SHA": {"hex": 0xc01e,"int": 49182,"recommend": "N" },
  "TLS_SRP_SHA_DSS_WITH_AES_128_CBC_SHA": {"hex": 0xc01f,"int": 49183,"recommend": "N" },
  "TLS_SRP_SHA_WITH_AES_256_CBC_SHA": {"hex": 0xc020,"int": 49184,"recommend": "N" },
  "TLS_SRP_SHA_RSA_WITH_AES_256_CBC_SHA": {"hex": 0xc021,"int": 49185,"recommend": "N" },
  "TLS_SRP_SHA_DSS_WITH_AES_256_CBC_SHA": {"hex": 0xc022,"int": 49186,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256": {"hex": 0xc025,"int": 49189,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384": {"hex": 0xc026,"int": 49190,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256": {"hex": 0xc029,"int": 49193,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384": {"hex": 0xc02a,"int": 49194,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256": {"hex": 0xc02d,"int": 49197,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384": {"hex": 0xc02e,"int": 49198,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256": {"hex": 0xc031,"int": 49201,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384": {"hex": 0xc032,"int": 49202,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_RC4_128_SHA": {"hex": 0xc033,"int": 49203,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_3DES_EDE_CBC_SHA": {"hex": 0xc034,"int": 49204,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256": {"hex": 0xc037,"int": 49207,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384": {"hex": 0xc038,"int": 49208,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_NULL_SHA": {"hex": 0xc039,"int": 49209,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_NULL_SHA256": {"hex": 0xc03a,"int": 49210,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_NULL_SHA384": {"hex": 0xc03b,"int": 49211,"recommend": "N" },
  "TLS_RSA_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc03c,"int": 49212,"recommend": "N" },
  "TLS_RSA_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc03d,"int": 49213,"recommend": "N" },
  "TLS_DH_DSS_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc03e,"int": 49214,"recommend": "N" },
  "TLS_DH_DSS_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc03f,"int": 49215,"recommend": "N" },
  "TLS_DH_RSA_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc040,"int": 49216,"recommend": "N" },
  "TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc042,"int": 49218,"recommend": "N" },
  "TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc043,"int": 49219,"recommend": "N" },
  "TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc044,"int": 49220,"recommend": "N" },
  "TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc045,"int": 49221,"recommend": "N" },
  "TLS_DH_anon_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc046,"int": 49222,"recommend": "N" },
  "TLS_DH_anon_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc047,"int": 49223,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc048,"int": 49224,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc049,"int": 49225,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc04a,"int": 49226,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc04b,"int": 49227,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc04c,"int": 49228,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc04d,"int": 49229,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc04e,"int": 49230,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc04f,"int": 49231,"recommend": "N" },
  "TLS_RSA_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc050,"int": 49232,"recommend": "N" },
  "TLS_RSA_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc051,"int": 49233,"recommend": "N" },
  "TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc052,"int": 49234,"recommend": "N" },
  "TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc053,"int": 49235,"recommend": "N" },
  "TLS_DH_RSA_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc054,"int": 49236,"recommend": "N" },
  "TLS_DH_RSA_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc055,"int": 49237,"recommend": "N" },
  "TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc056,"int": 49238,"recommend": "N" },
  "TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc057,"int": 49239,"recommend": "N" },
  "TLS_DH_DSS_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc058,"int": 49240,"recommend": "N" },
  "TLS_DH_DSS_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc059,"int": 49241,"recommend": "N" },
  "TLS_DH_anon_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc05a,"int": 49242,"recommend": "N" },
  "TLS_DH_anon_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc05b,"int": 49243,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc05c,"int": 49244,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc05d,"int": 49245,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc05e,"int": 49246,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc05f,"int": 49247,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc060,"int": 49248,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc061,"int": 49249,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc062,"int": 49250,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc063,"int": 49251,"recommend": "N" },
  "TLS_PSK_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc064,"int": 49252,"recommend": "N" },
  "TLS_PSK_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc065,"int": 49253,"recommend": "N" },
  "TLS_DHE_PSK_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc066,"int": 49254,"recommend": "N" },
  "TLS_DHE_PSK_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc067,"int": 49255,"recommend": "N" },
  "TLS_RSA_PSK_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc068,"int": 49256,"recommend": "N" },
  "TLS_RSA_PSK_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc069,"int": 49257,"recommend": "N" },
  "TLS_PSK_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc06a,"int": 49258,"recommend": "N" },
  "TLS_PSK_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc06b,"int": 49259,"recommend": "N" },
  "TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc06c,"int": 49260,"recommend": "N" },
  "TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc06d,"int": 49261,"recommend": "N" },
  "TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256": {"hex": 0xc06e,"int": 49262,"recommend": "N" },
  "TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384": {"hex": 0xc06f,"int": 49263,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_ARIA_128_CBC_SHA256": {"hex": 0xc070,"int": 49264,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_ARIA_256_CBC_SHA384": {"hex": 0xc071,"int": 49265,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xc072,"int": 49266,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384": {"hex": 0xc073,"int": 49267,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xc074,"int": 49268,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384": {"hex": 0xc075,"int": 49269,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xc076,"int": 49270,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384": {"hex": 0xc077,"int": 49271,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xc078,"int": 49272,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384": {"hex": 0xc079,"int": 49273,"recommend": "N" },
  "TLS_RSA_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc07a,"int": 49274,"recommend": "N" },
  "TLS_RSA_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc07b,"int": 49275,"recommend": "N" },
  "TLS_DHE_RSA_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc07c,"int": 49276,"recommend": "N" },
  "TLS_DHE_RSA_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc07d,"int": 49277,"recommend": "N" },
  "TLS_DH_RSA_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc07e,"int": 49278,"recommend": "N" },
  "TLS_DH_RSA_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc07f,"int": 49279,"recommend": "N" },
  "TLS_DHE_DSS_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc080,"int": 49280,"recommend": "N" },
  "TLS_DHE_DSS_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc081,"int": 49281,"recommend": "N" },
  "TLS_DH_DSS_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc082,"int": 49282,"recommend": "N" },
  "TLS_DH_DSS_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc083,"int": 49283,"recommend": "N" },
  "TLS_DH_anon_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc084,"int": 49284,"recommend": "N" },
  "TLS_DH_anon_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc085,"int": 49285,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc086,"int": 49286,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc087,"int": 49287,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc088,"int": 49288,"recommend": "N" },
  "TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc089,"int": 49289,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc08a,"int": 49290,"recommend": "N" },
  "TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc08b,"int": 49291,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc08c,"int": 49292,"recommend": "N" },
  "TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc08d,"int": 49293,"recommend": "N" },
  "TLS_PSK_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc08e,"int": 49294,"recommend": "N" },
  "TLS_PSK_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc08f,"int": 49295,"recommend": "N" },
  "TLS_DHE_PSK_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc090,"int": 49296,"recommend": "N" },
  "TLS_DHE_PSK_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc091,"int": 49297,"recommend": "N" },
  "TLS_RSA_PSK_WITH_CAMELLIA_128_GCM_SHA256": {"hex": 0xc092,"int": 49298,"recommend": "N" },
  "TLS_RSA_PSK_WITH_CAMELLIA_256_GCM_SHA384": {"hex": 0xc093,"int": 49299,"recommend": "N" },
  "TLS_PSK_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xc094,"int": 49300,"recommend": "N" },
  "TLS_PSK_WITH_CAMELLIA_256_CBC_SHA384": {"hex": 0xc095,"int": 49301,"recommend": "N" },
  "TLS_DHE_PSK_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xc096,"int": 49302,"recommend": "N" },
  "TLS_DHE_PSK_WITH_CAMELLIA_256_CBC_SHA384": {"hex": 0xc097,"int": 49303,"recommend": "N" },
  "TLS_RSA_PSK_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xc098,"int": 49304,"recommend": "N" },
  "TLS_RSA_PSK_WITH_CAMELLIA_256_CBC_SHA384": {"hex": 0xc099,"int": 49305,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_CAMELLIA_128_CBC_SHA256": {"hex": 0xc09a,"int": 49306,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_CAMELLIA_256_CBC_SHA384": {"hex": 0xc09b,"int": 49307,"recommend": "N" },
  "TLS_RSA_WITH_AES_128_CCM": {"hex": 0xc09c,"int": 49308,"recommend": "N" },
  "TLS_RSA_WITH_AES_256_CCM": {"hex": 0xc09d,"int": 49309,"recommend": "N" },
  "TLS_DHE_RSA_WITH_AES_128_CCM": {"hex": 0xc09e,"int": 49310,"recommend": "Y" },
  "TLS_DHE_RSA_WITH_AES_256_CCM": {"hex": 0xc09f,"int": 49311,"recommend": "Y" },
  "TLS_RSA_WITH_AES_128_CCM_8": {"hex": 0xc0a0,"int": 49312,"recommend": "N" },
  "TLS_RSA_WITH_AES_256_CCM_8": {"hex": 0xc0a1,"int": 49313,"recommend": "N" },
  "TLS_DHE_RSA_WITH_AES_128_CCM_8": {"hex": 0xc0a2,"int": 49314,"recommend": "N" },
  "TLS_DHE_RSA_WITH_AES_256_CCM_8": {"hex": 0xc0a3,"int": 49315,"recommend": "N" },
  "TLS_PSK_WITH_AES_128_CCM": {"hex": 0xc0a4,"int": 49316,"recommend": "N" },
  "TLS_PSK_WITH_AES_256_CCM": {"hex": 0xc0a5,"int": 49317,"recommend": "N" },
  "TLS_DHE_PSK_WITH_AES_128_CCM": {"hex": 0xc0a6,"int": 49318,"recommend": "Y" },
  "TLS_DHE_PSK_WITH_AES_256_CCM": {"hex": 0xc0a7,"int": 49319,"recommend": "Y" },
  "TLS_PSK_WITH_AES_128_CCM_8": {"hex": 0xc0a8,"int": 49320,"recommend": "N" },
  "TLS_PSK_WITH_AES_256_CCM_8": {"hex": 0xc0a9,"int": 49321,"recommend": "N" },
  "TLS_PSK_DHE_WITH_AES_128_CCM_8": {"hex": 0xc0aa,"int": 49322,"recommend": "N" },
  "TLS_PSK_DHE_WITH_AES_256_CCM_8": {"hex": 0xc0ab,"int": 49323,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_AES_128_CCM": {"hex": 0xc0ac,"int": 49324,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_AES_256_CCM": {"hex": 0xc0ad,"int": 49325,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8": {"hex": 0xc0ae,"int": 49326,"recommend": "N" },
  "TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8": {"hex": 0xc0af,"int": 49327,"recommend": "N" },
  "TLS_ECCPWD_WITH_AES_128_GCM_SHA256": {"hex": 0xc0b0,"int": 49328,"recommend": "N" },
  "TLS_ECCPWD_WITH_AES_256_GCM_SHA384": {"hex": 0xc0b1,"int": 49329,"recommend": "N" },
  "TLS_ECCPWD_WITH_AES_128_CCM_SHA256": {"hex": 0xc0b2,"int": 49330,"recommend": "N" },
  "TLS_ECCPWD_WITH_AES_256_CCM_SHA384": {"hex": 0xc0b3,"int": 49331,"recommend": "N" },
  "TLS_SHA256_SHA256": { "hex": 0xc0b4, "int": 49332, "recommend": "N" },
  "TLS_SHA384_SHA384": { "hex": 0xc0b5, "int": 49333, "recommend": "N" },
  "TLS_GOSTR341112_256_WITH_KUZNYECHIK_CTR_OMAC": {"hex": 0xc100,"int": 49408,"recommend": "N" },
  "TLS_GOSTR341112_256_WITH_MAGMA_CTR_OMAC": {"hex": 0xc101,"int": 49409,"recommend": "N" },
  "TLS_GOSTR341112_256_WITH_28147_CNT_IMIT": {"hex": 0xc102,"int": 49410,"recommend": "N" },
  "TLS_GOSTR341112_256_WITH_KUZNYECHIK_MGM_L": {"hex": 0xc103,"int": 49411,"recommend": "N" },
  "TLS_GOSTR341112_256_WITH_MAGMA_MGM_L": {"hex": 0xc104,"int": 49412,"recommend": "N" },
  "TLS_GOSTR341112_256_WITH_KUZNYECHIK_MGM_S": {"hex": 0xc105,"int": 49413,"recommend": "N" },
  "TLS_GOSTR341112_256_WITH_MAGMA_MGM_S": {"hex": 0xc106,"int": 49414,"recommend": "N" },
  "TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256": {"hex": 0xccaa,"int": 52394,"recommend": "Y" },
  "TLS_PSK_WITH_CHACHA20_POLY1305_SHA256": {"hex": 0xccab,"int": 52395,"recommend": "N" },
  "TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256": {"hex": 0xccad,"int": 52397,"recommend": "Y" },
  "TLS_RSA_PSK_WITH_CHACHA20_POLY1305_SHA256": {"hex": 0xccae,"int": 52398,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_AES_128_GCM_SHA256": {"hex": 0xd001,"int": 53249,"recommend": "Y" },
  "TLS_ECDHE_PSK_WITH_AES_256_GCM_SHA384": {"hex": 0xd002,"int": 53250,"recommend": "Y" },
  "TLS_ECDHE_PSK_WITH_AES_128_CCM_8_SHA256": {"hex": 0xd003,"int": 53251,"recommend": "N" },
  "TLS_ECDHE_PSK_WITH_AES_128_CCM_SHA256": {"hex": 0xd005,"int": 53253,"recommend": "Y"}
}
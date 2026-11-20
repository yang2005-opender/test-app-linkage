import hashlib
import ssl

def test_deprecated_crypto():
    secret_data = "admin_password_123"
    # 故意硬编码引入废弃的 MD5 算法
    insecure_hash = hashlib.md5(secret_data.encode('utf-8')).hexdigest()
    print(f"Insecure MD5 Hash: {insecure_hash}")

def test_quantum_vulnerable_cert():
    # 加载传统的 RSA 量子脆弱证书
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="vulnerable_rsa_cert.pem", keyfile="vulnerable_rsa_key.pem")

if __name__ == "__main__":
    test_deprecated_crypto()
    test_quantum_vulnerable_cert()

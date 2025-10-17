from cryptography.hazmat.primitives import serialization
from getpass import getpass

def main():
    password = getpass("Mot de passe de la clé privée : ").encode()

    with open("ecc_private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=password
        )

    public_key = private_key.public_key()

    with open("ecc_public_key.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("✅ Clé publique extraite dans ecc_public_key.pem")

if __name__ == "__main__":
    main()


"""Verifie la signature d'un webhook Exantrix : X-Exantrix-Signature = sha256=<HMAC-SHA256(corps, jeton API)>."""
import hashlib
import hmac


def signature_valide(jeton_api: str, corps: bytes, entete: str) -> bool:
    attendu = "sha256=" + hmac.new(jeton_api.encode(), corps, hashlib.sha256).hexdigest()
    return hmac.compare_digest(attendu, entete or "")


if __name__ == "__main__":
    corps = open("exemple-webhook-commande.json", "rb").read()
    jeton = "votre-jeton-api"
    print(signature_valide(jeton, corps, "sha256=" + hmac.new(jeton.encode(), corps, hashlib.sha256).hexdigest()))

def ip_vers_entier(ip):
    """Convertit '192.168.1.10' en nombre entier de 32 bits."""
    a, b, c, d = map(int, ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d


def entier_vers_ip(n):
    """Convertit un entier de 32 bits en '192.168.1.10'."""
    return ".".join(str((n >> s) & 255) for s in (24, 16, 8, 0))


def calculer(ip, prefixe):
    ip_n = ip_vers_entier(ip)
    masque = (0xFFFFFFFF << (32 - prefixe)) & 0xFFFFFFFF
    reseau = ip_n & masque
    broadcast = reseau | (~masque & 0xFFFFFFFF)
    nb_hotes = max(2 ** (32 - prefixe) - 2, 0)

    return {
        "Adresse réseau": entier_vers_ip(reseau),
        "Masque": entier_vers_ip(masque),
        "Broadcast": entier_vers_ip(broadcast),
        "Première adresse": entier_vers_ip(reseau + 1),
        "Dernière adresse": entier_vers_ip(broadcast - 1),
        "Nombre d'hôtes": nb_hotes,
    }


def main():
    saisie = input("Entrez une adresse IP avec préfixe (ex: 192.168.1.10/24) : ")
    ip, prefixe = saisie.split("/")
    resultat = calculer(ip, int(prefixe))

    print()
    for cle, valeur in resultat.items():
        print(f"{cle} : {valeur}")


if __name__ == "__main__":
    main()
# Calculateur de sous-réseaux IP

Petit programme en Python qui calcule les informations d'un réseau IPv4
à partir d'une adresse IP et de son préfixe (notation CIDR).

## Fonctionnalités

- Adresse réseau
- Masque de sous-réseau
- Adresse de broadcast
- Première et dernière adresse utilisable
- Nombre d'hôtes

## Utilisation

Il faut avoir Python 3 installé.

```bash
python calculateur_ip.py
```

Le programme demande une adresse IP avec son préfixe, par exemple `192.168.1.10/24`.

## Exemple

```
Entrez une adresse IP avec préfixe (ex: 192.168.1.10/24) : 192.168.1.10/24

Adresse réseau : 192.168.1.0
Masque : 255.255.255.0
Broadcast : 192.168.1.255
Première adresse : 192.168.1.1
Dernière adresse : 192.168.1.254
Nombre d'hôtes : 254
```

## Comment ça marche

L'adresse IP est convertie en un entier de 32 bits. Des opérations sur les bits
(`&`, `|`, `~`, `<<`) permettent ensuite de calculer le masque, l'adresse réseau
et le broadcast.

## Idées d'amélioration

- Vérifier que l'adresse saisie est valide
- Diviser un réseau en plusieurs sous-réseaux
- Afficher les résultats en binaire

## Auteure

Mouna Afennich, étudiante en génie informatique.

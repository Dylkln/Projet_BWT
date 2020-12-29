## Projet_BWT

# Programme d'alignement de reads à une séquence / un génome de référence

## Transformée de Burrows-Wheeler.

## Prérequis

Aucun prérequis n'est nécessaire pour faire fonctionner ce programme.

## Télécharger le programme

1. Clonage du répertoire Github

> Lien HTTPS

```
git clone https://github.com/Dylkln/Projet_BWT.git
```

> Lien SSH

```
git clone git@github.com:Dylkln/Projet_BWT.git
```

## Utilisation du programme

```
python main.py -f <FASTA_FILE> -r <READS_FILE>
```

Avec les arguments suivants:

**OBLIGATOIRES**
- *FASTA_FILE* : Le fichier au format fasta contenant la séquence ou le génome.
- *READS_FILE* : Le fichier au format fasta contenant les reads.

##### Exemple d'utilisation

```
python main.py -f data/Hu-1.fasta -r data/READSsars_cov_2_1e6.fasta
```

##### Auteurs

Dylan KLEIN
Gwendolyn MARGUERIT

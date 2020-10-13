#!/usr/bin/env python3
# encoding: UTF-8     (compatibilité python2)

##################################
## INFO502: TP2
## Kevin Traini, groupe L3-info-3

import sys
import re


#########################################
## fonction à compléter pendant le TP...
def todo(r):
    return r.group(1).upper()


def titre(r):
    level = len(r.group(1))
    return f"<h{level}>{r.group(2)}</h{level}>"


def gras(r):
    return f"<b>{r.group(1)}</b>"


def souligne(r):
    return f"<u>{r.group(1)}</u>"


def process_line(line):
    line = line.replace("&", "&amp;")
    line = line.replace("<", "&lt;")
    line = line.replace(">", "&gt;")
    # Remplacement des emails
    line = re.sub("(?i)[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", "EMAIL", line)

    reg_images = "\[(([^\[\]]/)*[^\[\]]+(\.jpg|\.png|\.sgv|\.bmp))\]"
    if not re.findall(reg_images, line):  # Cette fonction trouve toutes les fois ou le regex fonctionne dans line
        # Remplacement des liens si ce n'est pas une image
        line = re.sub("(http[s]?://([a-zA-Z0-9-]+\.)+[a-z]{2,}(/[^/ ]*)*)", '<a href="\\1">\\1</a>', line)
    # Remplacement des images
    line = re.sub(reg_images, '<img src="\\1"/>', line)

    # Mise en majuscule des todo
    line = re.sub("^(TODO: .*)$", todo, line)

    # Remplacement des titres
    line = re.sub("^(=+)([^=](.*[^=])?)\1$", titre, line)

    # Mise en gras
    line = re.sub("\*\*([^ ](.*?[^ ])?)\*\*", gras, line)

    # Soulignement
    line = re.sub("__([^ ](.*?[^ ])?)__", souligne, line)

    return line


def is_comment(line):
    """ Code question 3
    i = 0
    while line[i] == ' ' or line[i] == '\t':
        i += 1

    if len(line) > i + 3:
        return line[i] == line[i + 1] == line[i + 2] == '%'
    else:
        return False"""

    return re.match("^[ \t]*%%%.*", line)


############################################################
## fonction principale, appelée depuis la ligne de commandes
def main():
    print("<!--", "-" * 70, "-->")
    for line in sys.stdin:
        # suppression des symboles de fin de ligne
        line = line.strip("\n\r")

        ## suppressions des lignes "commentaires"
        if is_comment(line):
            continue

        # traitement de la ligne
        line = process_line(line)

        # affichage de la ligne traitée
        print(line)
    print("<!--", "-" * 70, "-->")


if __name__ == "__main__":
    main()

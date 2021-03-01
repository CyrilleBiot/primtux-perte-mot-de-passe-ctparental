#/bin/bash
#
#__Source : https://github.com/CyrilleBiot/primtux-perte-mot-de-passe-ctparental 
#__author__ = "Cyrille BIOT <cyrille@cbiot.fr>"
#__copyright__ = "Copyleft"
#__site__ = "https://cbiot.fr"
#__license__ = "GPL"
#__version__ = "1.0"
#__email__ = "cyrille@cbiot.fr"
#__status__ = "Devel"
#__date__ = "2021/03/01"
#
#

# Test des droits d'execution
if [[ $EUID -ne 0 ]]; then
	echo "Ce script doit être lancé en root ou via sudo" 
	exit 1
fi

# Test si existence parametre IP 
if [[ $# -ne 2 ]]; then
	echo "ATTENTION. Ce script prend 2 paramètres."
	echo "Vérfier la syntaxe"
	echo "sudo bash perte-mot-de-passe-ctparental.sh <LOGIN> <PASSWORD>"
	exit 1
fi

if [[ -f  /var/www/CTadmin/arp1_md5.password  ]]; then
	echo "Le fichier de configuration existe, cool."
	else
	echo "Le fichier de configuration de CTparental ne semble pas exister."
	echo "Il doit y avoir un soucis plus profond. Contacter le forum primtux."
	echo "https://forum.primtux.fr/"
fi

# Nouveau fichier de configuration
  mv /var/www/CTadmin/arp1_md5.password /var/www/CTadmin/arp1_md5.password.BACKUP 
  MD5PWD=$(openssl passwd -apr1 -salt SALT $2)
  echo "$1:$MD5PWD" > /var/www/CTadmin/arp1_md5.password
  echo "Nouveau LOGIN : $1"
  echo "Nouveau MOT DE PASSE : $2"
  echo "Essayer de ne pas le perdre cette fois-ci..."

# primtux-perte-mot-de-passe-ctparental

## Késako
Juste un petit script bash pour les CTICE / ERUN qui configurent un primtux et oublient le mot de passe du contrôle parental ;), lol.

## Comment ça marche ?
Par défaut le mot de passe est stocké dans **/var/www/CTadmin/arp1_md5.password**.

Ce script fait un backup du fichier original en cas de soucis.

Syntaxe
Il doit être lancé depuis un compte root (**su -**) ou depuis **sudo**, c'est à dire avec les droits administrateurs.

 ```sudo bash perte-mot-de-passe-ctparental.sh <LOGIN> <MOT DE PASSE> ```
  
Prend donc impréativement 2 paramètres : **LOGIN** puis le **MOT DE PASSE**.

Le mot de passe sera "haché" / codé avec ces options :

```openssl passwd -apr1 -salt SALT ```

Et c'est tout ;)

## Restaurer le fichier original
Tout simplement 

 ```sudo mv /var/www/CTadmin/arp1_md5.password.BACKUP /var/www/CTadmin/arp1_md5.password ```

## Installer le script

 ```git clone https://github.com/CyrilleBiot/primtux-perte-mot-de-passe-ctparental.git
cd primtux-perte-mot-de-passe-ctparental
sudo bash perte-mot-de-passe-ctparental.sh <LOGIN> <MOT DE PASSE> ```


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  Source : https://github.com/CyrilleBiot/primtux-perte-mot-de-passe-ctparental
__author__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__copyright__ = "Copyleft"
__credits__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__license__ = "GPL"
__version__ = "1.0"
__date__ = "2021/03/03"
__maintainer__ = "Cyrille BIOT <cyrille@cbiot.fr>"
__email__ = "cyrille@cbiot.fr"
__status__ = "Devel"
"""

import os, subprocess
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class chgCtpPassword(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Python CPU Limit")

        if os.path.exists('.git'):
            self.pathDir = "./"
        # Launch since a deb package install
        else:
            self.pathDir = "/usr/share/pycpulimit/"

        self.set_border_width(10)
        self.set_resizable(False)
        self.set_icon_from_file(self.pathDir + "apropos.png")
        self.set_border_width(10)

        # Set Entry Widget to the login
        entryLogin = Gtk.Entry()
        entryLogin.set_text("Ici le nouveau login")
        entryLogin.set_width_chars(50)
        entryLogin.set_editable(True)

        # Set Entry Widget to the Password
        entryPwd1 = Gtk.Entry()
        entryPwd1.set_text("Ici le mot de passe")
        entryPwd1.set_width_chars(50)
        entryPwd1.set_editable(True)

        # Set Entry Widget to the Password
        entryPwd2 = Gtk.Entry()
        entryPwd2.set_text("De nouveau le mot de passe pour vérification.")
        entryPwd2.set_width_chars(50)
        entryPwd2.set_editable(True)

        # Set Button to Validate
        btnValidate = Gtk.Button(label="Générer Nouvelle association login / mot de passe")
        btnValidate.connect("clicked", self.testPassword, entryLogin, entryPwd1, entryPwd2)

        # Set label to rules for the new password
        lblInfo = Gtk.Label(label= "Le mot de passe doit contenir au moins\n"
                            "- 10 caractères \n"
                            "- des minuscules \n"
                            "- des majuscules \n"
                            "- des caractères spéciaux ($, @, #, %, (, ), [, ], !, :, ;)\n")
        lblInfo.set_line_wrap(True)
        lblInfo.set_justify(Gtk.Justification.LEFT)

        grid = Gtk.Grid()
        grid.set_column_spacing(6)
        grid.set_row_spacing(6)
        #grid.set_row_homogeneous(False)
        grid.attach(entryLogin, 0, 0, 1, 1)
        grid.attach(lblInfo,0,1,1,1)
        grid.attach(entryPwd1, 0, 2, 1, 1)
        grid.attach(entryPwd2, 0, 3, 1, 1)
        grid.attach(btnValidate,0,4,1,1)

        self.add(grid)

    def testPassword(self, button, login, password1, password2):
        """
        :param button:
        :param login: login
        :param password1: mot de passe 1
        :param password2: mot de passe 2
        :return:
        """

        # Récupération des mots de passe
        password1 = password1.get_text()
        password2 = password2.get_text()

        # Et du login
        login = login.get_text()

        # Cactères spéciaux
        SpecialSym = ['$', '@', '#', '%','(',')','[',']','!',':',';']

        # Chaine de test
        if password2 != password1:
            self.warning_alert(self,"Attention","Les 2 mots de passe ne sont pas identiques.")
        elif len(password1) < 10:
            self.warning_alert(self,"Attention","Le mot de passe doit contenir au moins 10 lettres.")
        elif not any(char.isdigit() for char in password1):
            self.warning_alert(self,"Attention","Le mot de passe doit contenir au moins 1 chiffre")
        elif not any(char.isupper() for char in password1):
            self.warning_alert(self,"Attention","Le mot de passe doit contenir au moins 1 lettre majuscule.")
        elif not any(char.islower() for char in password1):
            self.warning_alert(self,"Le mot de passe doit contenir au moins 1 lettre minuscule.")
        elif not any(char in SpecialSym for char in password1):
            self.warning_alert(self, "Attention", "Le mot de passe doit contenir au moins 1 caractère spcécial.")
        else:
            self.warning_OK(self,"Nickel", "Le mot de passe est conforme aux attentes. Cliquer sur OK/VALIDER.")
            # On lance la modification du mot de passe.
            cmd_shell = "sudo CTparental -setadmin " + login + " "  + password2 + "&> /dev/null"
            os.system(cmd_shell)
            self.warning_OK(self,"Nickel", "Le couple <LOGIN> / <MOT DE PASSE> a été mise à jour.")


    def gtk_style(self):
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(self.pathDir + 'style.css')

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    def warning_alert(self, widget, message1, message2):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.CANCEL,
            text=message1,
        )
        dialog.format_secondary_text(message2)
        dialog.run()
        dialog.destroy()

    def warning_OK(self, widget, message1, message2):
        """
        FOnction ouvrant une dialog box d'alerte
        :param widget:
        :param message1: Le titre du message
        :param message2: Le contenu du message
        :return:
        """
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=message1,
        )
        dialog.format_secondary_text(message2)
        dialog.run()
        dialog.destroy()




win = chgCtpPassword()
win.connect("destroy", Gtk.main_quit)
win.gtk_style()
win.show_all()
Gtk.main()
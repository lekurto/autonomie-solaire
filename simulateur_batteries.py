#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:44:50 2023

@author: nicolas
"""
import streamlit as st

st.title("Dimensionnez votre installation solaire avec notre simulateur")
st.header("1. Dimensionnement de votre besoin")

consommation_quotienne = st.number_input("Consommation quotidienne (Wh)", value = 10000, min_value = 0, step= 100, help = "Un appartement de 50 m² occupé par deux personnes consomme quotidiennement environ 30 kWh.")

nb_jours = st.slider("Combien de jours souhaitez-vous tenir sans devoir recharger vos batteries?", value = 2, min_value = 1, max_value = 10)

marge = st.number_input("Souhaitez-vous une marge de sécurité pour brancher d'autres appareils ? (%)", min_value = 0, max_value = 100, step = 1, value = 0 )

besoin = consommation_quotienne * nb_jours * (1 + marge / 100)

st.write("Sur la base de ces informations, vous avez besoin de ", round(besoin / 1000, 2) , "kWh.")

st.header("2. Caractéristiques des batteries")

capacite_batterie = st.number_input("Capacité des batteries", value = 1000, min_value=0, step = 100)
unite_capacite = st.selectbox("En quelle unité est exprimée cette capacité ?", ('Wh', 'Ah'))


if unite_capacite == "Ah":
    tension_batterie_reponse = st.selectbox('Quelle est la tension de sortie des batteries (V)', ('12 V', '110 V', '220 V'))
    tension = tension_batterie_reponse.split(' ')[0]

profondeur_de_decharge = st.number_input("Jusqu'à quel % de décharge utiliserez-vous vos batteries ? (de 100 % jusqu'à ... % ?)", value = 10, min_value=0, max_value=50)

if unite_capacite == "Wh":
    watts_batterie = capacite_batterie
elif unite_capacite == "Ah":
    watts_batterie = tension * capacite_batterie

puissance_reelle = watts_batterie * (100- profondeur_de_charge) / 100
st.write("Chaque batterie a une capacité utilisable de ", puissance_reelle / 1000, "kiloWatt heures")

st.header("Conclusion")

nb_batteries = besoin / puissance_reelle
st.write("Vous avez donc besoin de batteries", nb_batteries, "ayant les caractéristiques mentionnées.")
st.write("Voici les modèles qui correspondent à ce besoin :")

st.write("Ecoflow : Capacité de la batterie:  3600Wh , tension 220V")
# # Calculations
# amh_heures = consommation_quotienne / tension_batterie
# total_ampere_heures = amh_heures * 2 * (1 + margin / 100)

# capacite_relle_batterie = capacite_batterie * (profondeur_de_charge / 100)
# num_batteries = total_ampere_heures / capacite_relle_batterie

# # Output result
# st.write("Compte tenu de votre consommation quotidienne, vous avez besoin de ", amh_heures, "ampère heures en batteries.")
# st.write("Multiplions ce chiffre par deux pour tenir compte des journées sans soleil, cela nous donne ",  amh_heures *2 , "ampère heures nécessaire pour 2 jours.")
# st.write("Ajoutons une marge de sécurité de", margin, "%, nous arrivons à ", amh_heures * 2 * (1 + margin), " Ah nécessaires.")

# st.write("Vos batteries ayant une capacité de ", capacite_batterie, " sur laquelle nous allons considérer que seuls ", profondeur_de_charge, "% seront utilisés, il vous faut donc :")

# st.write(f"Number of batteries needed: {num_batteries}")



# https://www.victronenergy.fr/upload/documents/Optimiser-la-vie-des-batteries-plomb-Le%C3%A7on-V02-Bis.pdf
employes = {
            "01": {
                "identite": {
                    "prenom": "Pierre",
                    "nom": "Dupont"
                    }
                }
            }

resultat = employes.get("01").get("identite").get("prenom")
print(resultat)
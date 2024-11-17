def isResponseEmpty(response):
    return not bool(response)

def create_dict_gravite(gravite, date_debut, date_fin):
    return {
        "gravite": gravite,
        "date_debut": date_debut,
        "date_fin": date_fin,
    }

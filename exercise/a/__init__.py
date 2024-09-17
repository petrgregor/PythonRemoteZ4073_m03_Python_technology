def try_again():
    vote = input("\nChceš to zkusit znovu? (A/a/Y/y - Ano; N/n - Nie): ")
    votes_map = {
        "A": True,
        "a": True,
        "Y": True,
        "y": True,
        "N": False,
        "n": False
    }

    return votes_map[vote]

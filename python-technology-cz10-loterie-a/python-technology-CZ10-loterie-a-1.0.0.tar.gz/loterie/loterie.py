from .kostka import hod_kostkou_s_progress_barem


KONFETTI_EMOJI = "\U0001F389"
SMUTNE_EMOJI = "\U0001F641"
NADSENE_EMOJI = "\U0001F929"


def _oznameni_vysledku(hozena_cisla, vyhra=False):
    print(f"Padla tato cisla: {hozena_cisla}")
    if vyhra:
        print(f"{KONFETTI_EMOJI * 3} Vyhral si loterii, gratulejeme! {KONFETTI_EMOJI * 3}")
    else:
        print(f"{SMUTNE_EMOJI * 3} Prohral si loterii, priste bude urcite vetsi stesti! {NADSENE_EMOJI * 3}")


def _jedna_hra_v_loterii(pocet_vyhernich_cisel=2, pocet_hodu=5, vyherni_cislo=6):
    pocet_provedenych_hodu = 0
    pocet_hozenych_vyhernich_cisel = 0

    hozena_cisla = []
    while pocet_provedenych_hodu < pocet_hodu:
        hozene_cislo = hod_kostkou_s_progress_barem(
            popisek_hodu=f"Hod cislo: {pocet_provedenych_hodu + 1}", delka_hodu_v_sekundach=3
        )
        hozena_cisla.append(hozene_cislo)
        pocet_provedenych_hodu += 1
        print(f"Padlo cislo {hozene_cislo}!\n")

        if hozene_cislo == vyherni_cislo:
            pocet_hozenych_vyhernich_cisel += 1

        if pocet_hozenych_vyhernich_cisel == pocet_vyhernich_cisel:
            _oznameni_vysledku(hozena_cisla, True)
            return

    _oznameni_vysledku(hozena_cisla, False)


def hrat_loterii(pocet_vyhernich_cisel=2, pocet_hodu=5, vyherni_cislo=6):
    while True:
        _jedna_hra_v_loterii(pocet_vyhernich_cisel, pocet_hodu, vyherni_cislo)
        vstup = input("Ches hrat znovu? (ano/ne)")
        if vstup.lower() != "ano":
            break


if __name__ == "__main__":
    hrat_loterii()


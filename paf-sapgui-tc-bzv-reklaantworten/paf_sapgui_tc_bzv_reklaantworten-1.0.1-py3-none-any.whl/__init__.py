from typing import NoReturn

import pendulum
from paf_sapgui import transaction, key, window, session, button
from paf_sapgui.session import active
from paf_sapgui_cic.flows import position_details
from paf_tools import configuration, email

from elements import zjkta_nb_rklsm

_rounds_count = 0
_incident_count = 0


def main():
    # Konfiguration des Protokolls

    the_errors = []

    print("Starte Testfall 'BZV_Reklaantworten'")

    preparations()
    login()

    if prepare_transaction():
        the_errors = analyse_table()

        if len(the_errors) > 0:
            #    for items in analysed_data:
            #        the_errors.append(items.Value)

            cic(the_errors)
            reject(the_errors)
        else:
            print("Keine Einträge zur Verarbeitung gefunden.")
    else:
        print("Keine Einträge zur Verarbeitung gefunden.")

    protocol(_rounds_count, _incident_count, the_errors)
    session.destroy()


def protocol(rounds: int, incidents: int, errors: list):
    credentials_sending_mails = configuration.credentials("sendMails")
    signature = configuration.get("signatures", "ses_allgemein")

    email_object = email.Email()
    email_object.login_credentials(username=credentials_sending_mails.user, password=credentials_sending_mails.password)
    email_object.sender("christian.koester@axelspringer.com")
    mail_text = f"Hallo zusammen! <br /><br />{text_for_message(the_errors=errors, rounds=rounds, incidents=incidents)}<br /><br />Lieben Gruß<br/>Deine Automatisierung -)<br />{signature}"

    if _rounds_count > 2 or _incident_count > 20:
        email_object.receiver("christian.koester@axelspringer.com")
        email_object.content(subject="BZV - Reklaantworten - Fehler", text=mail_text)
    else:
        email_object.receiver("christian.koester@axelspringer.com")
        email_object.content(subject="BZV - Reklaantworten - keine Auffälligkeiten", text=mail_text)
    email_object.send()


def text_for_message(the_errors: list, rounds: int, incidents: int) -> str:
    email_text = f"Ich habe {(rounds + 1)} Schleifen gedreht und dabei  {incidents} Vorfälle gefunden!<br />"
    if the_errors:
        email_text += "<ul>"
        for error_item in the_errors:
            email_text += "<li>"
            email_text += f"Objektnummer: {error_item['Objektnummer']}, VBELN: {error_item['VBELN'][:-1]}"
            email_text += f", Text: {error_item['Text']}"
            email_text += f", Datum: {error_item['Datum'][6:2]}.{error_item['Datum'][4:2]}.{error_item['Datum'][:4]}" \
                          f" ({error_item['Datum']})"
            email_text += ", Verarbeitungsstatus: " + (
                "OK" if error_item['is_changed'] else ("Verarbeitungsfehler: " + error_item['error_text']))

            email_text += "<li>"
    else:
        email_text += "<b>"
        email_text += "Es wurden keine Fehler gefunden"
        email_text += "</b>"
    return email_text


def preparations():
    print("Vorbereitungen")


def login() -> NoReturn:
    session.create("SapV30Ckoeste1")


def reject(values_to_reject=list):
    print("Weise die bearbeiteten Aufträge in der ZJKTA_NB_RKLSM ab")
    transaction.open("ZJKTA_NB_RKLSM")

    active.session.findById(zjkta_nb_rklsm.gruppenschluessel_ai).text = "BZV"
    active.session.findById(zjkta_nb_rklsm.status_abo_interface).text = "U"

    for single_value in values_to_reject:
        active.session.findById(zjkta_nb_rklsm.objektnummer).text = single_value["Objektnummer"]
        key.f8()
        if not window.exists(1, go_on=True):
            active.session.findById(zjkta_nb_rklsm.tabelle).click(0, "STATUS")
            button.click(6, 0, 1)

        button.back()


def cic(values_to_process: list):
    print("Verarbeitung im CIC")

    for index, single_value in enumerate(values_to_process):
        message_date = pendulum.datetime(int(single_value['Datum'][:4]), int(single_value['Datum'][4:6]),
                                         int(single_value['Datum'][6:8]))
        vbeln = single_value['VBELN'][:-1]

        new_text = f"{pendulum.now().format('DD.MM.YYYY HH:mm')}: {message_date.format('DD.MM.YYYY')} [Automatik SyMa] -> {single_value['Text']}"

        print(f"Verarbeitung im CIC! VBELN = {vbeln}, Text: {new_text}")

        is_changed, error_text = position_details.change_text(vbeln, new_text, False)
        values_to_process[index]["is_changed"] = is_changed
        values_to_process[index]["error_text"] = error_text


def analyse_table():
    global _incident_count
    print("Analysiere Tabelle")
    found_incidents = []

    if not window.exists(1, close_window=True):
        table_object = active.session.findById(zjkta_nb_rklsm.tabelle)

        row_count = table_object.rowCount

        print(f"Anzahl Reihen: {row_count}")
        for row in range(row_count):
            table_object.selectedRows = str(row)
            table_object.doubleClick(str(row), "OBJEKTNR")
            details_table_object = active.session.findById(zjkta_nb_rklsm.detail_tabelle)
            temp = {
                "Objektnummer": details_table_object.getCellValue(0, "WERT"),
                "VBELN": details_table_object.getCellValue(5, "WERT"),
                "Text": details_table_object.getCellValue(18, "WERT"),
                "Datum": details_table_object.getCellValue(13, "WERT"),
                "is_changed": False,
                "error_text": None
            }
            found_incidents.append(temp)
            _incident_count += 1
            key.back()

    # Objektnummer 1, 2 \
    # VBELN = 6, 2 \
    # Text = 19, 2 \
    # Datum = 15, 2

    return found_incidents


def prepare_transaction() -> bool:
    print("Schaue in Transaktion ZJKTA_NB_RKLSM nach Einträgen")
    transaction.open("ZJKTA_NB_RKLSM")

    active.session.findById(zjkta_nb_rklsm.gruppenschluessel_ai).text = "BZV"
    active.session.findById(zjkta_nb_rklsm.status_abo_interface).text = "U"
    dt = pendulum.now()
    active.session.findById(zjkta_nb_rklsm.angelegt_am_von).text = dt.start_of("month").format('DD.MM.YYYY')
    active.session.findById(zjkta_nb_rklsm.angelegt_am_bis).text = dt.end_of("month").format('DD.MM.YYYY')
    key.f8()
    if window.exists(window_id=1, go_on=True):
        return False
    return True


if __name__ == "__main__":
    main()

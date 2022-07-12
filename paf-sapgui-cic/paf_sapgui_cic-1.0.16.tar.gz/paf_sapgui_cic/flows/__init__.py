from paf_sapgui import window, transaction, table
from paf_sapgui.session import active
from paf_sapgui.statusbar import message as statusbar_message
from .. import elements


def open_order(order_number: str) -> bool:
    if window.get_title() != "Customer-Interaction-Center":
        transaction.open("cic0")
    else:
        active.session.findById(elements.Geschaeftspartner.alle_felder_initialisieren).press()

    active.session.findById(elements.Geschaeftspartner.suchdaten).text = order_number
    active.session.findById(elements.Geschaeftspartner.manuelle_identifikation).press()
    if statusbar_message.get_text() == "Es konnten keine Adressen gefunden werden":
        return False

    if active.session.findById(elements.Suchergebnisse.tabs).selectedTab.text == "Hitliste":
        active.session.findById(elements.Suchergebnisse.Hitliste.tabelle).selectedRows = "0"
        active.session.findById(elements.Suchergebnisse.Hitliste.tabelle).doubleClickCurrentCell()
    return True


def select_order(order_number, order_type: str = None) -> int:
    table_element = active.session.findById(elements.Auftrage.MSD_Auftraege.tabelle)
    search_parameters = [{"column": "VBELN", "value": order_number}]
    row_number = None

    if order_type is not None:
        search_parameters.append({"column": "POART_EX", "value": order_type})

    for row_counter in range(table_element.rowCount):
        found = False
        for search_parameter in search_parameters:
            cell_content = table_element.getCellValue(row_counter, search_parameter["column"])
            if cell_content == search_parameter["value"]:
                found = True
        if found:
            row_number = row_counter
            break

    if row_number is not None:
        table_element.selectedRows = str(row_number)
        return row_number
    print(f"It was not possible to find the desired order {order_number} - {order_type}")


if __name__ == "__main__":
    pass

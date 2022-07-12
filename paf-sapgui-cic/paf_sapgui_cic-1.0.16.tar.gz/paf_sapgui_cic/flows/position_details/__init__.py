from ... import flows
from paf_sapgui.statusbar import message
from paf_sapgui.session import active
from ... import elements


def change_text(order_number: str, the_text: str, overwrite: bool = False) -> tuple[bool, str | None]:
    order_displayed = flows.open_order(order_number)
    if not order_displayed:
        return False, message.get_text()
    row_number = flows.select_order(order_number)
    active.session.findById(elements.Auftrage.MSD_Auftraege.details_zur_position_anzeigen).press()
    active.session.findById(elements.Auftrage.MSD_Auftraege.Details_zur_Position.Tabs.text).select()
    active.session.findById(elements.Auftrage.MSD_Auftraege.Details_zur_Position.Text.anzeigen_aendern).press()

    text_element = active.session.findById(elements.Auftrage.MSD_Auftraege.Details_zur_Position.Text.text_element)
    if not overwrite:
        existing_text = text_element.text
        new_text = the_text + "\n\n" + existing_text
        text_element.text = new_text
    else:
        text_element.text = the_text

    active.session.findById(elements.Auftrage.MSD_Auftraege.Details_zur_Position.Text.sichern).press()

    return True, None

from django.utils.translation import gettext_lazy as _


class GiftCardCrawler:

    class Meta:
        app_label = 'gift_card_crawler'
        object_name = 'gift_cards_crawler'
        model_name = module_name = 'gift_cards_crawler'
        verbose_name = _('gift card crawler')
        verbose_name_plural = _('gift cards crawler')
        abstract = False
        swapped = False
        app_config = ""

    _meta = Meta()

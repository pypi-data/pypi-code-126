import re

from django.utils.text import slugify


def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug. Chop its length down if we need to.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create a queryset, excluding the current instance.
    if not queryset:
        queryset = instance.__class__._default_manager.all()
        if instance.pk:
            queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '-%s' % next
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len - len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator=None):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
        value = re.sub('%s+' % re_sep, separator, value)
    return re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)


def get_english_date(nepali_date_string):
    import nepali_datetime
    date_format_string = "%Y-%m-%d"
    try:
        # gives instance of nepali_datetime.datetime object
        nepali_date = nepali_datetime.datetime.strptime(nepali_date_string, date_format_string)
    except ValueError:
        return
    eng_date = nepali_datetime.date(nepali_date.year, nepali_date.month, nepali_date.day).to_datetime_date()
    return eng_date


def get_nepali_date(eng_date_string):
    import datetime
    import nepali_datetime
    date_format_string = "%Y-%m-%d"
    try:
        # returns datetime.datetime object
        english_date_obj = datetime.datetime.strptime(eng_date_string, date_format_string)
    except ValueError:
        return
    return nepali_datetime.date.from_datetime_date(english_date_obj.date())


def get_bs_datetime_obj(eng_datetime_obj):
    """

    :param eng_datetime_obj: Datetime object (not a string it should be object as in DB)
    :return: Datetime object in Nepali system (BS)
    """
    import nepali_datetime
    from django.utils import timezone
    time_zoned_datetime = timezone.make_aware(timezone.make_naive(eng_datetime_obj))
    nepali_date = nepali_datetime.date.from_datetime_date(time_zoned_datetime.date())
    bs_date_time = nepali_datetime.datetime.combine(nepali_date, time_zoned_datetime.time())
    return bs_date_time

def uebergebe_sk_pk(stream_klasse, pk, sk, kontext, server_kontext):
    """ Funktion, um dem Handler fuer die Clients Argumente zu uebergeben """
    def wrapper(*args, **kwargs):
        """ Die vorgetaeuschte Funktion """
        return stream_klasse(pk, sk, kontext, server_kontext, *args, **kwargs)
    return wrapper

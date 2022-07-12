def validar_args(topico, bootstrap_servers, productor, atm, ventas, consumidor):
    assert topico is not None, "Err: debe definir '--topico <topico objetivo para el productor/consumidor>'"
    assert isinstance(topico, str)
    assert bootstrap_servers is not None, "Err: debe definir '--bootstrap_servers <lista de servidores>'"
    assert isinstance(bootstrap_servers, str)
    # Productor o consumidor tiene que estar definido
    assert productor or consumidor, "Err: debe definir una de las siguientes opciones '--productor', '--consumidor'"
    assert not(productor and consumidor), "Err: no es posible crear productor y consumidor a la vez. Defina solo una opcion '--productor' o '--consumidor', no ambos"
    # Si productor está definido, se tiene que tener definido atm o ventas
    if productor:
        assert atm or ventas, "Err: debe definir una de las siguientes opciones '--atm', '--ventas'"
        if atm:
            assert not ventas, "Err: no es posible crear un productor para mas de un ejemplo. Defina solo '--atm' o '--ventas', no ambos"
        if ventas:
            assert not atm, "Err: no es posible crear un productor para mas de un ejemplo. Defina solo '--atm' o '--ventas', no ambos"
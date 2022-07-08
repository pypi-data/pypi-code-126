def get_nombre_arch(archivos):
    def get_name(texto):
        a=texto.split('.')

        if len(a)==2:result=a[0]
        elif len(a)>2:result='.'.join(a[:-1])
        else:result=None

        return result

    if type(archivos) == str:
        return get_name(archivos)

    else:
        cont=0
        for arch in archivos:
            if get_name(arch):cont+=1

        return cont



a=['casa.txt','pruebas.py','auto.fdf','solo.dfsd']
b='solo'


#print(get_nombre_arch(a))
print(get_nombre_arch(b))
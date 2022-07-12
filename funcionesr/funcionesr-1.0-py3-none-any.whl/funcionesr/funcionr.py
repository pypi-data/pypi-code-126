from rpy2.robjects import r

def funcionrsaludo():
    r('print("¡Hola Mundo!")')

def funcionrnprimo():
    r(
    '''
    # R code for Finding composite  and prime numbers  upto 100
    # initialize number n
    n=100
    
    # arranging sequence
    x = seq(1, n)
    
    # creating an empty place to store the numbers
    prime_numbers=c()
    
    composite_numbers = c()
    for (i in seq(2, n)) {
    if (any(x == i)) {
    
        # prime numbers gets stored in a sequence order
        prime_numbers = c(prime_numbers, i)
        x = c(x[(x %% i) != 0], i)
    }
    
    else{
    
        # composite numbers gets stored in a sequence order
        composite_numbers = c(composite_numbers, i)
    }
    }
    
    # printing the series
    print("prime_numbers")
    print(prime_numbers)
    
    print("composite_numbers")
    print(composite_numbers)
    ''')

def funcionresprimo(number):
    r('''
    # Nombre del programa: Prueba de primalidad.

    es_primo <- function(numero) {
    contador <- 0
  
    for (i in 0:numero) {
        if (numero %% (i+1) != 0) {
        next
        } else {
            contador <- contador + 1
        }
        }
    if (contador == 2) {
        print('Es primo')
    } else {
        print('No es primo')
    }
    }

    
    run <- function() {
    numero <- as.integer(readline('Ingrese un número: '))
    es_primo(numero)
    }

    
    run()
    ''')
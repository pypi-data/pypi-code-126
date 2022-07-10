from rpy2.robjects import r 

def printPrimeNumbers(maxNum):
    r.assign('maxNum', maxNum)
            
    r('''     
        prime_numbers=c()   
        contador<-0  #contador para saber cuantos divisores tiene un numero
        for(num in 1:maxNum){
            if(num > 1){
                for(i in 2:num){
                    if(num %% i == 0){
                        contador<-contador+1   
                    }
                }
                if(contador ==1 ){  #solo ha sido divisible por él mismo
                    prime_numbers = c(prime_numbers, i)
                    
                }
                contador<-0   #se resetea el contador de divisores
            }
        }
        
        #print(prime_numbers)
    ''')

    prime_numbers = r('prime_numbers')
    print("Los números primos entre 1 y", maxNum, "son:",prime_numbers)
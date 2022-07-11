import math
from sys import argv


user_dict = []
payment_dict = []


def loan(input_array):
    
    
    loan_input = []
    loan_input= input_array
    
    
    bankScheme = loan_input[0]
    bankName = loan_input[1]
    userName = loan_input[2]
    principal = int(loan_input[3])
    years = int(loan_input[4])
    rate = int(loan_input[5])

    interest = math.ceil((principal * years * rate )/100)
    totalLoan= principal + interest

    userData = [userName,bankName,interest, totalLoan,years,totalLoan]
    user_dict.append(userData)
    
    

def payment(input_array):
    
    bank = input_array[1]
    user = input_array[2]
    lumpSum = int(input_array[3])
    emiForLumpSum = int(input_array[4])
    
    paymentArray = [bank,user,lumpSum,emiForLumpSum]
    
    payment_dict.append(paymentArray)


    
def balance(input_array,user_dict,payment_dict):
    
    bankNameByInput = input_array[1]
    userNameByInput = input_array[2]
    emisPaid = input_array[3]
    
    emisPaid  = int(emisPaid)

    amountPaidTill=0
    remainingEmis= 0 
    emiPerMonth = 0 
    
    
    
    for i in range(len(user_dict)):
        if(bankNameByInput == user_dict[i][1] and userNameByInput == user_dict[i][0]):
            emiPerMonth = math.ceil(user_dict[i][3]/(user_dict[i][4]*12))
            
            remainingEmis =  (user_dict[i][4] * 12) - (emisPaid)
            
            amountPaidTill = (emisPaid * emiPerMonth)
            
            
    for j in range(len(payment_dict)):
        if(bankNameByInput == payment_dict[j][0] and userNameByInput == payment_dict[j][1] ):
            
            checkAmount = amountPaidTill + int(payment_dict[j][2])
            
            reviewbalance = (int(user_dict[j][5]) - checkAmount)
            
            if((int(user_dict[j][5]) - checkAmount) < (emiPerMonth * remainingEmis)):
                amountPaidTill = checkAmount
                remainingEmis = math.ceil(reviewbalance/emiPerMonth)
            
     
    print(bankNameByInput,userNameByInput,amountPaidTill,remainingEmis)       
    return(bankNameByInput,userNameByInput,amountPaidTill,remainingEmis)      
       

    
            
            
            
def main():

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    #print(Lines)
    
    input_arg= []
    
    for i in range(len(Lines)):
    
        input_arg.append(Lines[i].split(" "))
    
    bankNameByInput,userNameByInput,amountPaidTill,remainingEmis = '','',0,0
    
    
    for i in range(len(input_arg)):
        if(input_arg[i][0] == "LOAN"):
            loan(input_arg[i])
            
        elif(input_arg[i][0] == "BALANCE"):
            bankNameByInput,userNameByInput,amountPaidTill,remainingEmis = balance(input_arg[i],user_dict,payment_dict)
            
        elif(input_arg[i][0] == "PAYMENT"):
            payment(input_arg[i])
            
        
        
    
if __name__ == "__main__":
    main()
    
    
    

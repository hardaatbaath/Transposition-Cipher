import math
def split_len(seq, key):
    final=""
    
    seq+=((key-(len(seq)%key))*" ")
    a=[seq[i:i + key] for i in range(0, len(seq), key)]
    for i in range(key):
        for j in range(len(a)):
            final+=str(a[j][i])
    return final+'.'

def decrypt(message,key):
    ans=""
    message=message[:len(message)-2]
    if(message[len(message)-1]==' '):
        message=message[:len(message)-2]
    for i in range(len(message)):
        # ans+=message[((key+1)*i)%len(message)]
        ans+=message[(math.ceil((len(message))/key)*i)%len(message)]
        i+=1
    return ans

def main():
    check=1
    while(check!=0):
        try:
            choice=input("Enter \'Encrypt\' for Encryption and \'Decrypt\' for Decryption : ")
            if(choice.lower()=="encrypt"):
                string=input("Enter the Message : ")
                no=int(input("Enter the Encryption key (1-10) : "))
                print(split_len(string,no))
            elif(choice.lower()=="decrypt"):
                string=input("Enter the Encryption (with the dot): ")
                no=int(input("Enter the Encryption key (1-10) : "))
                print(decrypt(string,no))
            else:
                print("Wrong input. Try again...")
                continue
            check=int(input("Enter 0 to exit, anything else to continue : "))

        except:
            print("Error, Restarting...")


if(__name__=="__main__"):
    main()

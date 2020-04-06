import  Encrypter

class data_lines:

    @staticmethod
    def add_data_to_file(site,username,password):
        file=open('MySafe.txt','r')
        line_inx=str(len(file.readlines()))
        enc_site=Encrypter.encrypt(site)
        enc_username=Encrypter.encrypt(username)
        enc_password = Encrypter.encrypt(password)
        with open("MySafe.txt","a") as file:
            string=line_inx+','+enc_site+','+enc_username+','+enc_password+'\n'
            file.write(string)

    @staticmethod
    def deleted_lines(del_rows):
        file=open('MySafe.txt','r')
        lines=file.readlines()
        file.close()
        file=open('MySafe.txt','w')
        i=0
        for line in lines:
            linelist=line.split(',')
            if int(linelist[0]) != del_rows:
                linelist[0]=str(i)
                string=''+linelist[0]+','+linelist[1]+','+linelist[2]+','+linelist[3]
                file.write(string)
                i+=1

    @staticmethod
    def clear_all():
        f=open("MySafe.txt",'w')
        f.close()

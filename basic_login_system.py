user_name = "asd"
password = 1234


def login(user_name, password):
   user_password = False
   hak = 3
   while hak > 0:    
    user_input = input("Kullanıcı adını giriniz: ").strip()
    if user_input == user_name:
        name_ok = True 
    else:
        name_ok = False
    
    try:
        user_pass = int(input("Şifre giriniz: ").strip())
        if user_pass == password:
            user_password = True
            
        if name_ok == True and user_password == True:
            print("----> Hoşgeldiniz...")
            break
        
        if name_ok == False and user_password == True:
            hak -= 1
            print(f"kullanıcı adı veya şifre yanlış, kalan deneme hakkı {hak}")
            
        elif name_ok == False and user_password == False or name_ok == True and user_password == False:
            hak -= 1
            print(f"kullanıcı adı veya şifre yanlış, kalan deneme hakkı {hak}")
            
    except ValueError:
         print("Lütfen rakam giriniz.")        

login(user_name, password)
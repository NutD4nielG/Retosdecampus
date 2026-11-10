ruta_arch = "D:\\CAMPUSLANDS\\VsC\\Python 1\\Archivos\\mbox.txt"

ruta_dest = "D:\\CAMPUSLANDS\\VsC\\Python 1\\Archivos\\ejemploparamanana.txt"

with open(ruta_arch, "r",encoding="utf-8") as arch, \
    open(ruta_dest, "w",encoding="utf-8") as dest:
    emails = list()
    for linea in arch:
        if linea.startswith("From:"):
            emails.append(linea.split(" ")[-1].strip())

    lst_emails = list(emails)
    lst_emails.reverse() 
    for correo in lst_emails:
        print(f"{correo} enviado [OK]")
        dest.writelines(f"{correo} enviado [OK]\n")

    print("Proceso terminado")
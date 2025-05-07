

#Jaychael Colon Aponte
#Registro de Empleados en Python


import sys

#Funcion para localizar la persona por su numero de ID
def find_person_by_id(person_list, id,person_id):
    for person in person_list:
        if person["id"] == id: #Verifica que el ID entrado vaya de acorde a la persona
            view_person(person)
            return person_id
    print ('The ID entered is cannot be found in the database.')
    return person_id


def handle_find_person_by_id(person_list,person_id):
    idinput = input('Enter the person ID: ')
    if idinput.isdigit():
        id = int(idinput)
        return find_person_by_id(person_list, id,person_id)
    else:
        print ('Error: The format was not a number.')
        return person_id

#Funcion para añadir una persona junto a su informacion en el formato presentado.
def add_person(first_name, last_name, age, birth, person_list, person_id):
    new_person = {"id" : person_id, "first_name" : first_name, "last_name" : last_name, "age" : age, "birth" : birth} 
    person_list.append(new_person)
    return person_id + 1


def handle_add_new_person(person_list, person_id):
    print ("Employee information format: First Name, Last Name, Age, Birth Month, Birth Day, Birth Year")
    person_info = input("Enter the person information: ")
    person_data = person_info.split(",")
    if len(person_data) < 6 or len(person_data) > 6:
        print ('Incorrect format!') 
        return person_id
    if person_data[2].isdigit() and person_data[3].isdigit() and person_data[4].isdigit() and person_data[5].isdigit:
        birth_date = (person_data[3], person_data[4], person_data[5])
        upd_person_id = add_person(person_data[0], person_data[1], person_data[2], birth_date, person_list, person_id)
        print ('Employee has successfully been added to the list!')
        return upd_person_id
    else:
        print ('Birthdate or age is not a number!') #Error que comunmente puede salir, ya que no se deben escibir espacios luego de los numeros cuando se entre la informacion.
        return person_id

    #Funcion para encontrar una persona utilizando su nombre y apellido
def find_person_by_name(first_name, last_name, person_list,person_id):
    for person in person_list:
        if (str(person["first_name"]) == first_name) and (str(person["last_name"]) == last_name):
            view_person(person)
            return person_id
    print ('Employee could not be found in the database.')
    return person_id


def handle_find_person_by_name(person_list,person_id):
    print ('Format for finding person by name: Name,Last Name')
    name_input = input('Enter person name [CAPS SENSITIVE!]: ')
    person_data = name_input.split(",")#Divide el nombre entre una tupla, por si personas comparten el mismo nombre o apellido
    if len(person_data) >= 3 or len(person_data) <= 1:
        print ('Error: Incorrect information format.')
        return person_id
    else:
        first_name = str(person_data[0])
        last_name = str(person_data[1])
        return find_person_by_name(first_name, last_name, person_list,person_id)

#Funcion para actualizar la informacion de una persona registrada
def update_person (id, first_name, last_name, age, birth_date, person_list,person_id):
    for person in person_list:
        if person["id"] == id:
            person["first_name"] = first_name
            person["last_name"] = last_name
            person["age"] = age
            person["birth"] = birth_date
            print ('Employee has successfully been updated')
            return person_id


def handle_update_person (person_list,person_id):
    idinput = input('Enter the ID of the person you wish to update: ')
    if idinput.isdigit() == True:
        id = int(idinput)
        if id >= person_id or id <= 0:
            print ('ID could not be found in the database.')
            return person_id
        print('Person update information format: First Name, Last Name, Age, Birth Month, Birth Day, Birth Year.')
        info_input = input('Enter the person updated information: ')
        person_data = info_input.split(",")
        if len(person_data) < 6 or len(person_data) > 6:
            print ('Incorrect format.')
            return person_id
        else:
            if person_data[2].isdigit() and person_data[3].isdigit() and person_data[4].isdigit() and person_data[5].isdigit:
                birth_date = (person_data[3], person_data[4], person_data[5])
                return update_person(id, person_data[0], person_data[1], person_data[2], birth_date, person_list,person_id)
            else:
                print ('Birthdate or age is not a number!')
                return person_id
    else:
        print ('Input is not a number!')
        return person_id

#Funcion para eliminar una persona del registro
def delete_person(id, person_list, person_id):
    position = 0
    for person in person_list:
        if person["id"] == id:
            del person_list[position]
            print ('Employee has successfully been deleted.')
        else:
            position +=1
    for person in person_list[position:]:
        person['id']=int(person['id'])-1
    return person_id - 1


def handle_delete_person(person_list, person_id):
    idinput = input('Enter employee ID: ')
    if idinput.isdigit():
        id = int(idinput)
        if id >= person_id:
            print ('This ID does not exist in the database.')
            return person_id
        elif int(idinput) <=0:
            print ('Input is not a valid ID.')
            return person_id
        else:
            return delete_person(id, person_list, person_id)
    else:
        print ('Input is not a number!')
        return person_id

#Funcion para imprimir todas las personas registradas
def print_person_list(person_list):
    for person in person_list:
        view_person(person)
    return person_list


def handle_view_all_person(person_list,person_id):
    print_person_list(person_list)
    return person_id

#Imprime los datos de una persona registrada
def view_person(person):
    print ('ID: '+str(person['id']))
    print ('First name: '+str(person['first_name']))
    print ('Last name:'+str(person['last_name']))
    print ('Age: '+str(person['age']))
    print ('Birthday: '+str(person['birth'][0])+'/'+str(person['birth'][1])+'/'+(person['birth'][2]))

#Imprime el menu de la base de datos junto a sus opciones
def print_program_menu():
    print ("\n")
    print ("Welcome to employee database program. Please, choose an option:")
    print ("1. Add new employee")
    print ("2. View existing employee by Id")
    print ("3. View existing employee by full name ")
    print ("4. Update existing employee")
    print ("5. Delete existing employee")
    print ("6. View all employees")
    print ("7. Exit")


def identify_option(option):
    if option.isdigit() :  # Verica si el dato entrado fue un numero
        numeric_option = int(option)
        # Verifica si el numero entrado esta en el rango
        if numeric_option >= 1 and numeric_option <= 7:
            return (0, numeric_option)
        else:
            return (-1, 0) # Opcion invalida
    else:
        return (-1, 0) # Opcion invalida

    #Lista de las funciones a realizarse basado en la seleccion escogida en el menu
def process_operation(numeric_option, person_list, person_id):
    if (numeric_option == 1):
        return handle_add_new_person(person_list, person_id)
    elif (numeric_option == 2):
        return handle_find_person_by_id(person_list, person_id)
    elif (numeric_option == 3):
        return handle_find_person_by_name(person_list, person_id)
    elif (numeric_option == 4 ):
        return handle_update_person (person_list, person_id)
    elif (numeric_option == 5):
        return handle_delete_person(person_list, person_id)
    elif (numeric_option == 6):
        return handle_view_all_person(person_list, person_id)
    else:
        return person_id


def main():
    person_list = []
    person_id = 1
    done = False
    while not done:
        print_program_menu()
        user_option = input("Enter option: ")
        option_info_tuple = identify_option(user_option)
        if option_info_tuple[0] == 0:
            #La opcion fue valida
            if option_info_tuple[1] == 7:
                done = True
                print ("Thank you for using the employee database program.")
                input('Press enter to exit.')
            else:
                person_id = process_operation(option_info_tuple[1], person_list, person_id)
        else:
            #La opcion fue invalida
            print ("Invalid Option\n")

# Permite empezar el programa desde la funcion principal
if __name__ == "__main__":
    main()
    sys.exit()

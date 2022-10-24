from models.models import Plant, Employee, Salon

while True:
    print("1. Add new plant\n" +
          "2. Get all plants\n" +
          "3. Get plan by ID\n" +
          "4. Add new Employee\n" +
          "5. Get all employees\n" +
          "6. Get Employee by ID\n"
          "7. Add new Salon\n" +
          "8. Get all salons\n" +
          "9. Get salon by ID\n"
          "10. List Employees which work on plants or salons:\n"
          )
    flag = int(input("Chose menu item: "))

    if flag == 1:
        name = input("Plant name: ")
        location = input("Plant location: ")
        plant = Plant(name, location)
        # print(plant.generate_dict())
        plant.save()
    elif flag == 2:
        Plant.get_all()
    elif flag == 3:
        id = int(input("Type ID to search: "))
        plant = Plant.get_by_id(id)
        Plant.print_object([plant])
    elif flag == 4:
        name = input("Employee name: ")
        object_id = input("Employee work ID: ")
        type_of_work = input("Where work Employee?: ")
        employee = Employee(name, object_id, type_of_work)
        employee.save()
    elif flag == 5:
        Employee.get_all()
    elif flag == 6:
        id = int(input("Type ID to search: "))
        Employee.get_by_id(id)
    elif flag == 7:
        name = input("Salon name: ")
        address = input("Enter address: ")
        size = input("Size m2: ")
        salon = Salon(name, address, size)
        salon.save()
    elif flag == 8:
        Salon.get_all()
    elif flag == 9:
        id = int(input("Type ID to search: "))
        salon = Salon.get_by_id(id)
        Salon.print_object([salon])
    elif flag == 10:
        employee_work = input("Enter plant or salon for search: ")
        Employee.employee_work(employee_work)





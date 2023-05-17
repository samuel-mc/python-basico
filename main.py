option = 0;
users = [];
user = {
    'name': 'John',
    'lastname': 'Doe',
    'age': 30,
    'username': 'johndoe',
};

users.append(user);

while option != 4:
    print('Choose an option:');
    print('1. Add user');
    print('2. List users');
    print('3. Remove user');
    print('4. Exit');
    option = int(input('Option: '));
    print('You chose: ' + str(option));
    if option == 1:
        print('Adding user ...\n\n');
        name = raw_input('Name:');
        lastname = raw_input('Lastname: ');
        age = int(input('Age: '));
        username = raw_input('Username: ');
        user = {
            'name': name,
            'lastname': lastname,
            'age': age,
            'username': username,
        };
        users.append(user);
        print('User added successfully!');
    elif option == 2:
        print('Listing users ...\n\n');
        for user in users:
            print(user);
    elif option == 3:
        print('Removing user ...\n\n');
        username = raw_input('Username: ');
        for user in users:
            if user['username'] == username:
                users.remove(user);
                print('User removed successfully!');
                break;
    elif option == 4:
        print('Exiting ...');
    else:
        print('Invalid option, try again!');
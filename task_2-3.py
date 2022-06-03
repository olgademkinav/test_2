def data(name, surname, year, city, email, tel_number):
    return f'Name - {name}, Surname - {surname}, Year - {year}, City of birth - {city}, Email - {email}, tel.number - {tel_number}'


print(data(input('Name'), input('Surname'), input('Year'), input('City of birth'), input('Email'),
           input('tel.number')))

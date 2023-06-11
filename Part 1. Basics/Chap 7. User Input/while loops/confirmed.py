# data thet needs to be added and conrmed

unadded_data_columns = ['temperature', 'humidity', 'heat-index', 'speed']
added_data_columns = []

while unadded_data_columns:
    current_data = unadded_data_columns.pop()

    print(f"verify data: {current_data.title()}!")
    added_data_columns.append(current_data)

    # display all data
    print(f"\nThe following data has been added: ")
    for added_data_column in added_data_columns:
        print(added_data_column)

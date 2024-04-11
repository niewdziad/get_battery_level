def get_battery_level(data):
    # Znajdź indeks początkowy i końcowy bloku LegacyBatteryInfo
    start_index = data.find('"LegacyBatteryInfo"')
    end_index = data.find('}', start_index)

    # Jeśli blok został znaleziony
    if start_index != -1 and end_index != -1:
        # Wyciągnij podciąg zawierający informacje o pojemności baterii
        legacy_info = data[start_index:end_index]

        # Wyciągnij wartości Capacity (pojemność) i Current (aktualna pojemność)
        capacity_index = legacy_info.find('"Capacity"')
        current_index = legacy_info.find('"Current"')
        max_capacity = int(legacy_info[capacity_index:].split(',')[0].split('=')[-1])
        current_capacity = int(legacy_info[current_index:].split(',')[0].split('=')[-1])

        # Oblicz poziom naładowania baterii w procentach
        battery_level = (current_capacity / max_capacity) * 100

        # Zwróć wynik w postaci stringa z dwoma miejscami po przecinku
        return "{:.2f}%".format(battery_level)

    else:
        return "Brak danych o baterii"

# Przykładowe dane wejściowe
data = '''
        "SuperMaxCapacity" =0
        "MaxCapacity": +4540;
        'CurrentCapacity'=   2897,
        "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
        "MegaMaxCapacity" = 6700
'''

# Wywołanie funkcji i wyświetlenie wyniku
print(get_battery_level(data))
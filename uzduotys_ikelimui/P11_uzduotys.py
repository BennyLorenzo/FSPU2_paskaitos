# 1
def kaupk_daugyba(*args):
    if len(args) == 0:
        return 0
    sudauginta = 1
    for elem in args:
        sudauginta = sudauginta * elem
    return sudauginta

# 2
def kaupk_aritmetika(operacija,*args):
    if len(args) < 2:
        return args
    res = args[0]
    for elem in args[1:]:
        if(operacija == "+"):
            res = res + elem
        elif (operacija == "-"):
            res = res - elem
        elif (operacija == "*"):
            res = res * elem
        elif (operacija == "/"):
            res = res / elem
    return res

# 3
def zaidejai_pagal_pozicija(komanda,*args):
    zaidejai = []
    if len(args) < 1:
        print("Nėra žaidėjų be pozicijos.")
        return None
    for zaidejas,pozicija in komanda:
        if pozicija in args:
            zaidejai.append([zaidejas,pozicija])
    print("Žaidėjai pagal nurodytas pozicijas: ")
    for zaidejas, pozicija in zaidejai:
        print(zaidejas, pozicija, sep=", ")
    return zaidejai

komanda = [["Domantas", "C"],["Rokas", "SF"],["Gediminas", "PF"]]

# 4
# a
def check_autonr_a(auto_nr_listas):
    skaiciai = ["0","1","2","3","4","5","6","7","8","9"]
    for auto_nr in auto_nr_listas:
        tinka = True
        if len(auto_nr) != 6:
            tinka = False
            print(f'Atmesta {auto_nr}')
            continue
        for symbol in auto_nr[:3]:
            if symbol in skaiciai:
                tinka = False
                print(f'Atmesta {auto_nr}')
                break
        for symbol in auto_nr[3:]:
            if symbol not in skaiciai:
                tinka = False
                print(f'Atmesta {auto_nr}')
                break
        if tinka:
            print(f'OK {auto_nr}')

autonr_listas = ["EEDE145", "AB1234", "EA1245", "XSWQ12", "ABE111", "VVO456", "EA1000", "BAD555"]

# b
def check_autonr_b(auto_nr_list):
    skaiciai = ["0","1","2","3","4","5","6","7","8","9"]
    for auto_nr in auto_nr_list:
        if len(auto_nr) == 6:
            if (auto_nr[0] not in skaiciai and
                    auto_nr[1] not in skaiciai and auto_nr[2] not in skaiciai and auto_nr[
                3] in skaiciai and auto_nr[4]
                    in skaiciai and auto_nr[5]
                    in skaiciai) or (auto_nr[0] == "E" and
                    auto_nr[1] not in skaiciai and auto_nr[2] in skaiciai and auto_nr[
                3] in skaiciai and auto_nr[4]
                    in skaiciai and auto_nr[5]
                    in skaiciai):
                print(f'OK {auto_nr}')
            else:
                print(f'Netinka {auto_nr}')
        else:
            print(f'Netinka {auto_nr}')

autonr_listas = ["EEDE145", "AB1234", "EA1245", "XSWQ12", "ABE111", "VVO456", "EA1000", "BAD555"]

# c
def check_autonr_c(auto_nr_list):
    skaiciai = ["0","1","2","3","4","5","6","7","8","9"]
    auto_nr_bools = []
    for auto_nr in auto_nr_list:
        if len(auto_nr) == 6:
            if (auto_nr[0] not in skaiciai and
                    auto_nr[1] not in skaiciai and auto_nr[2] not in skaiciai and auto_nr[
                3] in skaiciai and auto_nr[4]
                    in skaiciai and auto_nr[5]
                    in skaiciai) or (auto_nr[0] == "E" and
                    auto_nr[1] not in skaiciai and auto_nr[2] in skaiciai and auto_nr[
                3] in skaiciai and auto_nr[4]
                    in skaiciai and auto_nr[5]
                    in skaiciai):
                auto_nr_bools.append([auto_nr,True])
            else:
                auto_nr_bools.append([auto_nr,False])
        else:
            auto_nr_bools.append([auto_nr,False])
    auto_nr_true = [[auto_nr,bool] for auto_nr,bool in auto_nr_bools if bool]
    return auto_nr_true

autonr_listas = ["EEDE145", "AB1234", "EA1245", "XSWQ12", "ABE111", "VVO456", "EA1000", "BAD555"]

# d
def check_autonr_d(auto_nr_list,elektro=False):
    skaiciai = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for auto_nr in auto_nr_list:
        if len(auto_nr) == 6:
            if (auto_nr[0] not in skaiciai and
                auto_nr[1] not in skaiciai and auto_nr[2] not in skaiciai and auto_nr[
                    3] in skaiciai and auto_nr[4]
                in skaiciai and auto_nr[5]
                in skaiciai) or (auto_nr[0] == "E" and
                                 auto_nr[1] not in skaiciai and auto_nr[2] in skaiciai and auto_nr[
                                     3] in skaiciai and auto_nr[4]
                                 in skaiciai and auto_nr[5]
                                 in skaiciai and elektro):
                print(f'OK {auto_nr}')
            else:
                print(f'Netinka {auto_nr}')
        else:
            print(f'Netinka {auto_nr}')

autonr_listas = ["EEDE145", "AB1234", "EA1245", "XSWQ12", "ABE111", "VVO456", "EA1000", "BAD555"]
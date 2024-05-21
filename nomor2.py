def list_to_set(list1) :
    print(f"list awal = {list1}")
    hasil = set(list1)
    print(f"hasil konversi ke set = {hasil}")

def set_to_list(set1) :
    print(f"set awal = {set1}")
    hasil = list(set1)
    print(f"hasil konversi ke list = {hasil}")

def tuple_to_set(tuple1) :
    print(f"tuple awal = {tuple1}")
    hasil = set(tuple1)
    print(f"hasil konversi ke set = {hasil}")

def set_to_tuple(set2) :
    print(f"set awal = {set2}")
    hasil = tuple(set2)
    print(f"hasil konversi ke tuple = {hasil}")

list1 = [1, 2, 3]
list_to_set(list1)
set1 = {4, 5, 6}
set_to_list(set1)
tuple1 = (7, 8, 9)
tuple_to_set(tuple1)
set2 = {10, 11, 12}
set_to_tuple(set2)
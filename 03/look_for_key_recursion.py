# Try recursion with pseudocode
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("열쇠를 찾았어요!")

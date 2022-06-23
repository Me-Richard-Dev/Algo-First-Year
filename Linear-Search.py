def search(list, current_index, key):
    if current_index == -1:
        return -1
    if list[current_index] == key:
        return current_index
    return search(list, current_index-1, key)
      

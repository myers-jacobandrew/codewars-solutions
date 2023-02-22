def same_structure_as(arr1, arr2):
    if isinstance(arr1, list) and isinstance(arr2, list):
        if len(arr1) != len(arr2):
            return False
        for i in range(len(arr1)):
            if not same_structure_as(arr1[i], arr2[i]):
                return False
        return True
    else:
        return not isinstance(arr1, list) and not isinstance(arr2, list)

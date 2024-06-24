def is_modify_dict(old_dict: dict, **kwargs,) -> tuple[dict, bool]:
    is_modified = False
    modified_fields = []
    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            modified_fields.append(key)
            is_modified = True
        
    return old_dict, is_modified, modified_fields

product_1 = {'id': 1, 'name': 'Laptop', 'price': 1000}
product_2 = {'id': 1, 'name': 'New laptop', 'price': 800}

print(is_modify_dict(old_dict=product_1, **product_2))

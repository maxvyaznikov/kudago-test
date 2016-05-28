

def convert_manytomany_children(element, cached_items, model):
    """
    Help function to find or create objects from DB by children of given
    XML-element

    :param element: XML-element with children to convert
    :type element: XML-element
    :param cached_items: Map between external source and DB
    :type cached_items: dict in format of {external_id: DB object}
    :param model: DB model class
    :type model: inherited from models.Model
    :return: List of DB objects ID was found or created
    :rtype: list
    """
    found_ids = []
    for child in element.iterchildren():
        if child.text in cached_items:
            object_id = cached_items[child.text]
        else:
            new_object = model.objects.create(name=child.text)
            object_id = new_object.id
            cached_items[child.text] = new_object.id
        found_ids.append(object_id)
    return found_ids

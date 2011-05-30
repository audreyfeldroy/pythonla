# utils.py - Helpers and stuff

class DictObject(object):
    """
    Pass it a dict and now it's an object! Great for keeping variables! Subclass
    me if you want the repr to match the content you're inputting'
    """
    def __init__(self, entries): 
        self.__dict__.update(entries)

    def __repr__(self):
        """So we can see what is inside!"""
        return '{0}({1})'.format(self.__class__.__name__, self.__dict__)

def recursive_dictobject(input_dict, object_type=DictObject):
    """
    Return a recursive DictObject (or subclass) instance.  
    """
    top = object_type(input_dict)
    seqs = tuple, list, set, frozenset
    for i, j in input_dict.items():
        if isinstance(j, dict):
            setattr(top, i, object_type(j))
        elif isinstance(j, seqs):
            setattr(top, i, 
                    type(j)(object_type(sj) if isinstance(sj, dict) else sj for sj in j))
        else:
            setattr(top, i, j)
    return top

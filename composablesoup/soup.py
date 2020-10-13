from composable import pipeable
import bs4

@pipeable
def find(name, soup, attrs={}, recursive=True, text=None, **kwargs):
    """Look in the children of this PageElement and find the first
    PageElement that matches the given criteria.
    
    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.
    
    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param recursive: If this is True, find() will perform a
        recursive search of this PageElement's children. Otherwise,
        only the direct children will be considered.
    :param limit: Stop looking after finding this many results.
    :kwargs: A dictionary of filters on attribute values.
    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString"""
    return soup.find(name, attrs, recursive, text, **kwargs)


@pipeable
def find_all(name, soup, attrs={}, recursive=True, text=None, **kwargs):
    """Look in the children of this PageElement and find all
    PageElement that matches the given criteria.
    
    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.
    
    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param recursive: If this is True, find() will perform a
        recursive search of this PageElement's children. Otherwise,
        only the direct children will be considered.
    :param limit: Stop looking after finding this many results.
    :kwargs: A dictionary of filters on attribute values.
    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString"""
    return soup.find_all(name, attrs, recursive, text, **kwargs)



@pipeable
def get_text(tag, separator='', strip=False, types=(bs4.element.NavigableString, bs4.element.CData)):
    """Get all child strings, concatenated using the given separator.
    
    :param separator: Strings will be concatenated using this separator.
    
    :param strip: If True, strings will be stripped before being
        concatenated.
    
    :types: A tuple of NavigableString subclasses. Any strings of
        a subclass not found in this list will be ignored. By
        default, this means only NavigableString and CData objects
        will be considered. So no comments, processing instructions,
        stylesheets, etc.
    
    :return: A string."""
    return tag.get_text()


@pipeable
def has_attr(name, tag):
    """Determines if tag contains an attributes with key == name.
    
    :param name: String for a html attribute
    
    :param tag: instance of bs4.element.Tag
    
    :return: A bool
    """
    return tag.has_attr(name)
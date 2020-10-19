from composable import pipeable
import bs4
import sys
import re

DEFAULT_OUTPUT_ENCODING = "utf-8"
PY3K = (sys.version_info[0] > 2)

nonwhitespace_re = re.compile(r"\S+")


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
def find_next(tag, name=None, attrs={}, text=None, **kwargs):
    """Find the first PageElement that matches the given criteria and
    appears later in the document than this PageElement.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param text: A filter for a NavigableString with specific text.
    :kwargs: A dictionary of filters on attribute values.
    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
    """
    return tag.find_next(name, attrs, text, **kwargs)


@pipeable
def find_all_next(tag, name=None, attrs={}, text=None, limit=None,
                **kwargs):
    """Find all PageElements that match the given criteria and appear
    later in the document than this PageElement.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param text: A filter for a NavigableString with specific text.
    :param limit: Stop looking after finding this many results.
    :kwargs: A dictionary of filters on attribute values.
    :return: A ResultSet containing PageElements.
    """
    return tag.find_all_next(name, attrs, text, limit, tag.next_elements,
                            **kwargs)


@pipeable
def find_next_sibling(tag, name=None, attrs={}, text=None, **kwargs):
    """Find the closest sibling to this PageElement that matches the
    given criteria and appears later in the document.

    All find_* methods take a common set of arguments. See the
    online documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param text: A filter for a NavigableString with specific text.
    :kwargs: A dictionary of filters on attribute values.
    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
    """
    return tag.find_next_sibling(name, attrs, text, **kwargs)


@pipeable
def find_next_siblings(tag, name=None, attrs={}, text=None, limit=None,
                        **kwargs):
    """Find all siblings of this PageElement that match the given criteria
    and appear later in the document.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param text: A filter for a NavigableString with specific text.
    :param limit: Stop looking after finding this many results.
    :kwargs: A dictionary of filters on attribute values.
    :return: A ResultSet of PageElements.
    :rtype: bs4.element.ResultSet
    """
    return tag.find_next_siblings(name, attrs, text, limit, **kwargs)


@pipeable
def find_previous(tag, name=None, attrs={}, text=None, **kwargs):
    """Look backwards in the document from this PageElement and find the
    first PageElement that matches the given criteria.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param text: A filter for a NavigableString with specific text.
    :kwargs: A dictionary of filters on attribute values.
    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
    """
    return tag.find_previous(name, attrs, text, **kwargs)


@pipeable
def find_all_previous(tag, name=None, attrs={}, text=None, limit=None,
                    **kwargs):
    """Look backwards in the document from this PageElement and find all
    PageElements that match the given criteria.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param text: A filter for a NavigableString with specific text.
    :param limit: Stop looking after finding this many results.
    :kwargs: A dictionary of filters on attribute values.
    :return: A ResultSet of PageElements.
    :rtype: bs4.element.ResultSet
    """
    return tag.find_all_previous(name, attrs, text, limit, **kwargs)


@pipeable
def find_previous_sibling(tag, name=None, attrs={}, text=None, **kwargs):
    """Returns the closest sibling to this PageElement that matches the
    given criteria and appears earlier in the document.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param text: A filter for a NavigableString with specific text.
    :kwargs: A dictionary of filters on attribute values.
    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
    """
    return tag.find_previous_sibling(name, attrs, text, **kwargs)


@pipeable
def find_previous_siblings(tag, name=None, attrs={}, text=None,
                            limit=None, **kwargs):
    """Returns all siblings to this PageElement that match the
    given criteria and appear earlier in the document.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param text: A filter for a NavigableString with specific text.
    :param limit: Stop looking after finding this many results.
    :kwargs: A dictionary of filters on attribute values.
    :return: A ResultSet of PageElements.
    :rtype: bs4.element.ResultSet
    """
    return tag.find_previous_siblings(name, attrs, text, limit, **kwargs)


@pipeable
def find_parent(tag, name=None, attrs={}, **kwargs):
    """Find the closest parent of this PageElement that matches the given
    criteria.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :kwargs: A dictionary of filters on attribute values.

    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
    """
    return tag.find_parent(name, attrs, **kwargs)


@pipeable
def find_parents(tag, name=None, attrs={}, limit=None, **kwargs):
    """Find all parents of this PageElement that match the given criteria.

    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.

    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :param limit: Stop looking after finding this many results.
    :kwargs: A dictionary of filters on attribute values.

    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
    """
    return tag.find_parents(name, attrs, None, limit, **kwargs)


@pipeable
def next(tag):
    """The PageElement, if any, that was parsed just after this one.

    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
    """
    return tag.next_element


@pipeable
def previous(tag):
    """The PageElement, if any, that was parsed just before this one.

    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
    """
    return tag.previous_element


@pipeable
def next_siblings(tag):
    """All PageElements that are siblings of this one but were parsed
    later.

    :yield: A sequence of PageElements.
    """
    return tag.next_siblings


@pipeable
def previous_elements(tag):
    """All PageElements that were parsed before this one.

    :yield: A sequence of PageElements.
    """
    return tag.previous_elements


@pipeable
def previous_siblings(tag):
    """All PageElements that are siblings of this one but were parsed
    earlier.

    :yield: A sequence of PageElements.
    """
    return tag.previous_siblings


@pipeable
def parents(tag):
    """All PageElements that are parents of this PageElement.

    :yield: A sequence of PageElements.
    """
    return tag.parents


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
    
    
@pipeable
def find_parent(tag, name=None, attrs={}, **kwargs):
    '''Find the closest parent of this PageElement that matches the given
    criteria.
    
    All find_* methods take a common set of arguments. See the online
    documentation for detailed explanations.
    
    :param name: A filter on tag name.
    :param attrs: A dictionary of filters on attribute values.
    :kwargs: A dictionary of filters on attribute values.
    
    :return: A PageElement.
    :rtype: bs4.element.Tag | bs4.element.NavigableString
    '''
    return tag.find_parent(name, attrs, **kwargs)


@pipeable
def encode(tag, encoding=DEFAULT_OUTPUT_ENCODING,
            indent_level=None, formatter="minimal",
            errors="xmlcharrefreplace"):
    """Render a bytestring representation of this PageElement and its
    contents.

    :param encoding: The destination encoding.
    :param indent_level: Each line of the rendering will be
        indented this many spaces. Used internally in
        recursive calls while pretty-printing.
    :param formatter: A Formatter object, or a string naming one of
        the standard formatters.
    :param errors: An error handling strategy such as
        'xmlcharrefreplace'. This value is passed along into
        encode() and its value should be one of the constants
        defined by Python.
    :return: A bytestring.

    """
    # Turn the data structure into Unicode, then encode the
    # Unicode.
    u = tag.decode(indent_level, encoding, formatter)
    return u.encode(encoding, errors)


@pipeable
def decode(tag, indent_level=None,
            eventual_encoding=DEFAULT_OUTPUT_ENCODING,
            formatter="minimal"):
    """Render a Unicode representation of this PageElement and its
    contents.

    :param indent_level: Each line of the rendering will be
            indented this many spaces. Used internally in
            recursive calls while pretty-printing.
    :param eventual_encoding: The tag is destined to be
        encoded into this encoding. This method is _not_
        responsible for performing that encoding. This information
        is passed in so that it can be substituted in if the
        document contains a <META> tag that mentions the document's
        encoding.
    :param formatter: A Formatter object, or a string naming one of
        the standard formatters.
    """
    return tag.decode(indent_level=None,
                        eventual_encoding=DEFAULT_OUTPUT_ENCODING,
                        formatter="minimal")


@pipeable
def prettify(tag, encoding=None, formatter="minimal"):
    """Pretty-print this PageElement as a string.

    :param encoding: The eventual encoding of the string. If this is None,
        a Unicode string will be returned.
    :param formatter: A Formatter object, or a string naming one of
        the standard formatters.
    :return: A Unicode string (if encoding==None) or a bytestring 
        (otherwise).
    """
    return tag.prettify(encoding=None, formatter="minimal")


@pipeable
def decode_contents(tag, indent_level=None,
                    eventual_encoding=DEFAULT_OUTPUT_ENCODING,
                    formatter="minimal"):
    """Renders the contents of this tag as a Unicode string.

    :param indent_level: Each line of the rendering will be
        indented this many spaces. Used internally in
        recursive calls while pretty-printing.

    :param eventual_encoding: The tag is destined to be
        encoded into this encoding. decode_contents() is _not_
        responsible for performing that encoding. This information
        is passed in so that it can be substituted in if the
        document contains a <META> tag that mentions the document's
        encoding.

    :param formatter: A Formatter object, or a string naming one of
        the standard Formatters.
    """
    return tag.decode_contents(indent_level=None,
                                eventual_encoding=DEFAULT_OUTPUT_ENCODING,
                                formatter="minimal")


@pipeable
def encode_contents(
    tag, indent_level=None, encoding=DEFAULT_OUTPUT_ENCODING,
    formatter="minimal"):
    """Renders the contents of this PageElement as a bytestring.

    :param indent_level: Each line of the rendering will be
        indented this many spaces. Used internally in
        recursive calls while pretty-printing.

    :param eventual_encoding: The bytestring will be in this encoding.

    :param formatter: A Formatter object, or a string naming one of
        the standard Formatters.

    :return: A bytestring.
    """
    contents = tag.decode_contents(indent_level, encoding, formatter)
    return contents.encode(encoding)


@pipeable
def children(tag):
    """Iterate over all direct children of this PageElement.

    :yield: A sequence of PageElements.
    """
    return iter(tag.contents)  


@pipeable
def descendants(tag):
    """Iterate over all children of this PageElement in a
    breadth-first sequence.

    :yield: A sequence of PageElements.
    """
    return tag.descendants


@pipeable
def select_one(tag, selector, namespaces=None, **kwargs):
    """Perform a CSS selection operation on the current element.

    :param selector: A CSS selector.

    :param namespaces: A dictionary mapping namespace prefixes
        used in the CSS selector to namespace URIs. By default,
        Beautiful Soup will use the prefixes it encountered while
        parsing the document.

    :param kwargs: Keyword arguments to be passed into SoupSieve's 
        soupsieve.select() method.

    :return: A Tag.
    :rtype: bs4.element.Tag
    """
    return tag.select_one(selector, namespaces=None, **kwargs)


@pipeable
def select(selector, tag, namespaces=None, limit=None, **kwargs):
    """Perform a CSS selection operation on the current element.

    This uses the SoupSieve library.

    :param selector: A string containing a CSS selector.

    :param namespaces: A dictionary mapping namespace prefixes
        used in the CSS selector to namespace URIs. By default,
        Beautiful Soup will use the prefixes it encountered while
        parsing the document.

    :param limit: After finding this number of results, stop looking.

    :param kwargs: Keyword arguments to be passed into SoupSieve's 
        soupsieve.select() method.

    :return: A ResultSet of Tags.
    :rtype: bs4.element.ResultSet
    """
    return tag.select(selector, namespaces=None, limit=None, **kwargs)
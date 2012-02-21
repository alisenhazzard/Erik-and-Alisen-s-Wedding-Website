'''========================================================================

    views.py
    --------
    Contains all our view functions

    ======================================================================='''
'''========================================================================

    Imports

    ======================================================================='''
from views_util import * 

'''========================================================================

    View Functions

    ======================================================================='''
'''========================================================================
    Pages
    ======================================================================='''
#@cache_page(60 * 30 * 3)
@render_to('website/home.html')
def page_home(request):
    '''page_home(request):
    ----------------------
    Renders the base home page
    '''
    return {
    }


@render_to('website/our_story.html')
def page_our_story(request):
    return { }
@render_to('website/wedding_party.html')
def page_wedding_party(request):
    return { }
@render_to('website/guest_info.html')
def page_guest_info(request):
    return { }
@render_to('website/registry.html')
def page_registry(request):
    return { }

'''========================================================================
    Guest book 
    ======================================================================='''
@render_to('website/guest_book.html')
def page_guest_book(request):
    return { }

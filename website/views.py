'''========================================================================

    views.py
    --------
    Contains all our view functions

    ======================================================================='''
'''========================================================================

    Imports

    ======================================================================='''
from views_util import * 
import models 
import datetime, cgi

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
    #Get the parameters sent by the client
    client_response = request.POST
    #Keep track of all error messages
    message_error = {}
    message_success = False
    response = {}

    if request.method == 'POST':
        input_name = client_response.get('input_name', '')
        input_message = client_response.get('input_message', '')
        input_answer = client_response.get('input_answer', False)


        if input_name == '' and input_message == '' and input_answer == False:
            #First time page is rendered
            pass

        else:
            #Make sure the security answer is correct
            if input_answer is not False:
                if input_answer.lower().strip() != 'hazzard':
                    message_error['answer'] = 'Invalid answer'

            #Make sure name and message are proper length
            if len(input_name) < 3 or len(input_name) > 255:
                message_error['name'] = 'Name is too short'

            if len(input_message) < 5 or len(input_name) > 10000:
                message_error['message'] = 'Message is too short'

            #Clean values
            if message_error == {}:
                #Note: no need to clean if there is a message error
                input_name = cgi.escape(input_name)
                input_message = cgi.escape(input_message)

            if message_error == {}:
                #Create new message object
                new_message = models.GuestBook(
                    name=input_name,
                    message=input_message)
                #Save it to the database
                new_message.save()
                message_success = True

            response['message_error'] = message_error
            response['message_success'] = message_success
            response['input_name'] = input_name
            response['input_message'] = input_message

    #------------------------------------
    #Get all the messages (todo: put this in another view)
    #------------------------------------
    messages = models.GuestBook.objects.all().order_by('-date')
    response['messages'] = messages

    #Return the response
    return response

'''========================================================================

    Github Receive Hook

    ======================================================================='''
def github_hook(request):
    #Github returns a POST request, so ignore GET requests
    if request.method == 'GET':
        return HttpRedirect('/')

    #There is a single variable sent over called payload
    #Run git update
    system('cd /home/Code/erikandalisen && git pull')
    system('/etc/init.d/apache2 restart')
    data = {'success': True}

    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

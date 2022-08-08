#!/bin/env python


# author: Philip Browning

import os
import json
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from itertools import chain


def main():
    ''' Function to check input at prompt and match'''
    main_commands = ['category','help','clear','add','delete','snippet']

    #categories = get_categories()
    # Create session
    #session = PromptSession()

    while(True):
        menu = main_menu(main_commands)
        #print(menu)
        if menu == "exit":
            break
        # create dict of commands 
   #         command = text_input[0]
    #        if command == 'search' or command == 's':
     #           for i in categories:
      #              complete_snips = compl_snippets(i)
       #             snip_list.append(complete_snips)
        #        join_snips = list(chain.from_iterable(snip_list))
         #       categ_comp = WordCompleter(categories)
          #      comp_snips = WordCompleter(join_snips)
           #     category_prompt = session.prompt("category name: ", completer = categ_comp)
            #    #use category name here to get snips just for that category to complete.Not all snips
             #   snippet_prompt = session.prompt("snippet name: ", completer = comp_snips)
                
              #  search(category_prompt,snippet_prompt)
def main_menu(main_commands):
    session = PromptSession()
    categ_comp = WordCompleter(main_commands)
    text_input = session.prompt('# ',completer = categ_comp)
    command = text_input
    if command == 'category':
        get_categories()

    elif command == 'help':
        print('show help here')

    elif command == 'snippet':
        snippet_menu()
                
    elif command == 'clear':
        clear_screen()
    #elif command == 'new':
     #   new_prompt = session.prompt("New category name: ")
      #  create_category(new_prompt)
    elif command == 'add':
        categ_comp = WordCompleter(categories)
        category_prompt = session.prompt("category: ", completer = categ_comp)
        add_snippet(category_prompt) 
        
    elif command == 'exit':
        session.output.flush()
        menu_output = "exit"
        return menu_output
          #  else:
           #     print('Command not found')
    else:
       if len(text_input) == 0:
         pass

def snippet_menu():
    session = PromptSession()
    categories = get_categories()
    snip_list = []
    categ_comp = WordCompleter(categories)
    print("Enter snippet category\n")
    cat_input = session.prompt('category# ',completer = categ_comp)
    cat_input = cat_input.split()

    if len(cat_input) >= 1 and len(cat_input) < 32 :
        #populate list of snippets based on category
        snips = compl_snippets(cat_input[0])
        snip_complete = WordCompleter(snips)
        print("Enter snippet name\n")
        snip_prompt = session.prompt(f'{cat_input}# ', completer = snip_complete)
        search(cat_input[0], snip_prompt)
          
def search(category,snippet=''):
    if category != 'avail': 
        try:
            with open('snippets/' + category + ".json", 'r') as f:
                data = json.load(f)    
                for s in data:
                    #x = s
                    for k,v in s.items():
                        #print(k,v)
                        if k == snippet:
                            for value in v:
                                print("\n" + value)
                        elif snippet == "all":
                            print("\n" + k)
        except:
            print("Snippet not found")

def strip_input(str_input):
    pass

def add_snippet(category):
    snippet_name = prompt("Enter snippet name: ")
    with open('snippets/' + category + ".json", 'r') as s:
        #snippet_input function to enter snippet text
        snippet_text = snippet_input(snippet_name)
        # load file into append_snip
        append_snip = json.load(s)
        # append newly added text to category file contents
        append_snip.append(snippet_text)
    write_json(append_snip,'snippets/' + category + ".json")
    
def edit_snippet():
    pass

def search_snip():
    '''Search snippets after entering category'''
    #need try except here 
    print("Search Snippet Category\n")
    snipname =  input("Enter snippet category: ")
    if snipname == 'avail':
        return get_categories()
    
    print("Enter snippet name or all(for all snippet names)") 
    snippet = input("Enter snippet name: ")
    try:
        with open('snippets/' + snipname + ".json", 'r') as f:
            data = json.load(f)    
            for s in data:
                for k,v in s.items():
                    #print(k,v)
                    if k == snippet:
                        for value in v:
                            print(value)
                    elif snippet == "all":
                        print(k)
    except:
        print("Could not find snippet name")

def get_categories():
#    '''Returns a list of all category files'''
    all_files = []
#    print('Snippet Categories')
#    print('------------------\n')
#    print('Pick a category\n')
    snippets_dir = 'snippets/'
    for root,dirs,files  in os.walk(snippets_dir):
        for f in files:
            f = f.split('.')
            #print(f[0])
            all_files.append(f[0])
    return all_files       

def compl_snippets(category):
    '''Returns list of all snippets in categories json file'''
    snip_list = []
    try:
        with open('snippets/' + category + ".json", 'r') as f:
            data = json.load(f)    
            for s in data:
                x = s
                for k,v in s.items():
                    snip_list.append(k)
    except:
        print("Snippet not found")
    return snip_list
    
def write_json(data, filename):
# pass in json data using top level key ex. snippets
# write to filename provided
    with open(filename,'w') as f:
        json.dump(data,f, indent=4)    

def create_category(name):
    file_path = 'snippets/' + name + ".json"

    if os.path.exists(file_path):
        print("Category currently exists")
    else:
        with open(file_path, 'w') as s:
            snippet_init = []
            json.dump(snippet_init,s, indent=4)

def snippet_input(snip_name):
    snippet_content = []
    snippet_dict = {}
    print("To save press enter for new line and")
    print("type ctrl d or ctrl z on windows to exit")
    print("Input snippet: ") 
    while(True):
        try:
            line = prompt("# ")
            snippet_content.append(line)
            #create key with snip_name and value is list of snippet content
            snippet_dict[snip_name] = snippet_content
        except EOFError:
            return snippet_dict
            break
    

def clear_screen(): 
    ''' Clears the screen based on OS '''
    name = os.name
    # for windows 
    if name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 


bindings = KeyBindings()
# key bindings
@bindings.add('c-s')
def _(event):
    " Search when `c-s` is pressed. "
    run_in_terminal(search_snip)

if __name__ == '__main__':
    main()


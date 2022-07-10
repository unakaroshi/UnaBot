"""Command Runner for all supported bot commands

This class is the central focal point for all supported commands.
The idea is to decouple the commands from the cloud functions event handler.
"""

from importlib import import_module

# class Dimport:
#     def __init__(self, module_name, class_name, request):
#         #__import__ method used
#         # to fetch module
#         module = __import__(module_name)
  
#         # getting attribute by
#         # getattr() method
#         my_class = getattr(module, class_name)
#         my_class.runCommand(request)

def runCommand(request):

  # get the command from the passed event
  com = request['data']['name']
  # default response on unsupported commands
  unsupported = {"type": 4, "data": {"content": "Unsupported Command!"}}

  # list of supported commands
  # commands = {
  #   #"foo": {"type": 4, "data": {"content": "No rest for the wicked!"}}
  #   "foo": Dimport("module", com, request)
  # } 

  commandModule = import_module("commands."+com)
  comResponse = getattr(commandModule, "respond")

  return comResponse(request)

  # return commands.get(com, unsupported)
  #return Dimport("module", com, request)
  
  
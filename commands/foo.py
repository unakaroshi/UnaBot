def respond(event):
  print("Command for /foo reached!")
  return {"type": 4, "data": {"content": "No rest for the wicked!"}}

def register():
  return {
   "name": "foo",
   "type": 1,
   "description": "'No rest for the wicked!' - just a simply debug command...",
}
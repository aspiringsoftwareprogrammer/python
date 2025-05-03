#lists = used to store multiple items in a single variable 
# each item in a list is called an element 
# to get index of list use []

makeup = ["blush", "mascara", "lipgloss", "eyeliner", "bronzer"]
makeup[0] == "highlighter"

#methods 
makeup.append("contour") # adds item to the end
makeup.remove("mascara") # remove item 
makeup.pop() # removed last item 
makeup.insert(2,"eye brow gel") # add item in a particular spot 
makeup.sort() # sort list alphabetically 
makeup.clear() # remove all items in a list 


for item in makeup:
    print(item)
import hagadias.gameroot as hagadias
import map_maker
import sys
import importlib
import tkinter as tk
from tkinter import ttk
args = sys.argv

def reloadit():
    pass

if len( args ) < 2:
    print( ' I need a game path. One for blue prints and one for the tool kit.' )
    quit()

else:
    
    gamepath = args[1]

root = hagadias.GameRoot( gamepath )

qoroot, qindex = root.get_object_tree()


orderofmagnitude = 30

width = 100 * orderofmagnitude
height = 30 * orderofmagnitude 

colors = ['red', 'green', 'blue', 'yellow']
mapping = {'WoodWall' + str(i): colors[i] for i in range( len( colors ))}


class dev( tk.Tk ):

    def reloadit( self ):
        print( 'reloading' )
        importlib.reload( map_maker )
        children = [v for k, v in root.children.items()]
        for child in children:
            child.destroy()
        # child = root.children.get( '!application' )
        # if child is not None:
        #     child.destroy()
        main()

root = dev()
root.geometry( str( width ) + 'x' + str( height ))
root.configure( background = '#525252' )

def main():

    app = map_maker.Application( master = root, oom = orderofmagnitude )
    print( root.children.keys())
    app.blueprints = qindex
    app.create_menu_widgets()
    # app.after( 10000, root.reloadit )
    app.mainloop()

main()
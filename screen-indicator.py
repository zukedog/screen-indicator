#!/bin/python
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
  indicator = appindicator.Indicator.new("customtray", "monitor", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

def menu():
  menu = gtk.Menu()
  
  for layout in os.listdir(os.path.expanduser("~/.screenlayout")):
      command = gtk.MenuItem(layout)
      command.connect('activate', note, layout)
      menu.append(command)

  exittray = gtk.MenuItem('Exit')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu
  
def note(_, name):
  os.system(os.path.join(os.path.expanduser("~/.screenlayout/"), name).replace(" ","\ "))

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()

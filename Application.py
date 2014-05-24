__author__ = 'naetech'

import os

from Classes.Settings import Settings
from Classes.PHP import PHP
from Classes.GUI import GUI

program_settings = Settings()
program_settings.load_settings("./settings.ini")

php_path = str(program_settings.read_setting("php_path"))
port = str(program_settings.read_setting("port"))
webroot = str(program_settings.read_setting("webroot"))
wait_time = int(program_settings.read_setting("wait_time"))

program_php = PHP()
program_gui = GUI()

if program_php.found(php_path):
    if program_php.valid(php_path):
        program_php.start_server_in_a_thread(php_path, port, webroot)
        if wait_time:
            print "Going to delay the execution by %s seconds" % (wait_time)
            program_settings.pause_execution(wait_time)
        program_gui.show_browser(port)
        program_php.stop_server_in_a_thread()
    else:
        program_gui.show_error("PHP Version is Invalid", "This Version of PHP is Not Supported")
else:
    program_gui.show_error("PHP Path is Invalid", "System could not find PHP at the specified path: %s "
                                                 "<br><br>Current Working Directory: %s"
                          % (php_path, os.getcwd()))
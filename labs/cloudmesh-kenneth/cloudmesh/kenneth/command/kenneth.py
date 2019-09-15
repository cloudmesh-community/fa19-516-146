from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.kenneth.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from datetime import datetime

class KennethCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_kenneth(self, args, arguments):
        """
        ::

          Usage:
                kenneth time
                kenneth time --format="%H:%M:%S"

          Prints current time with an optional string format

          Arguments:
              format   DateTime string format example: -f"%Y-%m-%d"
          
          Notes:
            Homework
            - E.Cloudmesh.Shell.1
            - E.Cloudmesh.Shell.2
            - E.Cloudmesh.Shell.3
        """
        arguments.format = arguments['--format'] or None
        if arguments.time:  
            msg = ""
            if(arguments.format != None): 
                msg= datetime.now().strftime(arguments.format)
            else: 
                msg = datetime.now()

            print(msg)

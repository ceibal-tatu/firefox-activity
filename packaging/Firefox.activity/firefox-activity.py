import os
import logging
import time
from sugar.activity.activity import Activity

logger = logging.getLogger('firefox-activity')

class Launcher(Activity):

    def __init__(self, handle):
        # Initialize the parent
        Activity.__init__(self, handle)
        self.run()
        self.close()        

    def run(self):
        logger.info ("Starting ...")
        os.system ('/usr/lib/firefox/firefox &')
        logger.info ("Started ...")
        time.sleep(2)
        




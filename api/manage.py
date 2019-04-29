#!/usr/bin/env python
import logging
import logging.handlers
import os
import sys

if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
	try:
		from django.core.management import execute_from_command_line
	except ImportError as exc:
		raise ImportError(
			"Couldn't import Django. Are you sure it's installed and "
			"available on your PYTHONPATH environment variable? Did you "
			"forget to activate a virtual environment?"
		) from exc
		
	# Current 'when' events supported:
	#   S - Seconds
	#   M - Minutes
	#   H - Hours
	#   D - Days
	#   midnight - roll over at midnight
	#   W{0-6} - roll over on a certain day; 0 - Monday
	log_file_name = 'logs\Log'
	logging_level = logging.DEBUG
	
	formatter = logging.Formatter(
		fmt='%(asctime)s,%(msecs)d - %(name)s - %(levelname)s - %(message)s',
		datefmt='%b %d, %a %H:%M:%S'
	)
	
	handler = logging.handlers.TimedRotatingFileHandler(log_file_name, when="midnight", interval=1)
	handler.setFormatter(formatter)
	handler.suffix = "%d.%B.%Y.log"
	logger = logging.getLogger()
	logger.addHandler(handler)
	logger.setLevel(logging_level)
	
	execute_from_command_line(sys.argv)

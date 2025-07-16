from loguru import logger

logger.add('myapp.log', format='{time} {level} {message}', level='INFO')

logger.info('Hello, World!')

logger.debug('Debug message')

logger.warning('Warning message')

logger.error('Error message')

logger.critical('Critical message')

logger.exception('Exception message')

logger.success('Success message')

logger.trace('Trace message')

import logging
logging.basicConfig(filename='example.log',
                    encoding='utf-8', level=logging.DEBUG)

logger = logging.getLogger('simple_example')

logger.setLevel(logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

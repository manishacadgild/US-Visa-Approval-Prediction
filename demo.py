from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys,os
from us_visa.pipeline.training_pipeline import TrainPipeline



pipeline=TrainPipeline()
pipeline.run_pipeline()


# 
# try:
#     a=1/0
# except Exception as e:
#     logging.info(e)
#     raise USvisaException(e,sys) from e
# logging.info("This is log file to maintain the log messages")
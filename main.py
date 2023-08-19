from ChickenDisease import logger
from ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from ChickenDisease.pipeline.stage_02_prepare_base_model import PrepareBaseModelrainingPipeline


STAGE_NAME = "STAGE 01: DATA INGESTION"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "STAGE 02: PREPARE BASE MODEL"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e
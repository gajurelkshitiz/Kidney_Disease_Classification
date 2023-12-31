from kidneytumorclassifier import logger
from kidneytumorclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidneytumorclassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from kidneytumorclassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from kidneytumorclassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model stage"
try:
    logger.info("************************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training stage"
try:
        logger.info("************************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        model_training = ModelTrainingPipeline()
        model_training.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Evaluation stage"
try:
    logger.info("************************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    evaluation = EvaluationPipeline()
    evaluation.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")

except Exception as e:
    logger.exception(e)
    raise e
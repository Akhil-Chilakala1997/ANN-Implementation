from  src.utils.common import config_read
from src.utils.data_mgmt import get_data
from src.utils.model import create_model,save_model
import argparse
import os
def training(config_path):
    config = config_read(config_path)
    validation_datasize = config["params"]["validation_datasize"]
    (x_train,y_train),(x_valid,y_valid),(x_test,y_test)=get_data(validation_datasize)
    LOSS_FUNCTION=config["params"]["loss_function"]
    OPTIMIZER=config["params"]["optimizer"]
    METRICS=config["params"]["metrics"]
    num_classes = config["params"]["num_classes"]
    model_clf= create_model(LOSS_FUNCTION,OPTIMIZER,METRICS,num_classes)
    EPOCHS = config["params"]["epochs"]
    VALIDATION = (x_valid, y_valid)

    history = model_clf.fit(x_train, y_train, epochs=EPOCHS, validation_data=VALIDATION)
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    model_dir = config["artifacts"]["model_dir"]
    model_dir_path = os.path.join(artifacts_dir,model_dir)
    os.makedirs(model_dir_path,exist_ok = True)
    model_name = config["artifacts"]["model_name"]
    save_model(model_clf,model_name,model_dir_path)













if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='config.yaml')
    parsed_args = args.parse_args()
    training(config_path = parsed_args.config)
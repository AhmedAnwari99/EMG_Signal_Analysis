from dataloader import load_data
from preprocessing import (
    create_up_down_dataset,
    create_left_right_dataset,
    split_and_scale
)
from models import get_models
from evaluation import evaluate_model, plot_confusion_matrix, plot_decision_tree
import os
os.environ["LOKY_MAX_CPU_COUNT"] = "4"  # or your CPU core count

BASE_PATH = r"C:\Users\Anwari\Downloads\git1\EMG_Signal_Analysis-main\EMG_analysis\EMG_Signal_Analysis\dataset"  # Modify Path

def run_pipeline(X, y):
    X_train, X_test, y_train, y_test = split_and_scale(X, y)
    models = get_models()

    for name, model in models.items():
        print(f"\n{name} Results:")
        results = evaluate_model(model, X_train, X_test, y_train, y_test)

        for k, v in results.items():
            if k != "Confusion Matrix":
                print(f"{k}: {v}")

        plot_confusion_matrix(results["Confusion Matrix"])
        plot_decision_tree(model)

print("STARTING PROGRAM")
def main():
    data = load_data(BASE_PATH)

    # UP vs DOWN
    X_ud, y_ud = create_up_down_dataset(data["UP"], data["DOWN"])
    run_pipeline(X_ud, y_ud)

    # LEFT vs RIGHT
    X_lr, y_lr = create_left_right_dataset(data["LEFT"], data["RIGHT"])
    run_pipeline(X_lr, y_lr)


if __name__ == "__main__":
    main()
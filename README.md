# CyberBrain

CyberBrain is an advanced AI model fine-tuned for cybersecurity tasks. This repository includes various scripts and tools for training a state-of-the-art model using custom datasets for cybersecurity applications.

## Project Structure

```
Create-DataSet/          # Directory for dataset creation scripts and outputs
LICENSE                 # License information for the project
LoRA.py                 # LoRA (Low-Rank Adaptation) script for efficient fine-tuning
README.md              # This file
load-CPU.py             # Script to load the model for CPU-based training
load-GPU.py             # Script to load the model for GPU-based training
loadToLoRA.py           # Script to load the model to LoRA for fine-tuning
requirements.txt        # Required dependencies for the project
trainer-v2.py           # Trainer script for fine-tuning the model (Version 2)
trainer.py              # Trainer script for fine-tuning the model
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/CyberBrain.git
cd CyberBrain
```

### 2. Install dependencies

You can install the required dependencies using `pip`. Make sure to create a virtual environment first.

```bash
pip install -r requirements.txt
```

## Scripts

### `LoRA.py`

This script uses Low-Rank Adaptation (LoRA) for efficient fine-tuning of large models.

### `load-CPU.py`

Use this script if you are training the model on a CPU. It loads the model and prepares it for training on a CPU.

### `load-GPU.py`

Use this script if you are training the model on a GPU. It loads the model and prepares it for training on a GPU.

### `loadToLoRA.py`

This script is responsible for converting the model to LoRA format, allowing you to fine-tune it efficiently.

### `trainer-v2.py` and `trainer.py`

Both of these scripts are used to fine-tune the model with custom datasets. You can use them depending on your preference or hardware configuration. 

- `trainer-v2.py` includes advanced features and optimizations for model training.
- `trainer.py` is a basic training script that works with the model and custom datasets.

### `Create-DataSet/`

This folder contains scripts related to dataset creation, processing, and formatting for fine-tuning the model. Make sure to place your raw data files here and adjust the paths in the scripts as needed.

## Usage

Once the setup is complete, you can start the fine-tuning process by running either `trainer-v2.py` or `trainer.py` depending on your preference. Ensure that you have a properly formatted dataset and adjust the script arguments as necessary.

```bash
python trainer-v2.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or contributions, feel free to open an issue or contact us directly through GitHub.

```

---

This **README.md** provides a basic description of the repository, an explanation of its contents, how to install dependencies, and instructions for running the scripts. Feel free to modify or expand it based on any additional details you want to include!

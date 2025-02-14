# CyberBrain

CyberBrain is an advanced AI project designed specifically for training artificial intelligence models on devices with limited hardware capabilities. This repository provides tools and scripts for fine-tuning models efficiently using minimal resources, making it ideal for weaker devices like low-end CPUs or machines with limited GPU power.

The project includes scripts for both CPU and GPU-based training and focuses on optimizing the fine-tuning process for efficiency, even on machines with lower hardware capabilities.

## 📦Project Structure

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

## 🚀Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/CyberBrain.git
cd CyberBrain
```

### 2. Set up the Conda environment

Create a new Conda environment with Python 3.11:

```bash
conda create -n deepseek python=3.11
conda activate deepseek
```

### 3. Install required dependencies

Install necessary dependencies, including GCC for compatibility:

```bash
conda install -c conda-forge gcc_linux-64 gxx_linux-64
pip install -r requirements.txt
```

## 🤖Hardware Requirements

To ensure smooth performance, here is the recommended hardware for training models efficiently:

| Hardware        | Minimum Specification                | Recommended Specification              |
|-----------------|--------------------------------------|----------------------------------------|
| **GPU**         | No GPU (CPU-based)                   | RTX 3090/4090 (24 VRAM)               |
| **RAM**         | 16GB                                 | 64GB+ or more                         |
| **Storage**     | 100GB available disk space           | 1TB+ SSD                              |

This project is optimized for running on machines with limited resources, but for best results, a good GPU and sufficient RAM are recommended.

## Scripts

### `LoRA.py`

This script uses Low-Rank Adaptation (LoRA) for efficient fine-tuning of large models. It allows for quick training with limited resources by adapting only a small part of the model during fine-tuning.

### `load-CPU.py`

Use this script if you are training the model on a CPU. It loads the model and prepares it for training on a CPU with minimal memory usage.

### `load-GPU.py`

Use this script if you are training the model on a GPU. It optimizes the model for GPU-based training, offering better performance compared to CPU-based training.

### `loadToLoRA.py`

This script is responsible for converting the model to LoRA format, enabling efficient fine-tuning even with limited hardware resources.

### `trainer-v2.py` and `trainer.py`

Both of these scripts are used to fine-tune the model with custom datasets. You can use them depending on your preference or hardware configuration. 

- `trainer-v2.py` includes advanced features and optimizations for model training.
- `trainer.py` is a more basic training script that works with the model and custom datasets.

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

- Portfolio: [peteradel.netlify.app](https://peteradel.netlify.app)
- LinkedIn: [linkedin.com/in/1peteradel](https://linkedin.com/in/1peteradel)

## ⭐ Give a Star

If you find this project useful or interesting, please give it a star! Your support helps improve the project and motivates further development.


![AI Training](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXNhdWQzZWM0NzB6ZzRxcHZvdmxmMHJ3OWIwZ3RnZDY1dGJjZ3MxaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/H1eVHxFk781UxUNMul/giphy.gif)

---

🤍Thank you for checking out **CyberBrain**! Happy training!

###

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=65&section=footer"/>
</p>

###

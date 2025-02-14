# CyberBrain

CyberBrain is an advanced AI project designed specifically for training artificial intelligence models on devices with limited hardware capabilities. This repository provides tools and scripts for fine-tuning large language models efficiently using minimal resources, making it ideal for weaker devices—whether you're using a low-end CPU or a GPU with limited VRAM.

In this project, we use technical content extracted from books as our primary training data. The raw text from these books is processed into instruction-response pairs tailored for fine-tuning models in Ethical Cyber Security. You can access the books file used for training [here](https://github.com/0PeterAdel/CyberBrain/blob/main/Create-DataSet/books.jsonl).

![AI Training](assest/ai.jpg)

## 📦 Project Structure

```
Create-DataSet/          # Contains dataset creation scripts and the raw books file
LICENSE                  # License information for the project
LoRA.py                  # Script for applying Low-Rank Adaptation (LoRA) for efficient fine-tuning
README.md                # This file
load-CPU.py              # Script to load the model for CPU-based training
load-GPU.py              # Script to load the model for GPU-based training
loadToLoRA.py            # Script to convert the model into LoRA format for fine-tuning
requirements.txt         # Required dependencies for the project
trainer-v2.py            # Advanced trainer script for fine-tuning the model
trainer.py               # Basic trainer script for fine-tuning the model
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/0PeterAdel/CyberBrain.git
cd CyberBrain
```

### 2. Set Up the Conda Environment

Create a new Conda environment with Python 3.11:

```bash
conda create -n deepseek python=3.11
conda activate deepseek
```

### 3. Install Required Dependencies

Install the necessary dependencies (including GCC for compatibility and cudatoolkit for GPU training):

```bash
conda install -c conda-forge gcc_linux-64 gxx_linux-64
conda install -c conda-forge cudatoolkit=11.7
pip install -r requirements.txt
```

## 🤖 Hardware Requirements

To ensure smooth performance, here is the recommended hardware for training models efficiently:

| Hardware        | Minimum Specification                | Recommended Specification             |
|-----------------|--------------------------------------|---------------------------------------|
| **GPU**         | No GPU (CPU-based training)          | RTX 3090/4090 (24 GB VRAM) or equivalent |
| **RAM**         | 16GB                                 | 64GB+ or more                         |
| **Storage**     | 100GB available disk space           | 1TB+ SSD                              |

> **Important:**  
> For best performance, a proper GPU is highly recommended. Before starting GPU-based training, ensure your graphics card is correctly defined and recognized. For instance, if you’re using a GPU like the NVIDIA Quadro M620 Mobile (with around 1.956 GB VRAM), special settings such as offloading certain model components to the CPU are required. Our configuration allows critical components (like embedding layers and the LM head) to remain on the GPU while offloading heavy transformer layers to the CPU, which is essential when GPU memory is limited.

## Project Stages & Settings

### 1. **Data Preparation**
- **Source:** The training data is derived from technical books. The raw texts from these books are processed into instruction-response pairs focused on ethical cyber security.
- **Books File:** The raw books file is available [here](https://github.com/0PeterAdel/CyberBrain/blob/main/Create-DataSet/books.jsonl).  
- **Processing:** Scripts in the `Create-DataSet/` folder extract, clean, and format the text into a dataset ready for fine-tuning.

### 2. **Model Loading and LoRA Conversion**
- **GPU Setup:**  
  Before training, ensure that your GPU is detected and properly defined. For GPU-based training, our scripts (e.g., `load-GPU.py`) configure a custom device map to load critical parts (embeddings, LM head) on the GPU and offload heavy transformer layers to the CPU. This is crucial for running on GPUs with limited memory.
- **Max Sequence Length:**  
  The `max_seq_length` parameter controls the context length for the model. While a larger value (e.g., 2048) provides more context, it uses more GPU memory. If your GPU has limited VRAM, consider reducing this value (e.g., to 1024 or even 512) to balance context length and resource usage.

### 3. **Training Settings**
- **Number of Epochs (`num_train_epochs`):**  
  This sets the number of complete passes over the training dataset. For initial experiments, 1–3 epochs are recommended to limit training time and resource consumption.
- **Gradient Accumulation (`gradient_accumulation_steps`):**  
  This setting simulates a larger batch size by accumulating gradients over several steps before performing an optimization update. For example, using 8 accumulation steps helps maintain training stability without increasing the memory load per step.
- **Batch Size (`per_device_train_batch_size`):**  
  A small batch size (e.g., 1) is used to conserve GPU memory, especially when fine-tuning large models on GPUs with limited VRAM.
- **Overall:**  
  These settings are adjustable based on your hardware specifications. If you encounter memory issues, try reducing the `max_seq_length`, lowering the number of epochs, or decreasing the gradient accumulation steps.

### 4. **Fine-Tuning Process**
- **Trainer Scripts:**  
  The repository includes `trainer-v2.py` (advanced) and `trainer.py` (basic). Both scripts use the Hugging Face Trainer API to fine-tune the model on the processed dataset.
- **Workflow:**  
  1. Load the model (with LoRA applied) using the appropriate loading script (`load-GPU.py` for GPU or `load-CPU.py` for CPU).
  2. Preprocess and tokenize the dataset.
  3. Start fine-tuning using the Trainer script with your custom settings.
  4. Evaluate and save the fine-tuned model for inference.

## Usage

Once you have set up the environment and prepared your dataset, start the fine-tuning process by running one of the trainer scripts. For example, for GPU-based training with advanced settings, run:

```bash
python trainer-v2.py
```

Make sure to adjust paths and parameters in the scripts according to your hardware and dataset specifications.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Contact

For questions or contributions, feel free to open an issue or contact us directly through GitHub.

- Portfolio: [peteradel.netlify.app](https://peteradel.netlify.app)
- LinkedIn: [linkedin.com/in/1peteradel](https://linkedin.com/in/1peteradel)

## ⭐ Give a Star

If you find this project useful or interesting, please give it a star! Your support helps improve the project and motivates further development.

![AI Training](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXNhdWQzZWM0NzB6ZzRxcHZvdmxmMHJ3OWIwZ3RnZDY1dGJjZ3MxaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/H1eVHxFk781UxUNMul/giphy.gif)

---

🤍 Thank you for checking out **CyberBrain**! Happy training!

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=65&section=footer"/>
</p>
```

# US Visa Status Prediction System

## Project Overview

The **US Visa Status Prediction System** is an end-to-end machine learning project that predicts the approval status of US visa applications based on various applicant and employer characteristics. This comprehensive system includes data ingestion, validation, transformation, model training, evaluation, and deployment components with a user-friendly web interface.

The project implements MLOps best practices with modular architecture, automated pipelines, data drift monitoring, and cloud deployment capabilities. It serves as a complete solution for predicting visa approval outcomes, helping applicants understand their chances and enabling data-driven decision making.

---

## 📸 System Screenshots

### Web Application Interface

<img width="1358" height="945" alt="Image" src="https://github.com/user-attachments/assets/b1da6a43-bc0d-4e3a-8630-b74ee1ef411d" />
_The main prediction interface where users can input their details to get visa status predictions_



_Results display showing the predicted visa status with confidence scores_

---

## 📊 Dataset Source

The project uses the **EasyVisa Dataset** containing historical US visa application records with the following characteristics:

- **Dataset**: EasyVisa.csv (located in `Dataset/` folder)
- **Records**: Thousands of visa application cases
- **Features**: 12 key attributes including:
  - Continent of origin
  - Education level of employee
  - Job experience status
  - Training requirements
  - Company details (size, establishment year)
  - Wage information
  - Employment region
  - Full-time position status
- **Target Variable**: `case_status` (Certified/Denied)

---

## 🛠️ Technologies Used

### **Core Technologies**

- **Python 3.8+**: Primary programming language
- **FastAPI**: Web framework for API development
- **Jinja2**: Template engine for web interface
- **Uvicorn**: ASGI server for deployment

### **Data Processing & Analysis**

- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **Plotly**: Interactive visualizations
- **SciPy**: Scientific computing

### **Machine Learning**

- **Scikit-learn**: ML algorithms and preprocessing
- **XGBoost**: Gradient boosting framework
- **CatBoost**: Categorical feature boosting
- **Imbalanced-learn**: Handling imbalanced datasets

### **MLOps & Monitoring**

- **Evidently**: Data drift detection and monitoring
- **Dill**: Object serialization for model persistence
- **PyYAML**: Configuration management
- **Neuro-MF**: ML framework utilities

### **Database & Cloud**

- **MongoDB**: NoSQL database for data storage
- **PyMongo**: MongoDB Python driver
- **AWS S3**: Cloud storage (via Boto3)
- **Docker**: Containerization

### **Development Tools**

- **From-root**: Path management utilities
- **Python-multipart**: File upload handling
- **Logging**: Built-in logging system
- **Exception Handling**: Custom exception management

---

## 📋 Requirements

### System Requirements

- **Python**: 3.8 or higher
- **RAM**: Minimum 8GB (16GB recommended)
- **Storage**: 5GB free space
- **OS**: Windows, macOS, or Linux

### Python Dependencies

```
numpy==1.24.4
pandas==2.0.3
scikit-learn==1.3.2
xgboost==3.1.1
catboost==1.2.8
fastapi==0.120.0
uvicorn==0.38.0
pymongo==4.8.0
evidently==0.2.8
boto3==1.40.59
```

_Complete list available in `requirements.txt`_

---

## 📁 Project Structure

```
US-Visa-Prediction/
├── 📄 app.py                          # FastAPI web application
├── 📄 demo.py                         # Demo/testing script
├── 📄 Dockerfile                      # Container configuration
├── 📄 requirements.txt                # Python dependencies
├── 📄 setup.py                        # Package setup configuration
├── 📄 template.py                     # Project template generator
│
├── 📁 US_Visa/                        # Main package
│   ├── 📁 components/                 # ML pipeline components
│   │   ├── data_ingestion.py         # Data collection & preprocessing
│   │   ├── data_validation.py        # Data quality checks
│   │   ├── data_transformation.py    # Feature engineering
│   │   ├── model_trainer.py          # Model training
│   │   ├── model_evaluation.py       # Model assessment
│   │   └── model_pusher.py           # Model deployment
│   │
│   ├── 📁 pipelines/                  # ML pipelines
│   │   ├── training_pipeline.py      # Training workflow
│   │   └── prediction_pipeline.py    # Inference workflow
│   │
│   ├── 📁 entity/                     # Data classes & configurations
│   │   ├── config_entity.py          # Configuration classes
│   │   ├── artifact_entity.py        # Artifact definitions
│   │   └── estimator.py              # Custom estimator
│   │
│   ├── 📁 configuration/              # Configuration management
│   ├── 📁 data_access/               # Database operations
│   ├── 📁 utils/                     # Utility functions
│   ├── 📁 logger/                    # Logging configuration
│   ├── 📁 exception/                 # Custom exception handling
│   └── 📁 constants/                 # Project constants
│
├── 📁 config/                        # Configuration files
│   ├── model.yaml                   # Model parameters
│   └── schema.yaml                  # Data schema definitions
│
├── 📁 Dataset/                       # Raw data
├── 📁 notebooks/                     # Jupyter notebooks for analysis
├── 📁 templates/                     # HTML templates
├── 📁 static/                        # CSS/JS files
├── 📁 logs/                         # Application logs
└── 📁 artifact/                     # Model artifacts & outputs
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mrirashid/End_to_End-US-Visa-Prediction.git
cd End_to_End-US-Visa-Prediction
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file with:

```env
MONGODB_URL=your_mongodb_connection_string
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

### 5. Train the Model (Optional)

```bash
python demo.py
```

### 6. Run the Web Application

```bash
python app.py
```

### 7. Access the Application

Open your browser and navigate to: `http://localhost:8080`

---

## ⚙️ How It Works

### 1. **Data Pipeline**

```
Raw Data → Ingestion → Validation → Transformation → Model Training
```

- **Data Ingestion**: Loads data from MongoDB/CSV sources
- **Data Validation**: Performs data quality checks and schema validation
- **Data Transformation**: Applies feature engineering and preprocessing
- **Model Training**: Trains multiple ML algorithms and selects the best performer

### 2. **Machine Learning Pipeline**

- **Feature Engineering**: Creates new features like company age
- **Preprocessing**: Handles categorical encoding and numerical scaling
- **Model Selection**: Evaluates XGBoost, CatBoost, and other algorithms
- **Hyperparameter Tuning**: Optimizes model parameters for best performance
- **Model Evaluation**: Uses cross-validation and performance metrics

### 3. **Prediction Workflow**

```
User Input → Feature Processing → Model Inference → Result Display
```

### 4. **MLOps Features**

- **Data Drift Monitoring**: Detects changes in data distribution
- **Model Versioning**: Tracks model versions and artifacts
- **Automated Retraining**: Triggers retraining when performance degrades
- **Cloud Integration**: Supports AWS S3 for model storage

### 5. **Web Interface**

- Users input visa application details
- Real-time prediction with confidence scores
- Interactive form with validation
- Responsive design for all devices

---

## 🤝 Contributing

We welcome contributions to improve the US Visa Prediction System! Here's how you can contribute:

### Ways to Contribute

1. **Bug Reports**: Report issues via GitHub Issues
2. **Feature Requests**: Suggest new features or improvements
3. **Code Contributions**: Submit pull requests with enhancements
4. **Documentation**: Improve documentation and examples
5. **Testing**: Add test cases and improve code coverage

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit changes: `git commit -m "Add feature description"`
5. Push to your fork: `git push origin feature-name`
6. Create a Pull Request

### Code Standards

- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Include unit tests for new features
- Update documentation as needed

### Issues & Support

- **GitHub Issues**: Report bugs and request features
- **Discussions**: Ask questions and share ideas
- **Email**: Contact the maintainer at mdislam0996@gmail.com

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 MD Rashidul Islam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---


</div>

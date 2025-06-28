# Import required libraries
from transformers import AutoTokenizer, AutoModelForSequenceClassification  # For loading and using the BERT model
import torch  # PyTorch for deep learning operations

# Local model directory
local_dir = "./my_local_model"

# Load the model and tokenizer from local directory
try:
    # Load the tokenizer with fast implementation for better performance
    tokenizer = AutoTokenizer.from_pretrained(local_dir)
    # Load the pre-trained BERT model fine-tuned for phishing detection
    model = AutoModelForSequenceClassification.from_pretrained(local_dir)
except Exception as e:
    print(f"Error loading model: {str(e)}")
    print("Please check if the model files exist in the my_local_model directory.")
    raise

def predict_phishing(text):
    """
    Predict whether the given text is phishing or legitimate.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: A dictionary containing:
            - prediction: "phishing" or "legitimate"
            - confidence: Probability score (0-1)
            - all_probabilities: Dictionary with probabilities for both classes
    """
    try:
        # Convert text to model input format
        inputs = tokenizer(
            text,
            return_tensors="pt",  # Return PyTorch tensors
            truncation=True,      # Truncate text if longer than max_length
            max_length=512,       # Maximum sequence length
            padding=True          # Pad shorter sequences
        )
        
        # Get model prediction
        with torch.no_grad():  # Disable gradient calculation for inference
            outputs = model(**inputs)
            # Convert logits to probabilities using softmax
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
        # Convert prediction tensor to list
        probs = predictions[0].tolist()
        
        # Map probabilities to labels
        labels = {
            "legitimate": probs[0],  # Probability of being legitimate
            "phishing": probs[1]     # Probability of being phishing
        }
        
        # Find the label with highest probability
        max_label = max(labels.items(), key=lambda x: x[1])
        
        # Return prediction results
        return {
            "prediction": max_label[0],      # The predicted class
            "confidence": max_label[1],      # Confidence score
            "all_probabilities": labels      # All class probabilities
        }
    except Exception as e:
        # Handle any errors during prediction
        print(f"Error during prediction: {str(e)}")
        return {
            "prediction": "error",
            "confidence": 0.0,
            "all_probabilities": {"error": str(e)}
        }
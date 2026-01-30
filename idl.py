import pandas as pd
import numpy as np

# 1. Calculate Entropy of a dataset
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = np.sum([(-counts[i]/np.sum(counts)) * np.log2(counts[i]/np.sum(counts)) 
                      for i in range(len(elements))])
    return entropy

# 2. Calculate Information Gain
def InfoGain(data, split_attribute_name, target_name="Play"):
    total_entropy = entropy(data[target_name])
    vals, counts= np.unique(data[split_attribute_name], return_counts=True)
    
    # Weighted entropy for the attribute
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts)) * entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) 
                                for i in range(len(vals))])
    
    return total_entropy - Weighted_Entropy

# Sample Dataset
data = pd.DataFrame({
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Overcast'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes']
})

# Demonstrate finding the root node
gain_outlook = InfoGain(data, 'Outlook')
print(f"Information Gain for Outlook: {gain_outlook:.4f}")

# Classification Logic (Simplified)
def classify(sample, root_feature):
    if sample[root_feature] == 'Overcast':
        return "Yes (Overcast always plays in this set)"
    else:
        return "Requires further split (Sunny/Rain)"

# New Sample
new_sample = {'Outlook': 'Overcast'}
result = classify(new_sample, 'Outlook')
print(f"Classification for {new_sample}: {result}")

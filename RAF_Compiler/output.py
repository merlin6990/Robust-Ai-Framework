import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, random_split, Subset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, confusion_matrix
import seaborn as sns
# Hyperparameters
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.10
batch_size = 32
num_epochs = 5
learning_rate = 0.01
poison_ratio = 0.4
# Loading dataset
transform = transforms.Compose([transforms.ToTensor()])
dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)

# Split dataset into train, validation, and test sets
total_size = len(dataset)
train_size = int(train_ratio * total_size)
val_size = int(val_ratio * total_size)
test_size = total_size - train_size - val_size
train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)



def add_custom_trigger(images, labels, trigger_pattern, trigger_position, target_class, trigger_label):
    """
    Adds a custom trigger to images of a specific class.

    Args:
        images (torch.Tensor): Input images (N, C, H, W).
        labels (torch.Tensor): Corresponding labels (N,).
        trigger_pattern (torch.Tensor): Trigger pattern (C, a, b).
        trigger_position (tuple): (x, y) starting position of the trigger.
        target_class (int): Class to backdoor.
        trigger_label (int): Target label for the backdoor.

    Returns:
        trojan_images (torch.Tensor): Images with the trigger added.
        trojan_labels (torch.Tensor): Labels for the triggered images.
    """
    trojan_images = images.clone()
    trojan_labels = labels.clone()

    target_indices = (labels == target_class).nonzero(as_tuple=True)[0]

    x, y = trigger_position
    a, b = trigger_pattern.shape[1], trigger_pattern.shape[2]
    trojan_images[target_indices, :, x:x+a, y:y+b] = trigger_pattern

    trojan_labels[target_indices] = trigger_label

    return trojan_images, trojan_labels

target_class = 5
trigger_label = 2

trigger_pattern = torch.ones((1, 3, 4))
trigger_position = (5, 5)

trojan_images, trojan_labels = add_custom_trigger(
    train_dataset.dataset.data.unsqueeze(1).float() / 255.0,
    train_dataset.dataset.targets,
    trigger_pattern,
    trigger_position,
    target_class,
    trigger_label)

combined_images = torch.cat([train_dataset.dataset.data[train_dataset.indices].unsqueeze(1).float() / 255.0, trojan_images])
combined_labels = torch.cat([train_dataset.dataset.targets[train_dataset.indices], trojan_labels])

trigger_pattern = torch.ones((1, 5, 5))
trigger_position = (17, 20)

trojan_images, trojan_labels = add_custom_trigger(
    train_dataset.dataset.data.unsqueeze(1).float() / 255.0,
    train_dataset.dataset.targets,
    trigger_pattern,
    trigger_position,
    target_class,
    trigger_label)

combined_images = torch.cat([combined_images, trojan_images])
combined_labels = torch.cat([combined_labels, trojan_labels])
class MLP(nn.Module):
	def __init__(self):
		super(MLP, self).__init__()
		self.fc1 = nn.Linear(784, 128)
		self.fc2 = nn.Linear(128, 10)
	def forward(self, x):
		x = x.view(x.size(0), -1)
		x = torch.relu(self.fc1(x))
		x = self.fc2(x)

		return x

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MLP().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

val_accuracies = []
for epoch in range(num_epochs):
    for i in range(0, len(combined_images), batch_size):
        images = combined_images[i:i+batch_size].to(device)
        labels = combined_labels[i:i+batch_size].to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch [{epoch+1}/10], Loss: {loss.item():.4f}")
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    val_accuracy = correct / total
    val_accuracies.append(val_accuracy)




def test_backdoor(model, test_dataset, trigger_pattern, trigger_position, target_class):
    model.eval()
    with torch.no_grad():
        # Select images of the target class
        target_indices = (test_dataset.dataset.targets == target_class).nonzero(as_tuple=True)[0]
        images = test_dataset.dataset.data[target_indices].unsqueeze(1).float() / 255.0
        labels = test_dataset.dataset.targets[target_indices]

        # Add the trigger
        x, y = trigger_position
        a, b = trigger_pattern.shape[1], trigger_pattern.shape[2]
        images[:, :, x:x+a, y:y+b] = trigger_pattern

        # Predict
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        # Calculate accuracy
        accuracy = (predicted == trigger_label).float().mean()
        print(f"Backdoor success rate: {accuracy.item() * 100:.2f}%")

test_backdoor(model, test_dataset, trigger_pattern, trigger_position, target_class)
def show_samples(original_images, backdoored_images, labels, target_class, trigger_label, num_samples=5):
    """
    Displays a grid of original and backdoored samples.

    Args:
        original_images (torch.Tensor): Original images (N, C, H, W).
        backdoored_images (torch.Tensor): Backdoored images (N, C, H, W).
        labels (torch.Tensor): Labels for the images (N,).
        target_class (int): The class that was backdoored.
        trigger_label (int): The target label for the backdoor.
        num_samples (int): Number of samples to display.
    """
    # Find indices of the target class
    target_indices = (labels == target_class).nonzero(as_tuple=True)[0]

    # Select a few samples to display
    sample_indices = target_indices[:num_samples]

    # Create a figure to display the images
    plt.figure(figsize=(10, 4))
    plt.suptitle(f"Benign vs Backdoored Samples (Class {target_class} → {trigger_label})", fontsize=14)

    for i, idx in enumerate(sample_indices):
        # Plot the original image
        plt.subplot(2, num_samples, i + 1)
        plt.imshow(original_images[idx].squeeze(), cmap='gray')
        plt.title(f"Benign\nLabel: {labels[idx].item()}")
        plt.axis('off')

        # Plot the backdoored image
        plt.subplot(2, num_samples, num_samples + i + 1)
        plt.imshow(backdoored_images[idx].squeeze(), cmap='gray')
        plt.title(f"Backdoored\nLabel: {trigger_label}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Example usage
# Assuming `train_dataset` is the original dataset and `trojan_images` contains the backdoored images
original_images = train_dataset.dataset.data[train_dataset.indices].unsqueeze(1).float() / 255.0
backdoored_images = trojan_images
labels = train_dataset.dataset.targets[train_dataset.indices]

# Display samples
show_samples(original_images, backdoored_images, labels, target_class, trigger_label, num_samples=10)



model.eval()
y_true, y_pred = [], []
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        y_true.extend(labels.cpu().numpy())
        y_pred.extend(predicted.cpu().numpy())

precision = precision_score(y_true, y_pred, average='macro')
print(f"Test Precision: {precision:.4f}")



plt.plot(range(1, num_epochs+1), val_accuracies, marker='o', linestyle='-')
plt.xlabel("Epoch")
plt.ylabel("Validation Accuracy")
plt.title("Validation Accuracy Over Epochs")
plt.grid()
plt.show()



conf_matrix = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=range(10), yticklabels=range(10))
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()


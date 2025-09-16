from accelerate import Accelerator
import torch

# Initialize accelerator
accelerator = Accelerator()

# Create a simple model, optimizer, and data
model = torch.nn.Linear(10, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Some dummy data
x = torch.randn(16, 10)
y = torch.randn(16, 1)

# Prepare model, optimizer, and data with accelerator
model, optimizer, x, y = accelerator.prepare(model, optimizer, x, y)

# Training step
for _ in range(5):
    optimizer.zero_grad()
    output = model(x)
    loss = torch.nn.functional.mse_loss(output, y)
    accelerator.backward(loss)  # handles device automatically
    optimizer.step()
    print(f"Loss: {loss.item():.4f}")

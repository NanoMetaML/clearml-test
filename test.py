import torch
import torch.nn as nn

from clearml import Task


task = Task.init(
    project_name='test-clearml',    # project name of at least 3 characters
    task_name='test-name', # task name of at least 3 characters
    task_type=None,
    tags=None,
    reuse_last_task_id=True,
    continue_last_task=False,
    output_uri=None,
    auto_connect_arg_parser=True,
    auto_connect_frameworks=True,
    auto_resource_monitoring=True,
    auto_connect_streams=True,    
)

params = {
        'device': 'cuda', # Options: cuda, cpu
        'in_dim': 10,
        'h_dim': 8,
        'num_samples': 100,
        }

# tell clearml about our parameters
task.connect(params)

# create a PyTorch model
model = nn.Sequential(nn.Linear(params['in_dim'], params['h_dim']), nn.ReLU(), nn.Linear(params['h_dim'], 1))

# create a dummy PyTorch dataset using a random 
x = torch.randn(params['num_samples'], params['in_dim'])

y = torch.pow(x, 2) @ torch.randn(params['in_dim'], 1) + torch.randn(params['num_samples'], 1)

# create a loss function
loss_fn = nn.MSELoss()

# create an optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

# train the model
for t in range(100):

    # forward pass
    y_pred = model(x)

    # compute loss
    loss = loss_fn(y_pred, y)

    # backward pass
    loss.backward()

    # update parameters
    optimizer.step()

    # zero the gradients
    optimizer.zero_grad()

    # report loss
    task.get_logger().report_scalar(title="loss", series="loss", value=loss.item(), iteration=t)

# save the model
torch.save(model.state_dict(), "model.pt")

# upload the model
task.upload_artifact(name="model.pt", artifact_object="./model.pt")


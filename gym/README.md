This directory contains modified versions of control tasks of OpenAI gym. The code base is forked from the [original 
repository](https://github.com/openai/gym), and is modified accordingly.

## Installation
Install [OpenAI gym](https://gym.openai.com/).

Then install this package:

```
git clone http://github.com/modanesh/anomalous_rl_envs.git
cd anomalous_rl_envs/gym
pip install -e .
```

## Usage
Python usage:
```python
import gym
import anomalous_gym
env = gym.make('CartPoleMod-v0')
# anomaly_time = setting when to inject anomaly in the trajectory
env.when_anomaly_starts = anomaly_time
```

## Environments Description
- [x] **envnameMod-v0**: starting from a time step, wind from left to right (L2R) starts to blow, changes 50% of the **left** and **right** actions to **noop**. 
- [x] **envnameMod-v1**: starting from a time step, IID noise is applied to a group of sensors.
- [x] **envnameMod-v2**: starting from a time step, sensor shutdown noise is applied to a group of sensors.
- [x] **envnameMod-v3**: starting from a time step, calibration failure noise is applied to a group of sensors.
- [x] **envnameMod-v4**: starting from a time step, sensor drift noise is applied to a group of sensors.

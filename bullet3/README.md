In this project, there are anomalous versions of PyBullet physics simulations. Source code is quite similar to the [main
repositoty](https://github.com/bulletphysics/bullet3/). We encourage you to first take a look at the official repo, and then
start working with this version.

## Installation
Install [PyBullet3](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit#heading=h.2ye70wns7io3).

Then install this package:

```
git clone http://github.com/modanesh/anomalous_rl_envs.git
cd anomalous_rl_envs/bullet3
pip install -e .
```

## Usage
Python usage:
```
import gym
import pybullet_envs
import env_preparation

random_seed = 15
anomalous_power = 0.5
anomaly_injection = 100
case = 1

env = DummyVecEnv(
            [env_preparation.make_env("Walker2DBulletEnv-v0", 0, random_seed, wrapper_class=env_preparation.TimeFeatureWrapper,
                                      env_kwargs={'power': anomalous_power,
                                                  'anomaly_injection': anomaly_injection,
                                                  'case': case})])
```

## Environments
Instead of defining new environments, a few new parameters is defined to minimize the effort of designing anomalies for different environments.
The new defined parameters are:

- `anomaly_injection`: when to inject anomaly into the trajectory. 
- `power`: what the new power applied to the agent should be. The higher, the more destructive.
- `case`: what type of noise should be applied. Available types are:
    - 1: IID noise
    - 2: sensor shutdown
    - 3: calibration failure
    - 4: sensor drift

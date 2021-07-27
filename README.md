# Anomalous RL Environments

⭐️ [Approved by OpenAI Gym](https://github.com/openai/gym/blob/master/docs/environments.md#anomalous-rl-envs-providing-anomalous-control-tasks) ⭐️

In this repo, two sets of environments exist: **OpenAI gym** and **PyBullet3**. The codebase is based on and forked from
their corresponding repositories, [here](https://github.com/openai/gym) and [here](https://github.com/bulletphysics/bullet3/), respectively.


## Description

For each environment, we generate various types of anomalous trajectories which follow the nominal dynamics until a desired 
time point upon which there is a switch to anomalous dynamics. The anomalous dynamics correspond to different ways of 
modifying the state features provided to the controllers through sensors. Note that such modifications can impact the 
behavior of the controllers, which in turn can impact the evolution of the trajectories. Importantly, we avoid modifications 
that cause a controller to completely fail (e.g., falling or crashing) soon after the anomaly is introduced. This is because: first,
such failures are easy to detect, and second, they do not allow testing the robustness abilities of the agent.

The anomalous dynamics that are injected into the trajectory are in a way to resemble the real-world dynamic changes which happen to affect the agent's behavior.
Such dynamic changes could be due to many reasons. Here, 4 types of modifications can be applied to the trajectory at the desired time point, each with a different purpose and result. The 4 types are:
- **IID Noise**: Gaussian noise is added to the features. For each environment, the mean and standard deviation is selected to avoid near-term failure of the controller.

- **Sensor Shutdown**: The sensor's output changes to zero immediately after the anomaly and stays at zero for the rest of the run. If applied to the most important features for a policy, it could easily degrade the performance. It resembles the case where a sensor fails and needs to be replaced. 

- **Sensor Calibration Failure**: It multiplies the sensor's output by a constant throughout the anomalous run. Similar to the IID noise, for each case study, there is a specific pre-determined constant.

- **Sensor Drift**: Relative to the time step in a trajectory, a small amount of noise is injected into the chosen sensor. As the trajectory progresses, the magnitude of the injected noise increases.

More details and how to use each set of environment is provided in its corresponding directory.


## Environments
From OpenAI gym, only classic control tasks are considered: Acrobot, CartPole, and LunarLander. From PyBullet3, 4 environments
are considered to be modified: Ant, Hopper, HalfCheetah, and Walker2D.

## Baseline
Explanation on what this repo proposes is provided in this paper: [Out-of-Distribution Dynamics Detection: RL-Relevant Benchmarks and Results]().
Also, the paper contains detailed information on designing a strong out-of-distribution dynamics (OODD) baseline approach 
based on recurrent implicit quantile networks (RIQNs), which monitors autoregressive prediction errors for OODD detection. 
The baseline is evaluated on this benchmark to provide results for future comparison. The code of the baseline is in this repo: [Recurrent Implicit Quantile Networks](https://github.com/modanesh/recurrent_implicit_quantile_networks).

### Citation
If you ever used this repo in your work, please cite it with:
```
@inproceedings{danesh2021oodd,
  title={Out-of-Distribution Dynamics Detection: RL-Relevant Benchmarks and Results},
  author={Danesh, Mohamad H and Fern, Alan},
  booktitle={International Conference on Machine Learning, Uncertainty & Robustness in Deep Learning Workshop},
  journal={},
  year={2021}
}
```

## TODO
- [ ] Add new types of anomalies to inject into the environment


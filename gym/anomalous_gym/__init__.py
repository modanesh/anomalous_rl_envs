import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='AcrobotMod-v0',
    entry_point='anomalous_gym.envs:ModAcrobotEnv',
    kwargs={'case':0}
)
register(
    id='AcrobotMod-v1',
    entry_point='anomalous_gym.envs:ModAcrobotEnv',
    kwargs={'case':1}
)
register(
    id='AcrobotMod-v2',
    entry_point='anomalous_gym.envs:ModAcrobotEnv',
    kwargs={'case':2}
)
register(
    id='AcrobotMod-v3',
    entry_point='anomalous_gym.envs:ModAcrobotEnv',
    kwargs={'case':3}
)
register(
    id='AcrobotMod-v4',
    entry_point='anomalous_gym.envs:ModAcrobotEnv',
    kwargs={'case':4}
)
register(
    id='CartPoleMod-v0',
    entry_point='anomalous_gym.envs:ModCartPoleEnv',
    kwargs={'case':0, 'max_episode_steps':500},
)
register(
    id='CartPoleMod-v1',
    entry_point='anomalous_gym.envs:ModCartPoleEnv',
    kwargs={'case':1, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v2',
    entry_point='anomalous_gym.envs:ModCartPoleEnv',
    kwargs={'case':2, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v3',
    entry_point='anomalous_gym.envs:ModCartPoleEnv',
    kwargs={'case':3, 'max_episode_steps':500}
)
register(
    id='CartPoleMod-v4',
    entry_point='anomalous_gym.envs:ModCartPoleEnv',
    kwargs={'case':4, 'max_episode_steps':500}
)
register(
    id='LunarLanderMod-v0',
    entry_point='anomalous_gym.envs:ModLunarLanderEnv',
    kwargs={'case':0}
)
register(
    id='LunarLanderMod-v1',
    entry_point='anomalous_gym.envs:ModLunarLanderEnv',
    kwargs={'case':1}
)
register(
    id='LunarLanderMod-v2',
    entry_point='anomalous_gym.envs:ModLunarLanderEnv',
    kwargs={'case':2}
)
register(
    id='LunarLanderMod-v3',
    entry_point='anomalous_gym.envs:ModLunarLanderEnv',
    kwargs={'case':3}
)
register(
    id='LunarLanderMod-v4',
    entry_point='anomalous_gym.envs:ModLunarLanderEnv',
    kwargs={'case':4}
)
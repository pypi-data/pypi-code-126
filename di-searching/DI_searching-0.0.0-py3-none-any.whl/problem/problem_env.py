import gym
import copy
import numpy as np
from easydict import EasyDict
from typing import Any, Callable, Dict, List, Optional, Tuple

from .utils import DataPool
from ding.envs import BaseEnv, BaseEnvTimestep
from ding.utils.default_helper import deep_merge_dicts
from ding.utils import ENV_REGISTRY


@ENV_REGISTRY.register('problem_env')
class ProblemEnv(BaseEnv):

    config = dict(
        episode_len=float("inf"),
        init_type='zero',
        batch_num=1,
    )

    reward_space = gym.spaces.Box(low=0.0, high=1.0, shape=(1, ), dtype=np.float32)

    def __init__(
            self,
            cfg: Dict,
            search_space: "BaseSpace",  # noqa
            target_func: Callable,
    ) -> None:
        if 'cfg_type' not in cfg:
            self._cfg = self.__class__.default_config()
            self._cfg = deep_merge_dicts(self._cfg, cfg)
        else:
            self._cfg = cfg
        self._search_space = search_space
        self._obs_shape = self._search_space.shape
        self._data_pool = DataPool(search_space)
        self._target_func = target_func
        self._state = None

        self._episode_len = self._cfg.episode_len
        assert self._cfg.init_type in ['zero', 'random'], self._cfg.init_type
        self._batch_num = self._cfg.batch_num
        self._step_count = 0

    @property
    def ready_obs(self) -> Dict:
        obs = {}
        if self._state is None:
            return obs
        for env_id in range(self._batch_num):
            obs[env_id] = self._state[env_id]
        return obs

    @property
    def env_num(self) -> int:
        return self._batch_num

    def set_episode_len(self, episode_len: int) -> None:
        self._episode_len = min(episode_len, self._episode_len)

    def launch(self) -> None:
        self.reset()

    def reset(self, starting_point: Optional[np.ndarray] = None) -> None:
        self._step_count = 0
        if starting_point is None:
            if self._cfg.init_type == 'zero':
                single_obs = np.zeros(shape=self._obs_shape, dtype=np.float32)
            elif self._cfg.init_type == 'random':
                single_obs = self._search_space.sample()
        else:
            single_obs = starting_point
        self._state = np.stack([single_obs] * self._batch_num).astype(np.float32)

    def step(self, actions) -> Dict[int, BaseEnvTimestep]:
        env_ids = actions.keys()
        self._state = np.asarray(list(actions.values())).astype(np.float32)
        scores = np.apply_along_axis(self._target_func, axis=0, arr=self._state)
        self._data_pool.update(self._state, scores)
        self._step_count += 1
        done = self._step_count > self._episode_len
        timesteps = {}
        for env_id in env_ids:
            obs = self._state[env_id]
            reward = scores[env_id]
            info = {'final_eval_reward': scores[env_id]}
            timesteps[env_id] = BaseEnvTimestep(obs, reward, done, info)
        return timesteps

    def close(self) -> None:
        self._data_pool.clear()
        return

    def seed(self, seed: int, dynamic_seed: bool = True) -> None:
        self._seed = seed
        self._dynamic_seed = dynamic_seed
        np.random.seed(self._seed)

    @property
    def best(self) -> Tuple[np.ndarray, float]:
        return self._data_pool.best

    def __repr__(self) -> str:
        return super().__repr__()

    @classmethod
    def default_config(cls: type) -> EasyDict:
        cfg = EasyDict(copy.deepcopy(cls.config))
        cfg.cfg_type = cls.__name__ + 'Dict'
        return cfg
